import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 异常
from ..命令行接口 import 用户模式 as 用户模式
class C用户视图(用户模式.I用户模式):
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	def f事件_进入模式(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车()
		v输出 = self.m设备.f输出()
		if "commit" in v输出:
			self.m设备.f执行命令("n")
	#模式
	def f模式_全局配置(self):
		from . import 全局配置 as 全局配置
		return 全局配置.C系统视图(self)
	#显示
	def f显示_版本(self):
		v命令 = "display version"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return v输出
	def f显示_启动配置(self):
		v命令 = "display saved-configuration"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return C配置内容(v输出)
	def f显示_当前配置(self):
		v命令 = "display current-configuration"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return C配置内容(v输出)
	def f显示_时间(self):
		v命令 = "display clock"
		v输出 = self.m设备.f执行显示命令(v命令)
		#2019-04-12 10:58:39-08:00	#←新版本的时间后面会带时区，去掉
		#Friday
		#Time Zone(China-Standard-Time) : UTC-08:00
		v输出 = v输出.split("\n")[0]
		v时区位置 = 字符串.f连续找最后(v输出, ":", "-")
		if v时区位置 > 0:
			v输出 = v输出[:v时区位置]
		v时间 = time.strptime(v输出, "%Y-%m-%d %H:%M:%S")
		return v时间
	def f显示_设备名称(self):
		v命令 = "display current-configuration | include sysname"
		v输出 = self.m设备.f执行显示命令(v命令)
		return C输出分析.f从配置取设备名称(v输出)
	def f显示_运行时间(self):
		"从开机到现在所经过的时间"
		raise NotImplementedError()
	def f显示_开机日期(self):
		raise NotImplementedError()
	def f显示_序列号(self):
		raise NotImplementedError()
	def f显示_出厂日期(self):
		raise NotImplementedError()
	#显示 基本表信息
	def f显示_物理地址表(self):
		v命令 = "display mac-address"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C物理地址表(v输出)
	def f显示_地址解析表(self):
		v命令 = "display arp"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C地址解析表(v输出)
	def f显示_接口表(self):
		v命令 = "display interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C接口表(v输出)
	def f显示_网络接口表4(self):
		v命令 = "display ip interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C网络接口表4(v输出)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		time.sleep(1)
		self.m设备.f输入_回车()
		v输出 = self.m设备.f输出()
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(a用户名)
		if "Password:" in v输出:
			v输出 = self.m设备.f执行命令(a密码)
		if "Error:" in v输出:
			raise 异常.X登录(v输出)
		self.f切换到当前模式()
	def f提升权限(self, a密码, a级别 = 15):
		self.m设备.f执行命令("super")
		self.m设备.f执行命令(a密码)
	def fs终端监视(self, a开关):
		v命令 = 命令.C命令("terminal monitor")
		v命令.f前置否定(a开关, c不)
		self.f执行当前模式命令(v命令)
	#连接
	def f连接_网络终端(self, a地址, **a参数):
		from . import 连接
		return 连接.C网络终端(self, a地址, **a参数)
