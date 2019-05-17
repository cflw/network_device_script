from ..基础接口 import 网络终端
from . import 模式
class I网络终端配置(模式.I模式, 网络终端.I网络终端配置):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
