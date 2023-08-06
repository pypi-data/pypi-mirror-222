#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : product_task
# @Time         : 2023/7/27 09:02
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 写成服务
import pickle

from meutils.pipe import *
from celery_tasks.task01 import func_task

from celery_tasks.task02 import send_msg


# # get/post: 100
# for i in range(10):
#     task = send_msg.delay(i)
#     logger.info(f"Task: {task.id}")
def fn():
    return 66666


print(func_task(pickle.dumps(fn)).get())
