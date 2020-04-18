from . import 设备
class I模式:
	def __init__(self, a):
		if isinstance(a, 设备.I设备):	#设备
			self.m设备 = a
		elif isinstance(a, I模式):
			self.m设备 = a.m设备