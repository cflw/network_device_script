class X设备(RuntimeError):
	"所有设备异常的基类"
	def __init__(self, a消息):
		self.m消息 = str(a消息)
	def __str__(self):
		return self.m消息
class X命令(X设备):
	"无法解析的命令"
	def __init__(self, a):
		X设备.__init__(self, a)
class X执行(X设备):
	"无法正确执行的命令"
	def __init__(self, a):
		X设备.__init__(self, a)
class X模式(X设备):
	"在错误的模式执行命令"
	def __init__(self, a):
		if hasattr(a, c模式名):
			X设备.__init__(self, "无法在%s执行命令" % (a.c模式名,))
		elif type(a) == str:
			X设备.__init__(self, a)
		else:
			X设备.__init__(self, "无法执行命令")
class X输出(X设备):
	"无法解析设备输出信息"
	def __init__(self, a):
		X设备.__init__(self, a)
class X操作(X设备):
	"操作无效, 设备不支持的操作也用这个"
	def __init__(self, a操作, a消息 = ""):
		X设备.__init__(self, "操作 %s 无效: %s" % (a操作, a消息))
		self.m操作 = a操作
class X接口格式(X设备):
	"""设备不支持接口格式,需要展开"""
	def __init__(self, a接口):
		X设备.__init__(self, "不支持接口格式 %s" % (a接口,))
class X登录(X设备):
	"""登录失败"""
	def __init__(self, a):
		X设备.__init__(self, a)
class X连接(X设备):
	"""连接失败"""
	def __init__(self, a):
		X设备.__init__(self, a)