import enum
class E网络安全性工作模式(enum.IntEnum):
	e默认 = 0
	e传输 = 1
	e隧道 = 2
class I网络密钥交换策略(I模式):
	def __init__(self, a):
		I模式.__init__(self, a)
	def fs散列方式(self, a):
		raise NotImplementedError()
	def fs加密方式(self, a):
		raise NotImplementedError()
	def fs认证方式(self, a):
		raise NotImplementedError()
class I网络密钥交换密钥链(I模式):	#思科ike keyring,华三ike keychain
	def __init__(self, a):
		I模式.__init__(self, a)	
	def fs预共享密钥(self, a地址, a密码, a操作 = E操作.e设置):
		raise NotImplementedError()
class I网络安全性变更集(I模式):	#ipsec transform set
	def __init__(self, a):
		I模式.__init__(self, a)
	def fs加密方式(self, a):
		raise NotImplementedError()
	def fs认证方式(self, a):
		raise NotImplementedError()
	def fs变更方式(self, a):
		raise NotImplementedError()
	def fs压缩方式(self, a):
		raise NotImplementedError()
	def fs工作模式(self, a):
		raise NotImplementedError()
class I网络安全性配置(I模式):
	def __init__(self, a):
		I模式.__init__(self, a)
