class I设备显示:
	#系统信息
	def f显示_版本(self):
		raise NotImplementedError()
	def f显示_设备名(self):
		"返回字符串"
		raise NotImplementedError()
	def f显示_系统版本(self):
		"返回 S版本 对象"
		raise NotImplementedError()
	#系统状态
	def f显示_运行时间(self):
		"从开机到现在所经过的时间, 返回datetime.timedelta对象"
		raise NotImplementedError()
	def f显示_开机日期(self):
		"返回time.struct_time对象"
		raise NotImplementedError()
	def f显示_中央处理器利用率(self):
		raise NotImplementedError()
	def f显示_内存利用率(self):
		"返回数字"
		raise NotImplementedError()
	#硬件信息
	def f显示_序列号(self):
		"返回字符串"
		raise NotImplementedError()
	def f显示_出厂日期(self):
		"返回time.struct_time对象"
		raise NotImplementedError()
	def f显示_资产(self):
		"""返回表"""
		raise NotImplementedError()
	#硬件状态
	def f显示_温度(self):
		"""返回表"""
		raise NotImplementedError()
	def f显示_风扇(self):
		"""返回表"""
		raise NotImplementedError()
	def f显示_电源(self):
		"""返回表"""
		raise NotImplementedError()
class I设备配置:
	def fs设备名(self, a名称):
		raise NotImplementedError()