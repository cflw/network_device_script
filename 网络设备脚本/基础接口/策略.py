import enum
class E类型(enum.Enum):
	e总是 = enum.auto()
	#协议
	e协议 = enum.auto()
	#数据结构
	e访问列表4 = enum.auto()
	e访问列表6 = enum.auto()
	e访问列表 = e访问列表4
	e前缀列表4 = enum.auto()
	e前缀列表6 = enum.auto()
	e前缀列表 = e前缀列表6
	#地址
	e源物理地址 = enum.auto()
	e目的物理地址 = enum.auto()
	e源网络地址4 = enum.auto()
	e源网络地址6 = enum.auto()
	e源网络地址 = e源网络地址4
	e目的网络地址4 = enum.auto()
	e目的网络地址6 = enum.auto()
	e目的网络地址 = e目的网络地址4
	#路由
	e下一跳4 = enum.auto()
	e下一跳6 = enum.auto()
	e默认下一跳4 = enum.auto()
	e默认下一跳6 = enum.auto()
	e出接口 = enum.auto()
	e默认出接口 = enum.auto()
	e度量值 = enum.auto()
	e区域类型 = enum.auto()	#ospf,isis
	e路由类型 = enum.auto()	#ospf,eigrp,isis
	#ip字段
	e优先级 = enum.auto()
class I匹配:
	def fs匹配(self, a类型, a值, a操作):
		raise NotImplementedError()
class I设置:
	def fs设置(self, a类型, a值, a操作):
		raise NotImplementedError()
def A匹配(a类型):
	def f装饰(af匹配):
		af匹配.m策略_匹配 = a类型
		return af匹配
	return f装饰
def A设置(a类型):
	def f装饰(af设置):
		af设置.m策略_设置 = a类型
		return af设置
	return f装饰
def A自动策略():
	def f装饰(a类):
		def f并入(aa字典, a成员, a属性名):
			if hasattr(v成员, a属性名):
				aa字典 |= {getattr(v成员, a属性名) : v成员}
				delattr(v成员, a属性名)
		#遍历成员
		va匹配 = {}
		va设置 = {}
		for v成员s in dir(a类):
			v成员 = getattr(a类, v成员s)
			f并入(va匹配, v成员, "m策略_匹配") or f并入(va设置, v成员, "m策略_设置")
		#赋值
		if va匹配:
			a类.ca匹配 = va匹配
			a类.fs匹配 = lambda self, a类型, a值, a操作 = True: self.ca匹配[a类型](self, a值, a操作)
		if va设置:
			a类.ca设置 = va设置
			a类.fs设置 = lambda self, a类型, a值, a操作 = True: self.ca设置[a类型](self, a值, a操作)
		return a类
	return f装饰