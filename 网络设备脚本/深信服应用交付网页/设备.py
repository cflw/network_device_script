import time
import cflw代码库py.cflw字符串 as 字符串
from ..网页接口 import 设备
from . import 模式
class C设备ad70(设备.I设备):
	"""适用于: ad 7.0.3"""
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.m当前模式 = 模式.C模式ad70.c主页
		v链接 = self.fg地址()
		self.m主机 = 字符串.f提取字符串之间(v链接, "//", "/")
	def f切换模式(self, a模式: str):
		if self.m当前模式 == a模式:
			return
		v地址 = self.fg模式地址(a模式)
		self.fs地址(v地址)
		self.m当前模式 = a模式
	def fg模式地址(self, a模式: str):
		return f"https://{self.m主机}{a模式}"
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式ad70(self)
class C设备ad705(设备.I设备):
	"""适用于: ad 7.0.8"""
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.m主机 = None
		self.m标识 = None
		self.m当前模式 = None
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式ad705(self)
	def f解析登录后地址(self):
		"""登录后调用
		解析"https://x.x.x.x/index?x_id=9dd00700-fcdd-11ea-bb09-c400ada9c07e" """
		v链接 = self.fg地址()
		self.m主机 = 字符串.f提取字符串之间(v链接, "//", "/")
		self.m标识 = 字符串.f提取字符串之间(v链接, "x_id=", "&", a结束严谨 = False)
	def f切换模式(self, a模式):
		v类型 = type(a模式)
		if type(self.m当前模式) == v类型 and self.m当前模式 == a模式:
			return	#相同,不切换
		if v类型 == str:
			self.f切换模式_主模式(a模式)
		elif v类型 == tuple:
			self.f切换模式_主模式(a模式[0])
			self.f切换模式_选项卡(a模式[1])
		else:
			raise TypeError()
		self.m当前模式 = a模式
	def f切换模式_主模式(self, a模式: str):
		v地址 = f"https://{self.m主机}/index?x_id={self.m标识}#mod={a模式}"
		self.fs地址(v地址)
		time.sleep(0.5)
	def f切换模式_选项卡(self, a模式: str):
		w选项顶层 = self.f查找(f"//li[@utid=\"{a模式}\"]")
		w选项按钮 = w选项顶层.f查找("a[2]/em/span/span")
		w选项按钮.f点击()
		time.sleep(0.5)