import cflw代码库py.cflw工具 as 工具
def f解析版本字符串(s: str):
	"""支持的格式:\n
	Version 7.1.070, Release 7734P05\n
	v7.1.070 r7734p05\n
	其他 工具.S版本号 支持的格式"""
	v = s.lower()
	if "version" in v:
		v逗号位置 = v.find(",")
		va大版本 = v[8 : v逗号位置].split(".")
		v补丁位置 = v.find("p", v逗号位置)
		if v补丁位置 > 0:
			v发行号 = v[v逗号位置+10 : v补丁位置]
			v补丁号 = v[v补丁位置+1 :]
			return 工具.S版本号.fc分段(*va大版本, v发行号, v补丁号)
		else:
			v发行号 = v[v逗号位置+10 :]
			return 工具.S版本号.fc分段(*va大版本, v发行号)
	elif "v" in v:
		v空格位置 = v.find(" ")
		va大版本 = v[1: v空格位置].split(".")
		v补丁位置 = v.find("p", v空格位置)
		if v补丁位置 > 0:
			v发行号 = v[v空格位置+2 : v补丁位置]
			v补丁号 = v[v补丁位置+1 :]
			return 工具.S版本号.fc分段(*va大版本, v发行号, v补丁号)
		else:
			v发行号 = v[v空格位置+2 :]
			return 工具.S版本号.fc分段(*va大版本, v发行号)
	else:
		return 工具.S版本号.fc字符串(v)