from ..基础接口 import 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 接口 as 南向接口
from ..华为命令行 import 实用
from ..华为命令行 import 接口 as 旧接口
from ..华为命令行.常量 import *
class C接口视图(旧接口.C接口视图):
	"""适用于: 华为ne40e(v8.180)"""
	@南向接口.A接口自动展开
	def fs开关(self, a操作):
		"""命令: [undo] shutdown
		不能关闭的口: loopback, """
		if self.m接口.m类型 == 北向接口.E类型.e环回:
			return
		v命令 = 实用.f生成开关命令(a操作)
		self.f执行当前模式命令(v命令)
