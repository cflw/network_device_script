import cflw代码库py.cflw字符串 as 字符串
def f解析中央处理器利用率(a文本: str):
	"""display cpu-usage
	适用于: 华三s6900(v7.1.070)"""
	v数字s = 字符串.f提取字符串之间(a文本, "seconds", "% in last 1 minute")
	return int(v数字s)
def f解析内存利用率(a文本: str):
	"""display memory
	适用于: 华三s6900(v7.1.070)"""
	v行s = 字符串.f提取包含行(a文本, "Mem:")
	v分割 = v行s.split()
	return float(v分割[2]) / float(v分割[1])