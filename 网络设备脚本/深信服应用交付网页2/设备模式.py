from ..基础接口 import 设备模式
from . import 模式
t模式 = 模式.C模式_ad705
class C授权管理页:
	"""适用于: ad 7.0.8R5"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f切换并查找序列号(self, a序号: str):
		self.m设备.f切换模式(t模式.c系统管理_通用配置_授权管理)
		if not hasattr(self, "ma序列号"):
			self.ma序列号 = []
			#先找框,然后找序列号.序列号顺序固定
			w序列号总框 = self.m设备.f查找("//div[@class=\"mod_system__authorize__box\"]")
			for w单个序列号框 in w序列号总框.fe查找("div"):
				if w序列号 := w单个序列号框.f查找("//span[@class=\"mod_system__authorize__sn_text\"]"):
					v序列号s = w序列号.fg文本()[4:]	#前4个字符是"序列号："要去掉
					self.ma序列号.append(v序列号s)
				else:
					self.ma序列号.append(None)
		return self.ma序列号[a序号]
	def fg网关序号(self):
		self.m设备.f切换模式(t模式.c系统管理_通用配置_授权管理)
		w序列号 = self.m设备.f查找("//div[@utid=\"gwid\"]")
		return w序列号.fg文本()
	def fg基本授权序列号(self):
		return self.f切换并查找序列号(0)
	def fgSSL卸载授权序列号(self):
		return self.f切换并查找序列号(1)
	def fgTCP单边加速授权序列号(self):
		return self.f切换并查找序列号(2)
	def fgHTTP缓存授权序列号(self):
		return self.f切换并查找序列号(3)
	def fg智能DNS全局授权序列号(self):
		return self.f切换并查找序列号(4)
	def fg软件升级授权序列号(self):
		return self.f切换并查找序列号(5)
class C设备显示_ad705(设备模式.I设备显示, C授权管理页):
	"""适用于: """
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_序列号(self):	#返回网关ID
		return self.fg网关序号()
