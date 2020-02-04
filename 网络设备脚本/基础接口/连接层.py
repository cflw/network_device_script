"""在不导入其他模块的情况下处理各种连接"""
def fi连接特性(a连接, a位):
	if hasattr(a连接, "c连接特性"):
		return a连接.c连接特性 & a位
	return False
def fi命令行(a连接):
	if fi连接特性(a连接, 0x0001):
		return True
	return False
def fi网页(a连接):
	if fi连接特性(a连接, 0x0002):
		return True
	if "selenium" in str(a连接.__class__):	#selenium
		return True
	return False
