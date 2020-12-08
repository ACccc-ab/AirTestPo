# -*- encoding=utf8 -*-
__author__ = "LiJie"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "android://127.0.0.1:5037/127.0.0.1:62025?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
    ], project_root="D:/pyworkspace/airtest_demo1/weixin")

# script content
print("start...")

start_app("com.tencent.mm")

wait(Template(r"tpl1606467832978.png", record_pos=(-0.001, -0.785), resolution=(720, 1280)))

swipe((360, 640), (360, 1280))

wait(Template(r"tpl1606468127422.png", record_pos=(-0.339, -0.344), resolution=(720, 1280)))
touch(Template(r"tpl1606468127422.png", record_pos=(-0.339, -0.344), resolution=(720, 1280)))

wait(Template(r"tpl1606468331024.png", record_pos=(-0.003, 0.525), resolution=(720, 1280)))
touch(Template(r"tpl1606468331024.png", record_pos=(-0.003, 0.525), resolution=(720, 1280)))

#点击广告X
wait(Template(r"tpl1606468410766.png", record_pos=(0.361, -0.403), resolution=(720, 1280)))
touch(Template(r"tpl1606468410766.png", record_pos=(0.361, -0.403), resolution=(720, 1280)))


# #点击第一件商品+
# wait(Template(r"tpl1606468983488.png", record_pos=(-0.253, 0.771), resolution=(720, 1280)))
# touch(Template(r"tpl1606468983488.png", record_pos=(-0.253, 0.771), resolution=(720, 1280)))
#
# #点击购物车
# wait(Template(r"tpl1606469034845.png", record_pos=(-0.435, 0.797), resolution=(720, 1280)))
# touch(Template(r"tpl1606469034845.png", record_pos=(-0.435, 0.797), resolution=(720, 1280)))
#
# #点击清空
# wait(Template(r"tpl1606469068652.png", record_pos=(0.389, 0.407), resolution=(720, 1280)))
# touch(Template(r"tpl1606469068652.png", record_pos=(0.389, 0.407), resolution=(720, 1280)))


#点击搜索
wait(Template(r"tpl1606469285413.png", record_pos=(-0.415, -0.633), resolution=(720, 1280)))
touch(Template(r"tpl1606469285413.png", record_pos=(-0.415, -0.633), resolution=(720, 1280)))

#点击输入框
wait(Template(r"tpl1606469329755.png", record_pos=(0.083, -0.64), resolution=(720, 1280)))
touch(Template(r"tpl1606469329755.png", record_pos=(0.083, -0.64), resolution=(720, 1280)))

#输入搜索词
text("麦乐鸡")

# generate html report
simple_report(__file__, logpath=True)





