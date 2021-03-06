from ..基础接口 import 异常
from ..命令行接口 import 命令
from ..华三命令行 import 设备 as 旧设备
from . import 用户模式
ca错误文本与异常类 = [
	("% Unrecognized command found at '^' position.", 异常.X命令),	#命令无法解析，符号“^”指示位置出错
	("% Incomplete command found at '^' position.", 异常.X命令),	#符号“^”指示位置的参数输入不完整
	("% Ambiguous command found at '^' position.", 异常.X命令),	#符号“^”指示位置的关键字不明确，存在二义性
	("% Too many parameters found at '^' position.", 异常.X命令),	#符号“^”指示位置的参数输入太多
	("% Wrong parameter found at '^' position.", 异常.X命令),	#在符号“^”指示位置的参数错误
]
class C设备v7(旧设备.C设备):
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图v7(self)