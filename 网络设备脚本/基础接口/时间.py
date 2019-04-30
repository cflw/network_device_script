class I时间(I模式):
	c模式名 = "系统时间"
	def __init__(self, a):
		I模式.__init__(self, a)
	def f等于系统时间(self):
		"把设备时间设置为当前系统时间"
		v时区 = 时间.S时区.fc系统时区()
		self.fs时区(v时区)
		self.fs日期时间(time.localtime())
	def fs日期时间(self, a):
		raise NotImplementedError()
	def fs时区(self, *a):
		raise NotImplementedError()
	@staticmethod
	def f解析日期时间(a):
		if isinstance(a, time.struct_time):
			return a
		elif isinstance(a, datetime.datetime):
			return a.timetuple()
		else:
			raise TypeError()
	@staticmethod
	def f解析时区(a):
		"返回datetime.tzinfo对象"
		v长度 = len(a)
		if v长度 == 1:
			v0 = a[0]
			if isinstance(v0, datetime.tzinfo):
				return v0
			elif isinstance(v0, 时间.S时区):
				return v0.f转datetime点timezone()
		elif v长度 == 2:
			v0 = a[0]
			v1 = a[1]
			return datetime.timezone(时间.C字符串转时间差.f时间(v1), v0)
		else:
			raise TypeError()
