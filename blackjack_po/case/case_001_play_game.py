# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/27 上午 10:48
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : case_001_play_game.py
# @Software : PyCharm
import unittest
from blackjack_po.page.game_screen import GameScreen
from blackjack_po.page.main_menu_screen import MainMenuScreen
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class PlayGame(unittest.TestCase):
    def setUp(self) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=None, devices=[
                "android://127.0.0.1:5037/127.0.0.1:62025?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
            ], project_root="D:/pyworkspace/airtest_demo1/blackjack_po")
        start_app('org.cocos2d.blackjack')

        self.mms = MainMenuScreen()
        self.gs = GameScreen()

    def test(self):
        #点击快速开始
        self.mms.quick_start()
        #点击10k
        self.gs.touch_10k()
        #点击投注
        self.gs.touch_bet()
        #点击停牌
        self.gs.touch_hit()
        #点击下注
        self.gs.touch_start()
        #点击返回
        self.gs.back()

    def tearDown(self) -> None:
        gs = None
        mms = None
        stop_app('org.cocos2d.blackjack')
