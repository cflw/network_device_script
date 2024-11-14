c密钥长度 = 1024
class I安全外壳配置:
	"SSH"
	c模式名 = "安全外壳配置模式"
	def fs开关(self, a操作):
		raise NotImplementedError()
	def f生成密钥(self, a长度, a操作):
		raise NotImplementedError()
	def fs端口号(self, a端口号, a操作):
		raise NotImplementedError()
	def fs源接口(self, a接口, a操作):
		raise NotImplementedError()
	def fs版本(self, a版本, a操作):
		raise NotImplementedError()
	def fs连接数(self, a数量, a操作):
		raise NotImplementedError()
	def fs认证重试(self, a次数, a操作):
		raise NotImplementedError()
	def fs认证超时(self, a时间, a操作):
		raise NotImplementedError()
	def fs访问列表(self, a访问列表, a操作):
		raise NotImplementedError()
class I安全外壳显示:
	def fg开关(self):
		"""ssh服务是否开启"""
		raise NotImplementedError()
	def fg端口号(self):
		"""返回ssh端口号"""
		raise NotImplementedError()
	def fg版本(self):
		"""返回ssh版本号(1或2)"""
		raise NotImplementedError()
	def fg认证重试(self):
		"""返回ssh认证次数"""
		raise NotImplementedError()
	def fg认证超时(self):
		"""返回ssh认证时间. 单位:秒"""
		raise NotImplementedError()
	def fg访问列表(self):	#返回的值应能直接传入 fs访问列表、f模式_访问控制列表
		"""返回ssh绑定的acl"""
		raise NotImplementedError()
