from . import 模式
from ..基础接口 import 用户模式
class I用户模式(模式.I模式, 用户模式.I用户模式):
	c模式名 = "用户模式"
	def __init__(self, a):
		模式.I模式.__init__(self, a)
	#模式
	def fg进入命令(self):	#用户模式不需要进入命令
		return ""
	def fg提交命令(self):	#用户模式不需要提交命令
		return ""