import weakref
from ..基础接口 import 设备
from ..基础接口 import 操作
class I模式:
	"命令行模式接口"
	def __init__(self, a):
		if isinstance(a, 设备.I设备):	#a是设备
			self.m设备 = weakref.proxy(a)
			self.m模式栈 = (weakref.ref(self), )
		elif isinstance(a, I模式):	#a是父模式
			self.m设备 = a.m设备
			self.m模式栈 = a.m模式栈[:-1] + (a, weakref.ref(self))
		else:
			raise TypeError("创建模式对象的第一个参数类型必需是 I设备 或 I模式")
	def __eq__(self, a):	#通用的模式相等比较
		if isinstance(a, I模式):
			if self is a:
				return True
			elif self.fg进入命令 != a.fg进入命令:
				return False
			else:
				return self.fg进入命令() == a.fg进入命令()
		else:
			return False
	def fi当前模式(self):
		return self == self.m设备.fg当前模式()
	def f切换到当前模式(self):
		if not self.fi当前模式():
			va模式 = [(r() if type(r) == weakref.ref else r) for r in self.m模式栈]
			self.m设备.f切换模式(va模式)
	def f执行当前模式命令(self, a命令):
		self.f切换到当前模式()
		self.m设备.f执行命令(a命令)
	def f显示_当前模式配置(self):	#当前模式的配置,在用户模式显示所有配置
		self.f切换到当前模式()
		return self.m设备.f显示_当前模式配置()
	def fg模式参数(self):
		"表示要进入该模式所使用的参数"
		raise NotImplementedError()
	def fg进入命令(self):
		"要进入该模式所使用的完整命令"
		raise NotImplementedError()
	def fg退出命令(self):
		"退出到上一级模式所使用的完整命令"
		raise NotImplementedError()
	def fg上级模式(self):
		if len(self.m模式栈) > 1:
			return self.m模式栈[-2]
		else:
			return None
	def fg删除命令(self):
		"删除当前模式所使用的完整命令,需要在上级模式执行"
		raise NotImplementedError()
	def fg提交命令(self):
		"使配置生效所使用的完整命令"
		raise NotImplementedError()
	def f事件_进入模式(self):
		"进入当前模式[后]做的事情"
		pass
	def f事件_退出模式(self):
		"退出当前模式[前]做的事情"
		self.m设备.f自动提交(操作.E自动提交.e退出当前模式时)
class C同级模式(I模式):	#和上一层模式是同一级别的，不需要进入命令也不需要退出命令
	def fg模式参数(self):
		return ""
	def fg进入命令(self):
		return ""
	def fg退出命令(self):
		return ""
