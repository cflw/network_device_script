from ..基础接口 import 异常
from ..命令行接口 import 命令
from ..华为命令行 import 设备 as 旧设备
ca错误文本与异常类 = [
	("Error: Unrecognized command found at '^' position.", 异常.X命令),
	("Error: Wrong parameter found at '^' position.", 异常.X命令),
	("Error: Ambiguous command found at '^' position.", 异常.X命令),
]
class C设备(旧设备.C设备):
	"""适用于: 华为ne40e(v8.180)"""
	def __init__(self, a连接, a型号, a版本):
		旧设备.C设备.__init__(self, a连接, a型号, a版本)
	def f提交(self):
		self.f执行命令("commit")
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图(self)
	#其它
	f检测命令异常 = 命令.F检测命令异常(ca错误文本与异常类)
