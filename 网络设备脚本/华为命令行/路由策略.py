from ..基础接口 import 操作
from ..基础接口 import 策略
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 路由映射
from . import 访问控制列表 as 访问列表
class C组(路由映射.I路由映射组, 模式.C同级模式):
	def __init__(self, a, a名称):
		路由映射.I路由映射组.__init__(self, a, a名称)
	def f模式_节点(self, a序号, a动作 = True, a操作 = 操作.E操作.e设置):
		return C节点(self, a序号, a动作)
@策略.A自动策略()
class C节点(路由映射.I路由映射节点):
	def __init__(self, a, a序号, a动作):
		路由映射.I路由映射节点.__init__(self, a, a序号, a动作)
	def fg进入命令(self):
		"""命令: route-policy 名称 动作 node 序号"""
		return f"route-policy {self.m名称} {访问列表.f生成允许(self.m动作)} node {self.m序号}"
	@策略.A匹配(策略.E类型.e访问列表)
	def f匹配_访问列表(self, a值, a操作 = 操作.E操作.e设置):
		"""命令: if-match acl 访问列表"""
		v命令 = f"if-match acl {a值}"
		self.f执行当前模式命令(v命令)
	@策略.A设置(策略.E类型.e下一跳4)
	def f设置_下一跳4(self, a值, a操作 = 操作.E操作.e设置):
		"""命令: apply ip-address next-hop 地址"""
		v命令 = f"apply ip-address next-hop {a值}"
		self.f执行当前模式命令(v命令)