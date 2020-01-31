import time
from ..基础接口 import 用户模式
from ..网页接口 import 图片
class C用户模式(用户模式.I用户模式):
	"""适用于:v8.0.7~8.0.13"""	
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置(self.m设备)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示(self.m设备)
	def f登录(self, a用户名, a密码):
		w用户名 = self.m设备.f查找("//*[@id=\"user\"]")
		w用户名.f输入(a用户名)
		w密码 = self.m设备.f查找("//*[@id=\"password\"]")
		w密码.f输入(a密码)
		# w验证码图 = self.m设备.f查找("//*[@id=\"captcha_img\"]")
		# v验证码图 = 图片.f取元素图片(self.m设备, w验证码图)
		# w验证码.f输入(图片.f处理验证码(v验证码图))
		w验证码 = self.m设备.f查找("//*[@id=\"verify\"]")
		v验证码 = 图片.f手动输入验证码(w验证码, 4)
		if v验证码:
			w登录 = self.m设备.f查找("//*[@id=\"button\"]")
			w登录.f点击()
		else:
			raise RuntimeError("请输入验证码")
		self.m设备.f查找_直到('//*[@id="ext-gen100"]')
		time.sleep(1)
