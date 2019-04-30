class I路由信息协议(I模式):
	def f显示_路由表(self):
		raise NotImplementedError()
	def f显示_数据库(self):
		raise NotImplementedError()
	def fs通告网络(self, a网络号, a操作):
		raise NotImplementedError()
	def fs通告接口(self, a接口, a操作):
		raise NotImplementedError()
class I路由信息协议接口:
	def fs通告接口(self, a接口, a操作):
		raise NotImplementedError()
	def fs认证(self, a认证方式, a密码, a操作):
		raise NotImplementedError()
