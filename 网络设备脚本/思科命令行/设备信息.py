class C版本信息(设备.I版本信息):
	def __init__(self, a):
		self.m字符串 = str(a)
	def fg版本s(self):
		return 字符串.f提取字符串之间(self.m字符串, "Version ", "\n", a包含开始 = True)
	def fg版本号(self):
		raise NotImplementedError()
	def fg编译日期(self):
		v字符串 = 字符串.f提取字符串之间(self.m字符串, "Compiled ", " by")
		v时间 = time.strptime(v字符串, "%a %d-%b-%y %H:%M")
		return v时间
	def fg运行时间(self):
		v字符串 = 字符串.f提取字符串之间(self.m字符串, "uptime is", "\n")
		v周 = 字符串.f提取字符串之间(v字符串, " ", " week", a反向查找 = True)
		v日 = 字符串.f提取字符串之间(v字符串, " ", " day", a反向查找 = True)
		v时 = 字符串.f提取字符串之间(v字符串, " ", " hour", a反向查找 = True)
		v分 = 字符串.f提取字符串之间(v字符串, " ", " minute", a反向查找 = True)
		return datetime.timedelta(weeks = int("0" + v周), days = int("0" + v日), hours = int("0" + v时), minutes = int("0" + v分))
	def fg开机日期(self):
		v字符串 = 字符串.f提取字符串之间(self.m字符串, "System restarted at ", "\n")
		if v字符串:	#找到时间,提取时间
			#14:22:27 beijing Sun Aug 21 2016
			v空格0 = v字符串.find(" ")
			v空格1 = v字符串.find(" ", v空格0 + 1)
			v字符串 = v字符串[:v空格0] + v字符串[v空格1:]
			v时间 = time.strptime(v字符串, "%H:%M:%S %a %b %d %Y")
			return v时间
		else:	#找不到时间,从本机时间减运行时间
			v运行时间 = self.fg运行时间()
			return time.localtime(time.time() - v运行时间.total_seconds())
	def fg序列号(self):
		return 字符串.f提取字符串之间(self.m字符串, "Processor board ID ", "\n")
	def fg版权(self):
		return 字符串.f提取字符串之间(self.m字符串, "Copyright ", "\n", a包含开始 = True)
	def fg物理地址(self):
		v地址 = 字符串.f提取字符串之间(self.m字符串, "Base ethernet MAC Address       : ", "\n")
		if v地址:
			return 地址.S物理地址.fc字符串(v地址)
		else:
			return None
