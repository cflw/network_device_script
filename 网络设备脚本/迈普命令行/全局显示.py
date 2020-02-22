from ..命令行接口 import 全局显示
from . import 基本表信息
class C全局显示(全局显示.I全局显示):
	#显示
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_时间(self):
		v命令 = "show clock"
		v输出 = self.m设备.f执行显示命令(v命令)	#beijing(UTC+08:00) THU APR 04 11:11:12 2019
		#解析
		v空格位置 = 字符串.f全部找(v输出, " ")
		v行结束 = v输出.find("\n", v空格位置[0])
		if v行结束 > 0:	#如果有换行符,截取到行结束
			v输出 = v输出[v空格位置[0]+1 : v行结束]
		else:	#如果没有换行符,截取到字符串结束
			v输出 = v输出[v空格位置[0]+1:]	#THU APR 04 11:11:12 2019
		v时间 = time.strptime(v输出, "%a %b %d %H:%M:%S %Y")
		return v时间
	def f显示_设备名(self):
		v命令 = "show running-config | include hostname"
		v输出 = self.m设备.f执行显示命令(v命令)
		v位置 = v输出.find("hostname")
		v行结束 = v输出.find("\n", v位置)
		return v输出[v位置 + 9 : v行结束]
	#显示具体
	def f显示_接口表(self):
		v命令 = "show interface switchport"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C交换接口表(v输出)
	def f显示_网络接口表4(self):
		v命令 = "show ip interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C网络接口表4(v输出)
