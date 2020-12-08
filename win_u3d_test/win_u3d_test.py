# -*- encoding=utf8 -*-
__author__ = "LiJie"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Windows:///6425326",
    ], project_root="D:/pyworkspace/airtest_demo1/win_u3d_test")


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

touch(Template(r"tpl1606726160313.png", record_pos=(0.0, -0.082), resolution=(1656, 947)))

sleep(2)

touch(Template(r"tpl1606726220923.png", record_pos=(-0.354, -0.165), resolution=(1656, 947)))
sleep(2)

touch(Template(r"tpl1606726296019.png", record_pos=(0.001, 0.047), resolution=(1656, 947)))
sleep(2)

text("汇智动力")
sleep(2)

touch(Template(r"tpl1606726400764.png", record_pos=(-0.431, 0.206), resolution=(1656, 947)))
sleep(2)

touch(Template(r"tpl1606726489120.png", record_pos=(-0.354, -0.094), resolution=(1656, 947)))
sleep(2)

swipe(Template(r"tpl1606727788110.png", record_pos=(-0.336, -0.102), resolution=(1320, 722)),Template(r"tpl1606727841951.png", record_pos=(0.008, 0.108), resolution=(1320, 722)))
sleep(2)

swipe(Template(r"tpl1606727895882.png", record_pos=(-0.158, -0.104), resolution=(1320, 722)),Template(r"tpl1606727841951.png", record_pos=(0.008, 0.108), resolution=(1320, 722)))
sleep(2)


swipe(Template(r"tpl1606728040628.png", record_pos=(0.011, -0.102), resolution=(1320, 722)),Template(r"tpl1606727841951.png", record_pos=(0.008, 0.108), resolution=(1320, 722)))
sleep(2)

swipe(Template(r"tpl1606727895882.png", record_pos=(-0.158, -0.104), resolution=(1320, 722)),Template(r"tpl1606727841951.png", record_pos=(0.008, 0.108), resolution=(1320, 722)))
sleep(2)

swipe(Template(r"tpl1606727895882.png", record_pos=(-0.158, -0.104), resolution=(1320, 722)),Template(r"tpl1606727841951.png", record_pos=(0.008, 0.108), resolution=(1320, 722)))
sleep(2)

assert_exists(Template(r"tpl1606728195348.png", record_pos=(-0.311, -0.217), resolution=(1320, 722)))


