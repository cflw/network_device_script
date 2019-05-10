from ..命令行接口 import 接口 as 南向接口
from ..命令行接口 import 端口安全 as 南向端口安全
#端口安全
class C端口安全(南向端口安全.I接口配置):
	def __init__(self, a, a接口):
		南向端口安全.I接口配置.__init__(self, a, a接口)
	@南向接口.A接口自动展开
	def fs开关(self, a开关):
		if a开关:
			self.f执行当前模式命令("port-security enable")
		else:
			self.f执行当前模式命令("undo port-security enable")
	@南向接口.A接口自动展开
	def fs数量(self, a数量):
		v命令 = "port-security max-mac-num " + int(a数量)
		self.f执行当前模式命令(v命令)
	@南向接口.A接口自动展开
	def fs动作(self, a动作):
		v命令 = "port-security protect-action " + C端口安全.f生成动作(a动作)
		self.f执行当前模式命令(v命令)
	@staticmethod
	def f生成动作(a动作):
		v类型 = type(a动作)
		if v类型 == str:
			return a动作
		elif v类型 == int:
			return ("shutdown", "restrict", "protect")[a动作]
		elif v类型 == bool:
			if a动作:
				return "restrict"
			else:
				return "shutdown"
		return "restrict"
