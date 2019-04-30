from ..基础接口 import 路由信息协议
from . import 模式
from . import 接口配置
class I路由信息协议(模式.I模式, 路由信息协议.I路由信息协议):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
class I路由信息协议接口(接口配置.I接口配置模式基础, 路由信息协议.I路由信息协议接口):
	def __init__(self, a, a接口):
		接口配置.I接口配置模式基础.__init__(self, a, a接口)
