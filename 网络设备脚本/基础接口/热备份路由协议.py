class I冗余路由:
	c模式名 = "热备份路由协议配置模式"
	#显示
	def fg组号(self):
		raise NotImplementedError()
	#配置
	def fs版本(self, a版本, a操作):
		raise NotImplementedError()
	def fs网络地址4(self, a地址, a操作):
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