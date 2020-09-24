import cflw代码库py.cflw字符串 as 字符串
def f解析中央处理器利用率(a文本):
	"""show system resources"""
	#CPU states  :   3.24% user,   0.12% kernel,   96.62% idle
	v文本 = 字符串.f提取字符串之间(a文本, "CPU states  :", "\n")
	v空闲s = 字符串.f提取字符串之间(v文本, "kernel,", "%")
	return 1 - float(v空闲s) * 0.01
def f解析内存利用率(a文本):
	"""show system resources"""
	#Memory usage:   8236356K total,   3631152K used,   4605204K free
	v文本 = 字符串.f提取字符串之间(a文本, "Memory usage:", "\n")
	v总共s = 字符串.f提取字符串之间(v文本, None, "K")
	v使用s = 字符串.f提取字符串之间(v文本, "total,", "K")
	return int(v使用s) / int(v总共s)