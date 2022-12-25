import time
from ..基础接口 import 用户模式
from ..基础接口 import 异常
from ..网页接口 import 图片
class C用户模式af8035(用户模式.I用户模式):
	"""适用于:v8.0.35~"""	
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置af8035(self.m设备)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示af8035(self.m设备)
	def f登录(self, a用户名: str, a密码: str):
		w用户名 = self.m设备.f查找("/html/body/div[4]/div[3]/table/tbody/tr/td/div[2]/form/div[1]/div[1]/div/input")
		w用户名.f输入(a用户名)
		w密码 = self.m设备.f查找("/html/body/div[4]/div[3]/table/tbody/tr/td/div[2]/form/div[1]/div[2]/div/input")
		w密码.f输入(a密码)
		w验证码 = self.m设备.f查找("/html/body/div[4]/div[3]/table/tbody/tr/td/div[2]/form/div[1]/div[3]/div/input")
		w消息 = self.m设备.f查找("/html/body/div[4]/div[3]/table/tbody/tr/td/div[2]/div")
		w登录 = self.m设备.f查找("/html/body/div[4]/div[3]/table/tbody/tr/td/div[2]/form/button")
		for i in range(5):
			# 输入验证码并点击登录按钮
			v验证码 = 图片.f手动输入验证码(w验证码, 4)
			if v验证码:
				w登录.f点击()
				time.sleep(2)
			else:
				raise RuntimeError("请输入验证码")
			if not "login.php" in self.m设备.fg地址():
				time.sleep(4)	#等待首页加载
				break	#已经离开登录页,跳出循环
			#还在登录页,检查消息
			if w标头 := self.m设备.f查找_直到("//*[@id=\"header\"]", a超时 = 1):	# 提示：正在登录，请稍后
				break
			v消息 = w消息.fg文本()
			if "验证码输入不正确" in v消息:	# 提示：验证码输入不正确，请重新输入
				continue
			elif "用户名或密码不正确" in v消息:	# 提示：用户名或密码不正确!您还剩下9次尝试机会!
				raise 异常.X登录("用户名密码错误")
			break	#没报错,结束循环
		else:
			raise 异常.X登录("登录失败次数过多")
		# 结束
		self.m设备.f查找_直到('/html/body/div[1]/div[2]/span[1]')	#检查导航栏首页按钮
		time.sleep(2)
