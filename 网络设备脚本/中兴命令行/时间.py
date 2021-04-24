import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 时间
from ..命令行接口 import 模式
class C时间显示m6000(时间.I时间显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
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
