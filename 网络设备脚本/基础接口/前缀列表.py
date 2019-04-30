class S前缀列表规则:
	def __init__(self, **a):
		self.m序号 = None
		self.m允许 = True
		self.m网络号 = None
		self.m最小长度 = None
		self.m最大长度 = None
		self.f更新(**a)
	def f更新(self, **a):
		for k, v in S前缀列表规则.ca更新函数.items():
			if k in a:
				v(self, a[k])
	def fs序号(self, a):
		self.m序号 = a
	def fs允许(self, a):
		self.m允许 = a
	def fs网络号(self, a):
		self.m网络号 = a
	def fs最小长度(self, a):
		self.m最小长度 = a
	def fs最大长度(self, a):
		self.m最大长度 = a
	ca更新函数 = {
		"a允许": fs允许,
		"a网络号": fs网络号,
		"a最小长度": fs最小长度,
		"a最大长度": fs最大长度,
	}
class I前缀列表(I模式):
	c模式名 = "前缀列表配置模式"
	def __init__(self, a):
		I模式.__init__(self, a)
	def fs规则(self, a序号 = None, a规则 = None, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fe规则(self):
		raise NotImplementedError()
	def f应用到(self, a):
		raise NotImplementedError()
