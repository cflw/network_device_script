from ..基础接口 import 生成树
from . import 模式
from . import 接口配置
class I多生成树(模式.I模式, 生成树.I多生成树):
	c模式名 = "多生成树配置模式"
	def __init__(self, a):
		模式.I模式.__init__(self, a)
class I生成树接口(接口配置.I接口配置模式基础, 生成树.I生成树接口):
	c模式名 = "生成树接口配置模式"
	def __init__(self, a, a接口):
		接口配置.I接口配置模式基础.__init__(self, a, a接口)
