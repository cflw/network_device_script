class I设备显示:
	#系统信息
	def f显示_版本(self):
		raise NotImplementedError()
	def f显示_设备名(self)->str:
		raise NotImplementedError()
	def f显示_系统版本(self):
		"返回 S版本 对象"
		raise NotImplementedError()
	#系统状态
	def f显示_运行时间(self)->"datetime.timedelta":
		"从开机到现在所经过的时间"
		raise NotImplementedError()
	def f显示_开机日期(self)->"time.struct_time":
		"具体什么时候开机"
		raise NotImplementedError()
	def f显示_中央处理器利用率(self)->float:
		raise NotImplementedError()
	def f显示_内存利用率(self)->float:
		raise NotImplementedError()
	#硬件信息
	def f显示_序列号(self)->str:
		raise NotImplementedError()
	def f显示_出厂日期(self)->"time.struct_time":
		raise NotImplementedError()
	def f显示_资产(self)->"pandas.DataFrame":
		raise NotImplementedError()
	#硬件状态
	def f显示_温度(self)->"pandas.DataFrame":
		raise NotImplementedError()
	def f显示_风扇(self)->"pandas.DataFrame":
		raise NotImplementedError()
	def f显示_电源(self)->"pandas.DataFrame":
		raise NotImplementedError()
class I设备配置:
	def fs设备名(self, a名称: str):
		raise NotImplementedError()