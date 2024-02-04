import time
import cflw代码库py.cflw字符串 as 字符串
from ..网页接口 import 设备
from . import 模式
class C设备_ad705(设备.I设备):
	"""适用于: ad 7.0.8"""
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.m主机 = None
		self.m会话标识 = None	#url中的x_id参数
		self.m当前模式 = None
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式_ad705(self)
	def f解析登录后地址(self):
		"""登录后调用
		解析"https://x.x.x.x/index?x_id=9dd00700-fcdd-11ea-bb09-c400ada9c07e" """
		v链接 = self.fg地址()
		self.m主机 = 字符串.f提取字符串之间(v链接, "//", "/")
		self.m会话标识 = 字符串.f提取字符串之间(v链接, "x_id=", "&", a结束严谨 = False)
	def f切换模式(self, aa模式: tuple):
		if self.m当前模式 == aa模式:
			return	#相同,不切换
		match len(aa模式):
			case 1:
				self.f切换模式_主模式(aa模式[0].m路径)
			case 2:
				self.f切换模式_主模式(aa模式[0].m路径)
				self.f切换模式_选项卡(aa模式[1].m路径)
			case _:
				raise ValueError()
		self.m当前模式 = aa模式
	def f切换模式_主模式(self, a路径: str):
		v地址 = f"https://{self.m主机}/index?x_id={self.m会话标识}#mod={a路径}"
		self.fs地址(v地址)
		time.sleep(0.5)
	def f切换模式_选项卡(self, a标识: str):
		w选项顶层 = self.f查找(f"//li[@utid=\"{a标识}\"]")
		w选项按钮 = w选项顶层.f查找("a[2]/em/span/span")
		w选项按钮.f点击()
		time.sleep(0.5)