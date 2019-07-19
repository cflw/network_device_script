class I接口配置:
	c模式名 = "热备份路由协议接口配置模式"
	def fs版本(self, a版本, a操作):
		raise NotImplementedError()
	def fs地址4(self, a地址, a操作):
		raise NotImplementedError()
	def fs抢占(self, a操作):
		raise NotImplementedError()
	def fs优先级(self, a优先级, a操作):
		raise NotImplementedError()
	def fs问候时间(self, a秒, a操作):
		raise NotImplementedError()
	def fs维持时间(self, a秒, a操作):
		raise NotImplementedError()
	def fs跟踪(self, a接口, a优先级, a操作):
		raise NotImplementedError()
	def fs认证(self, a密码, a操作):
		raise NotImplementedError()