"""提供命令行显示相关的工具"""
import cflw代码库py.cflw字符串 as 字符串
#===============================================================================
# 管道
#===============================================================================
def F单节选(a查找: str):
	def f(a文本: str)->str:
		v切片 = f找单节选(a文本, a查找)
		if v切片 == None:
			return ""
		return a文本[v切片]
	return f
def f找单节选(a文本: str, a查找: str, a开始位置: int = 0):
	v行切片 = 字符串.f找包含行(a文本, a查找, a开始位置)
	if v行切片 == None:
		return None
	v开始位置 = v行切片.start
	v结束位置 = v行切片.stop
	v开始缩进 = 字符串.f取行缩进(a文本[v行切片])
	while True:
		v行切片 = 字符串.f找下一行切片(a文本, v行切片.start)
		if v行切片 == None:
			break
		v缩进 = 字符串.f取行缩进(a文本[v行切片])
		if v缩进 <= v开始缩进:
			break
		v结束位置 = v行切片.stop
	return slice(v开始位置, v结束位置)
def F多节选(a查找: str):
	def f(a文本: str)->str:
		v文本 = ""
		v位置 = 0
		while True:
			v切片 = f找单节选(a文本, a查找, v位置)
			if v切片 == None:
				break
			if v文本:
				v文本 += "\n"	#每节之间没有换行符,补一个
			v文本 += a文本[v切片]
			v位置 = v切片.stop
		return v文本
	return f
def F开始行(a查找: str):
	def f(a文本: str)->str:
		v位置 = a文本.find(a查找)
		if v位置 == -1:
			return ""
		v位置 = 字符串.f找行开始(a文本, v位置)
		return a文本[v位置:]
	return f
def F结束行(a查找: str):
	def f(a文本: str)->str:
		v位置 = a文本.find(a查找)
		if v位置 == -1:
			return ""
		v位置 = 字符串.f找行结束(a文本, v位置)
		return a文本[:v位置]
	return f
def F包含行(a查找: str):
	def f(a文本: str)->str:
		v文本 = ""
		v位置 = 0
		while True:
			v切片 = 字符串.f找包含行(a文本, a查找, v位置)
			if v切片 == None:
				break
			if v文本:
				v文本 += "\n"	#补换行符
			v文本 += a文本[v切片]
			v位置 = v切片.stop
		return v文本
	return f
#===============================================================================
# 显示表格
#===============================================================================
def F显示并解析(a命令, af解析):
	def f显示并解析(self):
		v输出 = self.m设备.f执行显示命令(a命令)
		v表 = af解析(v输出)
		return v表
	return f显示并解析