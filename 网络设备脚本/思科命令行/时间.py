class C时间(设备.C同级模式, 设备.I时间):
	def __init__(self, a):
		设备.I时间.__init__(self, a)
	def fs日期时间(self, a):
		v时间 = 设备.I时间.f解析日期时间(a)
		v时间文本 = time.strftime("%H:%M:%S %b %d %Y", v时间)
		v命令 = "clock set " + v时间文本
		self.m设备.f执行用户命令(v命令)
	def fs时区(self, *a):
		v时区 = 设备.I时间.f解析时区(a)
		v总秒 = v时区.utcoffset(None).total_seconds()
		if v总秒 < 0:
			v符号 = "-"
			v总秒 = -v总秒
		else:
			v符号 = "+"
		v时分秒 = 时间.C时间计算.f总秒拆成时分秒(v总秒)
		v命令 = "clock timezone %s %s%s " % (v时区.tzname(), v符号, v时分秒[0])
		if v时分秒[1] != 0:
			v命令 += str(v时分秒[1])
		self.f切换到当前模式()
		self.m设备.f执行命令(v命令)