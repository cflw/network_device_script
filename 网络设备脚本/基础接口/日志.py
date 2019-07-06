import enum
class E严重级别(enum.IntEnum):
	e紧急 = 0
	e警报 = 1
	e关键 = 2
	e错误 = 3
	e警告 = 4
	e通知 = 5
	e信息 = 6
	e调试 = 7
class I日志配置:
	"""全局日志配置"""
	c模式名 = "日志配置模式"
	#显示
	def f显示_日志(self, a数量, a升序):
		"""显示日志内容"""
		raise NotImplementedError()
	#操作
	def fs开关(self, a操作):
		"""全局日志开关,开启后设备才会收集日志"""
		raise NotImplementedError()
	def fs缓冲大小(self, a字节, a操作):
		"""设备最多可记录的日志字节数"""
		raise NotImplementedError()
	def fs服务器开关(self, a操作):
		raise NotImplementedError()
	def fs服务器地址(self, a地址, a操作):
		raise NotImplementedError()
	def fs服务器严重级别(self, a级别, a操作):
		raise NotImplementedError()