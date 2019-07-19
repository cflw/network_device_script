import time
import cflw代码库py.cflw字符串 as 字符串
from ..命令行接口 import 用户模式
class C用户模式(用户模式.I用户模式):
	def __init__(self, a设备):
		用户模式.I用户模式.__init__(self, a设备)
		self.m版本信息 = None
		self.m版本信息时间 = 0
	def f事件_进入模式(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车(-1, 5)
	def f模式_全局配置(self):
		from . import 全局配置 as 全局配置
		self.f切换到当前模式()
		return 全局配置.C全局配置(self)
	#显示
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_时间(self):
		v命令 = "show clock"
		v输出 = self.m设备.f执行显示命令(v命令)
		from . import 时间
		return 时间.f解析时间(v输出)
	def f显示_设备版本(self):
		return self.fg版本信息()
	#连接
	def f连接_网络终端(self, a地址, **a参数):
		from . import 连接 as 连接包装
		return 连接包装.C网络终端(self, a地址, **a参数)
	#操作
	def f登录(self, a用户名 = "", a密码 = ""):
		time.sleep(0.5)
		v输出 = self.m设备.f输出()[-100:]
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(a用户名)
		if "Password:" in v输出:
			self.m设备.f执行命令(a密码)
		self.f切换到当前模式()
		time.sleep(0.5)
	def f提升权限(self, a密码 = ""):
		v输出 = self.m设备.f执行命令("enable")
		while "Password" in v输出:
			v输出 = self.m设备.f执行命令(a密码)
		if "Error" in v输出:
			raise 异常.X执行(v输出)
	def f保存配置(self):
		self.f执行当前模式命令("write")
	def f清除配置(self):
		self.f执行当前模式命令("erase startup-config")
		self.m设备.f执行命令("y")
	def f重新启动(self):
		v输出 = self.f执行当前模式命令("reload")
		#System configuration has been modified. Save? [yes/no]:
		if "Save?" in v输出:
			v输出 = self.m设备.f执行命令("n")
		#Proceed with reload? [confirm]
		if "reload?" in v输出:
			self.m设备.f输入_回车()
	def fs终端监视(self, a开关):
		if a开关:
			self.m设备.f执行用户命令("terminal monitor")
		#↓某些未知情况不能关闭终端监视，先注释
		# v命令 = 命令.C命令("terminal monitor")
		# v命令.f前置否定(a开关, c不)
		# self.m设备.f执行用户命令(v命令)
	#内部
	def fg版本信息(self):
		if time.time() - self.m版本信息时间 >= 60:	#超过1分种则刷新
			v输出 = self.m设备.f执行显示命令("show version")
			self.m版本信息 = C版本信息(v输出)
		return self.m版本信息
