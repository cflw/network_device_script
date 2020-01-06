import time
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 无线局域网
from . import 模式
class C无线电接口配置(无线局域网.I接口配置):
	"""适用于: wdr5620"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_主机表(self):
		return C主机表(self.m设备)
class C主机表:
	"""适用于: wdr5620"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def __iter__(self):
		return self.fe主机()
	def fe主机(self):
		self.m设备.f切换模式(模式.C模式wdr5620.c设备管理)
		i = 0
		while True:
			va元素 = list(self.m设备.fe查找("//*[@id='eptMngList']/div[@class='eptConC']"))
			if i >= len(va元素):
				break
			v元素 = va元素[i]
			w管理 = v元素.f查找("div/div/input[1]")
			w管理.f点击()
			w详细 = self.m设备.f查找("//*[@id='eptMngDetail']")
			w名称 = w详细.f查找("div/p/span/pre")
			v名称 = w名称.fg文本()
			w标题 = w详细.f查找("div/span")
			v网络地址s, v物理地址s, v连接方式s = w标题.fg文本().split("|")
			v物理地址 = 地址.S物理地址.fc字符串(v物理地址s.strip()[4:])
			yield 无线局域网.S主机表项(a名称 = v名称, a物理地址 = v物理地址)
			#结束
			w主人网络 = self.m设备.f查找("//*[@id='linkedEpt_rsMenu']")
			w主人网络.f点击()
			i += 1
