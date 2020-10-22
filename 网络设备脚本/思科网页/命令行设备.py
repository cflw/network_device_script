import time
import selenium.webdriver	#selenium
from ..网页接口 import 设备 as 网页设备
from ..网页接口 import 元素
from ..命令行接口 import 命令
from ..命令行接口 import 设备 as 命令行设备
from ..思科命令行.常量 import *
from . import 命令行用户模式 as 实现用户模式
class C设备(网页设备.I设备, 命令行设备.I设备):
	"""适用于: c7200"""
	def __init__(self, a连接, a型号, a版本):
		网页设备.I设备.__init__(self, a连接)
		命令行设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.ma模式栈 = []
	#网页
	def fg命令框(self, a包装 = True):
		w命令框 = self.f查找("/html/body/pre/form/dt/input[2]", a包装)
		return w命令框
	#适配
	def f输出(self):
		w输出框 = self.f查找("/html/body/pre/form/dt/pre", False)
		return w输出框.text
	def f输入(self, a文本):
		w命令框 = self.fg命令框(False)
		w命令框.send_keys(str(a文本))
	def f输入_回车(self, a数量 = 1, a等待 = 1):
		w命令框 = self.fg命令框(False)
		v间隔 = a等待 / a数量
		for i in range(a数量):
			w命令框.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
			time.sleep(v间隔)
	def f输入_结束符(self):
		v地址 = self.fg地址()	#http://192.168.1.10/level/15/exec/-
		if "exec/-" in v地址:	#命令页
			v元素 = self.f查找("/html/body/pre/a[2]")
			v元素.f点击()
		else:	#主页
			v元素 = self.f查找("/html/body/menu/dl/dt[2]/a[1]")
			v元素.f点击()
	def f刷新(self):
		w命令框 = self.fg命令框(False)
		w命令框.clear()
		w命令框.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
	def f切换到当前连接(self):
		pass
	#模式
	def f模式_用户(self):
		return 实现用户模式.C用户模式(self)
	def f模式_配置(self):
		from . import 命令行全局配置 as 实现全局配置
		return 实现全局配置.C全局配置(self)
	#命令
	def f退出(self):
		self.f执行命令("exit")
	def f执行命令(self, a命令):
		w命令框 = self.fg命令框(False)
		w命令框.send_keys(str(a命令))
		w命令框.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
		time.sleep(0.5)
		return self.f输出()
	def f执行用户命令(self, a命令):
		v命令 = 命令.C命令(a命令)
		if not isinstance(self.fg当前模式(), 实现用户模式.C用户模式):
			v命令.f前面添加(c做)
		return self.f执行命令(v命令)
	def f执行显示命令(self, a命令, a自动换页 = None):
		return self.f执行用户命令(a命令)