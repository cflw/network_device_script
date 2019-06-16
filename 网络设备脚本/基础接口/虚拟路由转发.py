class S路由区分符:
	def __init__(self, a号, a数):
		self.m号 = int(a号)
		self.m数 = int(a数)
	def __str__(self):
		return f"{self.m号}:{self.m数}"
class I资源配置:
	c模式名 = "虚拟路由转发资源配置模式"
	def fs路由区分符(self, a路由区分符, a操作):
		raise NotImplementedError()
	def fs路由目标(self, a路由区分符, a方向, a操作):
		raise NotImplementedError()
class I接口配置:
	c模式名 = "虚拟路由转发接口配置模式"
	def fs虚拟路由转发(self, a名称, a保留地址, a操作):
		raise NotImplementedError()