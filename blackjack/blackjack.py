# -*- encoding=utf8 -*-
__author__ = "LiJie"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:62025?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
    ], project_root="D:/pyworkspace/airtest_demo1/blackjack")

# script content
print("start...")

# 启动App(也可以点击图标运行)
start_app('org.cocos2d.blackjack')
sleep(3)

#点击快速启动，也可以只用坐标点击
touch(Template('./pic/快速启动.png'))
# touch((913, 160))
sleep(3)

#点击筹码10k
touch(Template(r"./pic/10k.png"))
sleep(3)

#点击投注
touch(Template(r"./pic/投注.png"))
sleep(3)

#点击停牌
touch(Template(r"./pic/停牌.png"))
sleep(3)

#点击下注poco("android:id/content")poco("android.widget.FrameLayout")
touch(Template(r"./pic/下注.png"))
sleep(3)

#点击返回
touch(Template(r"./pic/返回.png"))
sleep(3)

#关闭App
stop_app('org.cocos2d.blackjack')

# generate html report
from airtest.report.report import simple_report
simple_report(__file__, logpath=True)





