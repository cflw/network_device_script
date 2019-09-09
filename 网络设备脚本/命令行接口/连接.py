from ..基础接口 import 连接
class I命令行连接(连接.I命令行连接):
	def __init__(self, a模式):
		连接.I命令行连接.__init__(self, a模式)
	def fg进入命令(self):
		raise NotImplementedError()
	def f连接(self):
		v命令 = self.fg进入命令()
		self.m模式.f执行当前模式命令(v命令)