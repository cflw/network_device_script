from ..基础接口 import 全局显示
from ..命令行接口 import 模式
class C全局显示v7(全局显示.I全局显示, 模式.I模式, 模式.C同级模式):
	def __init__(self, a):
		模式.I模式.__init__(self, a)