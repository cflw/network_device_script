import cflw代码库py.cflw字符串 as 字符串
def f解析中央处理器利用率(a文本):
	"""show processes cpu history"""
	v利用率s = 字符串.f提取字符串之间(a文本, "one minute:", "%")
	return float(v利用率s) * 0.01
def f解析内存利用率(a文本):
	"""show memory summary total"""
	v利用率s = 字符串.f提取字符串之间(a文本, "Memory utilization:", "%")
	return float(v利用率s) * 0.01