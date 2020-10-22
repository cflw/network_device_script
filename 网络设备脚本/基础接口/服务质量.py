from . import 策略
class I流量分类(策略.I匹配):
	pass
class I流量行为(策略.I设置):
	def fs允许(self, a允许: bool):
		raise NotImplementedError()
class I助手:
	"""服务质量助手包含设备和策略名称,在设备中自动绑定类和行为,统一不同设备的操作"""
	def fg分类名称(self):
		raise NotImplementedError()
	def fg行为名称(self):
		raise NotImplementedError()
	def fg策略名称(self):
		raise NotImplementedError()
