import cflw代码库py.cflw字符串 as 字符串
#===============================================================================
# 内置类型
#===============================================================================
def f解析范围(a范围):
	v类型 = type(a范围)
	if v类型 == range:
		return a范围
	elif v类型 == int:
		return range(a范围, a范围 + 1)
	elif v类型 == str:
		return 字符串.ft范围(a范围)
	else:
		raise TypeError("无法解析的类型")