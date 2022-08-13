import enum
class E类型(enum.IntEnum):
	e二层 = enum.auto()
	e三层 = enum.auto()
	e虚拟 = enum.auto()
class I区域显示:
	def fg名称(self):
		"""当前区域名称"""
		raise NotImplementedError()
	def fg接口(self):
		"""该区域有哪些接口"""
		raise NotImplementedError()
class I区域配置:	#表示一个接口区域
	def fs类型(self, a类型, a操作):
		"""当前区域类型"""
		raise NotImplementedError()
	def fs接口(self, a接口, a操作):
		"""区域包含哪些接口"""
		raise NotImplementedError()