class I接口配置模式:	#常见的接口配置
	#模式
	def f模式_虚拟局域网(self):
		raise NotImplementedError()
	def f模式_端口安全(self):
		raise NotImplementedError()
	def f模式_生成树(self):
		raise NotImplementedError()
	def f模式_路由信息协议(self, a进程号, a版本):
		raise NotImplementedError()
	def f模式_开放最短路径优先(self, a进程号, a版本):
		raise NotImplementedError()
	def f模式_增强内部网关路由协议(self, a版本):
		raise NotImplementedError()
	def f模式_中间系统到中间系统(self, a版本):
		raise NotImplementedError()
	#接口
	def fs开关(self, a操作):	#可以填True/False,也可以填 E操作 值
		raise NotImplementedError()
	def fs描述(self, a描述, a操作):
		raise NotImplementedError()
	#以太网
	def fs速率(self, a速率, a操作):
		raise NotImplementedError()
	def fs双工模式(self, a全双工, a操作):
		raise NotImplementedError()
	#三层
	def fs网络地址4(self, a地址, a操作):
		raise NotImplementedError()
	def fe网络地址4(self):
		"返回这个接口拥有的所有地址"
		raise NotImplementedError()
	def fs网络地址6(self, a地址, a操作):
		raise NotImplementedError()
	def fe网络地址6(self):
		raise NotImplementedError()
	#串行
	def fs时钟频率(self, a频率, a操作):
		raise NotImplementedError()
	#流量控制
	def fs访问控制列表(self, a访问控制列表, a方向, a操作):
		raise NotImplementedError()
	def fs服务质量(self, a, a方向, a操作):
		raise NotImplementedError()
