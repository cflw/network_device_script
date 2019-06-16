from ..基础接口 import 链路层发现协议
from . import 模式
from . import 接口
class I进程配置(模式.I模式, 链路层发现协议.I进程配置):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
class I接口配置(接口.I接口配置基础, 链路层发现协议.I接口配置):
	def __init__(self, a, a接口):
		接口.I接口配置基础.__init__(self, a, a接口)