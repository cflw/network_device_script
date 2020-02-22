from ..简单网管接口 import 设备
class C设备(设备.I设备):
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
	def f模式_配置(self):
		from . import 全局配置
		return 全局配置.C全局配置(self)
	def f模式_显示(self):
		from . import 全局显示
		return 全局显示.C全局显示(self)