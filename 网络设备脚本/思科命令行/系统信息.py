import cflw代码库py.cflw字符串 as 字符串
def f解析中央处理器利用率(a文本):
	"""show processes cpu"""
	#CPU utilization for five seconds: 34%/0%; one minute: 35%; five minutes: 34%
	v数字s = 字符串.f提取字符串之间(a文本, "five minutes:", "%")
	return float(v数字s) * 0.01
def f解析内存利用率(a文本):
	"""show processes memory"""
	#Processor Pool Total:  371078328 Used:   54758420 Free:  316319908
	v总共s = a文本[21:33]
	v使用s = a文本[38:50]
	return int(v使用s) / int(v总共s)
class C进程表:
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
class C进程处理器表:
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
class C进程内存表:
	"""show processes memory"""
	c标题行 = " PID TTY  Allocated      Freed    Holding    Getbufs    Retbufs Process"