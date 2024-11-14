import time
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
class C版本信息:	#需重写
	"""show version
	适用于: 思科c7200"""
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
def f解析中央处理器利用率(a文本):
	"""show processes cpu 该命令还会显示进程信息"""
	#CPU utilization for five seconds: 34%/0%; one minute: 35%; five minutes: 34%
	v数字s = 字符串.f提取字符串之间(a文本, "five minutes:", "%")
	return float(v数字s) * 0.01
def f解析内存利用率(a文本):
	"""show processes memory 该命令还会显示进程信息"""
	#Processor Pool Total:  371078328 Used:   54758420 Free:  316319908
	v总共s = a文本[21:33]
	v使用s = a文本[38:50]
	return int(v使用s) / int(v总共s)
class C进程表:	#需重写
	"""show processes"""
	c进程标识 = 0
	QTy = 4	#?
	PC = 16	#?
	c运行时间 = 19	#单位:毫秒
	Invoked = 35	#?
	uSecs = 45	#?
	Stacks_TTY = 54	#?
	c进程名称 = 65
	c标题行 = " PID QTy       PC Runtime (ms)    Invoked   uSecs    Stacks TTY Process"
class C进程处理器表:	#需重写
	"""show processes cpu"""
	c进程标识 = 0
	c运行时间 =	4	#单位:毫秒
	Invoked = 21	#?
	uSecs = 34	#?
	c五秒 = 42
	c一分钟 = 49
	c五分钟 = 56
	TTY = 61	#?
	c进程名称 = 66
	c标题行 = " PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process "
class C进程内存表:	#需重写
	"""show processes memory"""
	c标题行 = " PID TTY  Allocated      Freed    Holding    Getbufs    Retbufs Process"
def f计算生产日期(a序列号: str):
	"""根据序列号计算生产日期, 精确到周
	序列号格式: LLLYYWWXXXX, 其中的YYWW是生产的年,周"""
	v年s = a序列号[3:5]
	v周s = a序列号[5:7]
	v相对年 = int(v年s)	#1=1997年,以此类推
	v周 = int(v周s)
	v日 = (v周 - 1) * 7
	return time.strptime(f"{1996 + v相对年} {v日}", "%Y %j")