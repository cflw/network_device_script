class I中间系统到中间系统(I模式):
	c模式名 = "中间系统到中间系统配置模式"
	def __init__(self, a, a进程号):
		I模式.__init__(self, a)
	def f显示_路由表(self):
		raise NotImplementedError()
	def f显示_邻居(self):
		raise NotImplementedError()
	def fs通告接口(self, a接口, a操作 = E操作.e设置):
		raise NotImplementedError()
