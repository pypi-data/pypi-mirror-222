# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - Resource SDK (BlueKing - Resource SDK) available.
Copyright (C) 2023 THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.
We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""

from functools import partial
from multiprocessing.pool import ThreadPool as _ThreadPool
from threading import Thread

from django import db
from django.utils import timezone, translation

from bk_resource.utils.local import local
from bk_resource.utils.logger import logger


class InheritParentThread(Thread):
    def __init__(self, *args, **kwargs):
        self.inherit_data = [item for item in local]
        self.timezone = timezone.get_current_timezone().zone
        self.language = translation.get_language()
        super(InheritParentThread, self).__init__(*args, **kwargs)

    def sync(self):
        for sync_item in self.inherit_data:
            setattr(local, sync_item[0], sync_item[1])
        timezone.activate(self.timezone)
        translation.activate(self.language)

    def unsync(self):
        # 新的线程会往local再写一些数据
        # 线程结束的时候，需要把所有线程相关的所有变量都清空
        for item in local:
            delattr(local, item[0])

        # db._connections 也是线程变量，所以在线程结束的时候需要主动的释放
        db.connections.close_all()

    def run(self):
        self.sync()
        try:
            super(InheritParentThread, self).run()
        except Exception as e:
            logger.exception(e)

        self.unsync()


def run_func_with_local(items, tz, lang, func, *args, **kwargs):
    """
    线程执行函数
    :param func: 待执行函数
    :param items: Thread Local Items
    :param tz: 时区
    :param lang: 语言
    :param args: 位置参数
    :param kwargs: 关键字参数
    :return: 函数返回值
    """
    # 同步local数据
    for item in items:
        setattr(local, item[0], item[1])

    # 设置时区及语言
    timezone.activate(tz)
    translation.activate(lang)

    try:
        data = func(*args, **kwargs)
    except Exception as e:
        raise e
    finally:
        # 关闭db连接
        db.connections.close_all()

        # 清理local数据
        for item in local:
            delattr(local, item[0])

    return data


class ThreadPool(_ThreadPool):
    """
    线程池
    """

    @staticmethod
    def get_func_with_local(func):
        tz = timezone.get_current_timezone().zone
        lang = translation.get_language()
        items = [item for item in local]
        return partial(run_func_with_local, items, tz, lang, func)

    def map_ignore_exception(self, func, iterable, return_exception=False):
        """
        忽略错误版的map
        """
        futures = []
        for params in iterable:
            if not isinstance(params, (tuple, list)):
                params = (params,)
            futures.append(self.apply_async(func, args=params))

        results = []
        for future in futures:
            try:
                results.append(future.get())
            except Exception as e:
                if return_exception:
                    results.append(e)
                logger.exception(e)

        return results

    def map_async(self, func, iterable, chunksize=None, callback=None, error_callback=None):
        return super(ThreadPool, self).map_async(
            self.get_func_with_local(func),
            iterable,
            chunksize=chunksize,
            callback=callback,
            error_callback=error_callback,
        )

    def apply_async(self, func, args=(), kwds=None, callback=None, error_callback=None):
        if kwds is None:
            kwds = {}
        return super(ThreadPool, self).apply_async(
            self.get_func_with_local(func), args=args, kwds=kwds, callback=callback, error_callback=error_callback
        )

    def imap(self, func, iterable, chunksize=1):
        return super(ThreadPool, self).imap(self.get_func_with_local(func), iterable, chunksize)

    def imap_unordered(self, func, iterable, chunksize=1):
        func = partial(run_func_with_local, func, local)
        return super(ThreadPool, self).imap_unordered(self.get_func_with_local(func), iterable, chunksize=chunksize)


if __name__ == "__main__":
    InheritParentThread().start()
