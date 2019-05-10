class S规则:
	def __init__(self, **a):
		self.m序号 = None
		self.m允许 = True
		self.m网络号 = None
		self.m最小长度 = None
		self.m最大长度 = None
		self.f更新(**a)
	def __str__(self):
		v = ""
		#序号
		if self.m序号 >= 0:
			v += "序号%d, " % (self.m序号,)
		#允许
		if self.m允许:
			v += "允许, "
		else:
			v += "拒绝, "
		#地址
		if self.m网络号:
			v += "网络号%s, " % (self.m网络号,)
		if self.m最小长度:
			v += "最小%s, " % (self.m最小长度,)
		if self.m最大长度:
			v += "最大%s, " % (self.m最大长度,)
		return v
	def f更新(self, **a):
		for k, v in S规则.ca更新函数.items():
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
class I列表配置:
	c模式名 = "前缀列表配置模式"
	def fs规则(self, a序号, a规则, a操作):
		raise NotImplementedError()
	def fe规则(self):
		raise NotImplementedError()
	def fg规则(self, a序号):
		raise NotImplementedError()
	def f应用到(self, a):
		raise NotImplementedError()
