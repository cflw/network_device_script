import enum
from selenium.webdriver.common.by import By	#selenium
from ..网页接口 import 设备
class C设备(设备.I设备):
	"""适用于: mw155r"""
	c菜单框架 = "/html/frameset/frameset[2]/frame[1]"
	c主体框架 = "/html/frameset/frameset[2]/frame[2]"
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.ma模式 = ()
		self.m当前框架 = -1
		self.mi登录 = False
	def f切换模式(self, aa模式):
		if self.ma模式 == aa模式:
			return
		self.f切换框架(C设备.c菜单框架)
		#切换模式
		for v模式 in aa模式:
			v元素 = self.m连接.find_element(By.XPATH, f"/html/body/menu/ol[@id='ol{v模式}']/a[1]")
			v元素.click()
		self.ma模式 == aa模式
	def f切换框架(self, a框架):
		if self.m当前框架 == a框架:
			return
		self.m连接.switch_to.default_content()
		if a框架:
			e = self.m连接.find_element(By.XPATH, a框架)
			self.m连接.switch_to.frame(e)
		self.m当前框架 = a框架
	def f查找(self, a找):
		if self.mi登录:
			self.f切换框架(C设备.c主体框架)
		return 设备.I设备.f查找(self, a找)
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式(self)