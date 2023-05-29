https://www.hzdledu.cn/hzzx/jswz/2695.html

Airtest自动化测试——PO模式编写Airtest测试用例
日期：2022-04-01 17:32:59 访问量：418 来源：
目录

1. PO模式

2. Airtest项目中PO模式的运用

 

1. PO模式

PO模式或POM模式，被称为Page Object Model，页面对象模型。

 

其基本思想是以面对对象编程为基础，将每个界面抽象为类，将界面的元素封装为类的属性，将界面的操作封装为方法。

Airtest自动化测试
 

1.1 PO模式的分层

项目的基本结构按照PO模型从上到下分为三层或四层：

 

三层：

1. 运行层

2. 用例层

3. 页面层

 

四层：

1. 运行层

2. 用例层

3. 页面层

4. 基础操作层

 

1.2 运行层

运行层run.py文件，调用用例层的用例，生成报告

 

1.3 用例层

用例层case文件夹，生成页面类对象，调用页面类的方法实现用例的流程操作，不涉及具体的页面操作

 

1.4 页面层

页面层page文件夹，包含所有页面类，编写页面的元素信息和对页面元素的操作

 

1.5 基础操作层

基础操作层basePage文件夹，主要是把一些基础操作，比如click、touch、swipe等和相应的等待语句，wait或sleep，以及相应的异常捕获和截图进行二次封装

建议先熟悉三层的PO模式再过渡到4层的PO模式，更好理解项目架构

 

2. Airtest项目中PO模式的运用

这里以blackjack.apk游戏demo为范例，讲解项目中如何使用PO三层模式

 

2.1 项目架构

 
 
Airtest自动化测试
 

一般按照从下到上的方式构建，比较方便调试，因此一般的构建顺序是：

1. 构建页面层

2. 构建用例层

3. 编写运行层

 

2.2 构建页面层

将页面元素的截图定义为页面类的属性

将页面元素的操作定义为页面类的方法

 

例如：main_menu_screen.py

 
 
Airtest自动化测试
 

2.3 编写用例层

按照分层思想，用例层只生成页面类的对象，并通过页面对象调用相应的方法实现操作，不要涉及具体的元素操作。

 

例如：case_001_play_game.py

 
Airtest自动化测试
 

建议每个用例单独初始化设备并连接，开关一次App，避免用例多了以后的互相干扰

 

2.4 编写运行层

负责调用要执行的用例，以及生成报告，不要涉及页面操作

 

例如：run.py

 
Airtest自动化测试
 

2.5 pic文件夹

页面的层的元素截图都放在此文件夹，在编写页面层的页面类时使用，可按照界面继续生成子文件夹分类

例如：blackjack/pic/main_menu_screen/快速开始.png

Airtest自动化测试
 

最好在页面类的元素截图路径使用相对路径，方便项目移植和后续的持续集成

 

2.6 log文件夹

log文件夹下的截图和log.txt在运行时自动生成，可以通过修改run.py中的语句

Airtest自动化测试
中的__file__、logdir=True、logpath=True来修改

 

2.7 运行

 

2.7.1 运行单个用例

直接对用例文件右键或快捷键ctrl+shift+F10运行blackjack/case文件下的某个用例，例如

case_001_play_game.py

 

2.7.2 运行多个用例

默认是扫描项目下case文件夹的所有py文件

suite = unittest.defaultTestLoader.discover('./case/', pattern='*.py')

 

可以更改扫描文件夹和pattern里的正则表达式只执行某个模块用例，或者某些用例，例如：

suite = unittest.defaultTestLoader.discover('./case/', pattern='case_*.py')

#将只把case_开头的用例加入到测试套件

 

2.8 其它

演示项目的代码可以从gitee上下载：

https://gitee.com/jeknight/airtest/tree/master/blackjack_po