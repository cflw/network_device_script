import time
import cflw代码库py.cflw字符串 as 字符串
from ..命令行接口 import 用户模式
from ..命令行接口 import 命令
from . import 基本表信息
from .常量 import *
class C用户模式m6000(用户模式.I用户模式):
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	#模式
	def f事件_进入模式(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车(-1, 5)
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置m6000(self)
	#显示
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_时间(self):
		v命令 = "show clock"
		v输出 = self.m设备.f执行显示命令(v命令)	#16:20:09 beijing Tue Mar 12 2019
		#解析
		v空格位置 = 字符串.f全部找(v输出, " ")
		v行结束 = v输出.find("\n")
		if v行结束 > 0:	#如果有换行符,截取到行结束
			v输出 = v输出[0 : v空格位置[0]] + v输出[v空格位置[1] : v行结束]
		else:	#如果没有换行符,截取到字符串结束
			v输出 = v输出[0 : v空格位置[0]] + v输出[v空格位置[1]:]	#09:09:36 Thu Sep 29 2016
		v时间 = time.strptime(v输出, "%H:%M:%S %a %b %d %Y")
		return v时间
	#显示具体
	def f显示_接口表(self):
		v命令 = "show interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C接口表(v输出)
	def f显示_网络接口表4(self):
		v命令 = "show ip interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C网络接口表4(v输出)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		time.sleep(1)
		v输出 = self.m设备.f输出()
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(a用户名)
		if "Password:" in v输出:
			self.m设备.f执行命令(a密码)
	def f提升权限(self, a密码 = c提权密码, a级别 = None):
		v命令 = 命令.C命令("enable")
		if a级别:
			v命令 += a级别
		elif a密码 == c提权密码:	#使用默认的提权密码时,级别固定18
			v命令 += 18
		self.f执行当前模式命令(v命令)
		self.m设备.f执行命令(a密码)
