#内部
from ..基础接口 import 全局配置
from . import 模式
#接口
class I全局配置模式(模式.I模式, 全局配置.I全局配置模式):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
