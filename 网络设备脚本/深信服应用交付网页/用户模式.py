import time
from ..基础接口 import 用户模式
from ..基础接口 import 异常
class C用户模式ad70(用户模式.I用户模式):
	"""适用于: ad 7.0.3"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示ad70(self.m设备)
	def f登录(self, a用户名, a密码):
		#输入
		w用户名 = self.m设备.f查找("//*[@id=\"user\"]")
		w用户名.f输入(a用户名)
		w密码 = self.m设备.f查找("//*[@id=\"password\"]")
		w密码.f输入(a密码)
		#登录
		w登录 = self.m设备.f查找("//*[@id=\"button\"]")
		w消息 = self.m设备.f查找("//*[@id=\"error_msg\"]")
		w登录.f点击()
		time.sleep(1)
		if not self.m设备.f查找_直到("//*[@id=\"id_top\"]", a超时 = 1):
			# 提示：请输入密码！
			# 提示：用户名或密码错误 (还有4次机会)
			v消息 = w消息.fg文本()
			if "用户名或密码错误" in v消息:
				raise 异常.X登录("用户名密码错误")
		time.sleep(1)
class C用户模式ad705(用户模式.I用户模式):
	"""适用于: ad 7.0.8"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示ad705(self.m设备)
	def f登录(self, a用户名, a密码):
		#输入
		w用户名 = self.m设备.f查找("//input[@name=\"username\"]")
		w用户名.f输入(a用户名)
		w密码 = self.m设备.f查找("//input[@name=\"password\"]")
		w密码.f输入(a密码)
		w协议 = self.m设备.f查找("//input[@name=\"checkbox\"]")
		w协议.f选中()
		#登录
		w登录 = self.m设备.f查找("//button[@class=\"uedc-ppkg-login_product-submit\"]")
		w消息 = self.m设备.f查找("//div[@class=\"uedc-ppkg-login_product-tip\"]")
		w登录.f点击()
		if not self.m设备.f查找_直到("//div[@id=\"top_nav\"]", a超时 = 5):
			# 请输入合法的用户名
			# 请输入合法的密码
			# 身份验证-用户名或密码错误(剩余重试[4]次)
			v消息 = w消息.fg文本()
			if "用户名或密码错误" in v消息:
				raise 异常.X登录("用户名密码错误")
		time.sleep(1)
		self.m设备.f解析登录后地址()