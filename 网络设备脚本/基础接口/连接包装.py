class I连接包装:
	"一台设备连接到其它设备时使用"
	def __init__(self, a模式):
		self.m连接 = a模式.m设备.m连接
	def f读_最新(self):
		return self.m连接.f读_最新()
	def f读_最近(self, a数量):
		return self.m连接.f读_最近(a数量)
	def f读_直到(self, a文本 = "", a时间 = 5):
		return self.m连接.f读_直到(a文本, a时间)
	def f写(self, a文本):
		self.m连接.f写(a文本)
	def fs编码(self, a编码):
		self.m连接.fs编码(a编码)
