class I服务器配置:
	def fs开关(self, a操作):
		raise NotImplementedError()
	def fs层数(self, a层数, a操作):
		raise NotImplementedError()
	def fs版本(self, a版本, a操作):
		raise NotImplementedError()
	def fs源地址(self, a地址, a操作):
		raise NotImplementedError()
	def fs发送广播(self, a操作):
		raise NotImplementedError()
class I客户端配置:
	def f模式_远端(self, a地址, a端, a操作):
		"""指定服务器"""
		raise NotImplementedError()
	def fs开关(self, a操作):
		raise NotImplementedError()
	def fs接收广播(self, a操作):
		raise NotImplementedError()
	def f显示_同步信息(self):
		raise NotImplementedError()
class I远端配置:
	def fg地址(self):
		raise NotImplementedError()
	def fs版本(self, a版本, a操作):
		raise NotImplementedError()
	def fs优先(self, a操作):
		raise NotImplementedError()
	def fs认证(self, a钥匙, a操作):
		raise NotImplementedError()
	def fs源(self, a源, a操作):
		raise NotImplementedError()