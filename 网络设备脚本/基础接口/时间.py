import time
import datetime
import cflw代码库py.cflw时间 as 时间
def f解析日期时间(a):
	"""转换成time.struct_time"""
	if isinstance(a, time.struct_time):
		return a
	elif isinstance(a, datetime.datetime):
		return a.timetuple()
	else:
		raise TypeError("无法解析的类型")
def f解析时区(a):
	"""把datetime.tzinfo对象原封不动返回
	把"时区名±时:分"解析成datetime.timezone对象"""
	if isinstance(a, datetime.tzinfo):
		return a
	elif isinstance(a, 时间.S时区):
		return a.ft标准库时区()
	elif type(a) == str:
		v符号位置 = max(a.find("+"), a.find("-"))
		if v符号位置 < 0:
			raise ValueError("格式错误, 找不到正负号")
		elif v符号位置:	#v符号位置 > 0
			v时区名 = a[: v符号位置].strip()
		else:	#v符号位置 == 0
			v时区名 = None
		v冒号位置 = a.find(":", v符号位置)
		if v冒号位置 < 0:
			v时 = int(a[v符号位置+1 :])
			v分 = 0
		else:
			v时 = int(a[v符号位置+1 : v冒号位置])
			v分 = int(a[v冒号位置+1 :])
		return datetime.timezone(datetime.timedelta(hours = v时, minutes = v分), v时区名)
	else:
		raise TypeError("无法解析的类型")
def f拆分时区(a时区):
	"""把datetime.tzinfo转换成(时区名: str, 正号: bool, 时: int, 分: int)"""
	v总秒 = a时区.utcoffset(None).total_seconds()
	if v总秒 < 0:
		v符号 = False
		v总秒 = -v总秒
	else:
		v符号 = True
	v时分秒 = 时间.f总秒拆成时分秒(v总秒)
	return a时区.tzname(None), v符号, v时分秒[0], v时分秒[1]
def f解析并拆分时区(a时区):
	v时区 = f解析时间(a时区)
	return f拆分时区(v时区)
class I时间显示:
	def f显示_时间(self):
		"返回 time.struct_time 对象"
		raise NotImplementedError()
	def f显示_时区(self):
		"返回 datetime.timezone 对象"
		raise NotImplementedError()
class I时间配置:
	c模式名 = "时间配置模式"
	def fs为系统时间(self):
		"""把设备时间时区设置为当前系统的时间时区"""
		v时区 = 时间.S时区.fc系统时区()
		self.fs时区(v时区)
		self.fs日期时间(time.localtime())
	def fs日期时间(self, a日期时间):
		raise NotImplementedError()
	def fs时区(self, a时区):
		"""支持的类型: datetime.timezone
		支持的字符串格式: "时区名±时:分" """
		raise NotImplementedError()