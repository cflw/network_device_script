import time
from ..网页接口 import 设备
from . import 模式
class C设备af8035(设备.I设备):
	"""适用于:v8.0.35~8.0.59
	8.0.35换新界面, 菜单位置和旧版本不一样"""
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.ma模式 = 模式.C模式_af8035.c首页
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式af8035(self)
	def f切换模式(self, aa模式: tuple, a等待元素 = None):
		#第1级在页面顶部, 第2级在左侧可展开/折叠, 默认展开, 第3,4级在左侧, 2,3,4在模式栈是同一级, 第5级在上侧
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
			v序号, v文本, v路径 = aa模式[j]
			w按钮 = self.f查找_直到(v路径, af条件 = (lambda e: e.fg文本() == v文本))
			w按钮.f点击()
			time.sleep(1)
		self.ma模式 = aa模式
		if a等待元素:
			self.f查找_直到(a等待元素)
		time.sleep(1)