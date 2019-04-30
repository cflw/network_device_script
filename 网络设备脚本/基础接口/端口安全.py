import enum
class E端口安全动作(enum.IntEnum):
	e丢弃包 = 12
	e丢弃并警告 = 11
	e关闭端口 = 0
	e暂时关闭端口 = 1
class I端口安全(I模式):
	def __init__(self, a):
		I模式.__init__(self, a)
	def fs开关(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	def f模式_接口(self, a接口):
		raise NotImplementedError()
	def f应用到接口(self, a接口):
		raise NotImplementedError()
	def fs自动恢复时间(self, a时间):
		raise NotImplementedError()
	def fs地址老化时间(self, a时间):
		raise NotImplementedError()
class I端口安全接口(I接口配置模式基础):
	def __init__(self, a, a接口):
		I接口配置模式基础.__init__(self, a, a接口)
	def fs开关(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs地址(self, a地址, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs最大地址数(self, a数量, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs自动恢复时间(self, a时间, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs地址老化时间(self, a时间, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs端口安全动作(self, a动作, a操作 = E操作.e设置):
		raise NotImplementedError()
