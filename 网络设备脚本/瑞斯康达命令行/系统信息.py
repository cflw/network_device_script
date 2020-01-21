import cflw代码库py.cflw字符串 as 字符串
def f解析中央处理器利用率(a文本):
	v数字s = 字符串.f提取字符串之间(a文本, "Last 1 minute CPU utilization:", "%")
	return float(v数字s) * 0.01
def f解析内存利用率(a文本):
	v数字s = 字符串.f提取字符串之间(a文本, "memory utilization  :", "%")
	return float(v数字s) * 0.01
