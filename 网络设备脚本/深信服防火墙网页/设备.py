import time
from ..网页接口 import 设备
from . import 模式
class C设备(设备.I设备):
	"""适用于:v8.0.7~8.0.13"""
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.ma模式 = 模式.C模式af8.c运行状态_总览
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式(self)
	def f切换模式(self, aa模式: tuple, a等待元素 = None):
		#每一级判断是否相同,从不同的那一级开始切换
		if self.ma模式 == aa模式:
			return
		v原长度 = len(self.ma模式)
		v新长度 = len(aa模式)
		v长度 = min(v原长度, v新长度)
		for i in range(v长度):
			if self.ma模式[i] != aa模式[i]:
				break
		for j in range(i, v新长度):
			w按钮 = self.f查找_直到(aa模式[j])
			w按钮.f点击()
		self.ma模式 = aa模式
		if a等待元素:
			self.f查找_直到(a等待元素)
		time.sleep(1)
	def f切换模式_序号(self, aa模式: tuple):
		v层级 = len(a模式)
		w导航 = self.f查找("/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
		#一级菜单
		w菜单1 = w导航.f查找(f"div[{a模式[0]}]")	#ext-comp-1012
		w按钮1 = w菜单1.f查找("div[1]")	#ext-gen39
		w按钮1.f点击()
		if v层级 == 1:
			return
		#二级菜单
		w菜单2 = w菜单1.f查找(f"div/div/ul/div/li[{a模式[1]}]")
		w按钮2 = w菜单1.f查找("div[1]")	#ext-gen39
		w按钮2.f点击()
		if v层级 == 2:
			return
		#三级菜单
		w菜单3 = w菜单2.f查找(f"ul[1]/li[{a模式[2]}]")
		w按钮3 = w菜单3.f查找("div[1]")
		w按钮3.f点击()
	def f切换子模式0(self, a模式: int):
		w导航 = self.f查找("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/ul")
	def f切换子模式1(self, a模式: int):
		w导航 = self.f查找("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/ul")