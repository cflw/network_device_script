import enum
import cflw代码库py.cflw字符串 as 字符串
#===============================================================================
# 字段
#===============================================================================
class E字段(enum.IntEnum):
	c本端 = 0x10000000
	c对端 = 0x20000000
	#字符串
	e名称 = 0x0001
	e本端名称 = c本端 + e名称
	e对端名称 = c对端 + e名称
	e描述 = 0x0002
	e本端描述 = c本端 + e描述
	e对端描述 = c对端 + e描述
	#地址
	c地址 = 0x40000000
	e物理地址 = c地址 + 0x0010
	e本端物理地址 = c本端 + e物理地址
	e对端物理地址 = c对端 + e物理地址
	e网络地址4 = c地址 + 0x0011
	e本端网络地址4 = c本端 + e网络地址4
	e对端网络地址4 = c对端 + e网络地址4
	e网络地址6 = c地址 + 0x0012
	e本端网络地址6 = c本端 + e网络地址6
	e对端网络地址6 = c对端 + e网络地址6
	#路由
	e网络号 = c地址 + 0x0020
	e路由器号 = c地址 + 0x0021
	e本端路由器号 = c本端 + e路由器号
	e对端路由器号 = c对端 + e路由器号
	e自治系统号 = 0x0022
	e本端自治系统号 = c本端 + e自治系统号
	e对端自治系统号 = c对端 + e自治系统号
	#接口
	c接口 = 0x80000000
	e接口 = c接口 + 0x0030
	e本端接口 = c本端 + e接口
	e对端接口 = c对端 + e接口
	#时间
	c时间 = 0x01000000
def fi本端(a字段):
	return bool(a字段 & E字段.c本端)
def fi对端(a字段):
	return bool(a字段 & E字段.c对端)
def fi无端(a字段):
	"""判断一个字段是否既不是本端也不是对端"""
	return (not fi本端(a字段)) and (not fi对端(a字段))
#===============================================================================
# 记录
#===============================================================================
class C记录:
	"""一条记录"""
	def __init__(self):
		self.m字典 = {}
	def __len__(self):
		return len(self.m字典)
	def __bool__(self):
		return bool(self.m字典)
	def __str__(self):
		v字符串 = ""
		for k, v in self.m字典.items():
			if v字符串:
				v字符串 += ", "
			else:
				v字符串 = "{"
			v键 = 字符串.f提取字符串之间(str(k), "e", None)
			v值 = str(v)
			v字符串 += f"{v键}: {v值}"
		v字符串 += "}"
		return v字符串
	def __repr__(self):
		return repr(self.m字典)
	def __setitem__(self, k, v):
		if not k in E字段:
			raise ValueError("键必需是 E字段 值")
		if fi无端(k):
			raise ValueError("键必需包含本端或对端信息")
		self.m字典[k] = v
	def __getitem__(self, k):
		if not k in E字段:
			raise ValueError("键必需是 E字段 值")
		if fi无端(k):
			v本端 = E字段.c本端 + k
			vi本端 = v本端 in self.m字典
			v对端 = E字段.c对端 + k
			vi对端 = v对端 in self.m字典
			if vi本端 and vi对端:
				raise RuntimeError("键不包含端信息, 且字典中同时存在两端, 无法选择其中一端")
			if vi对端:
				return self.m字典[v对端]
			if vi本端:
				return self.m字典[v本端]
			return None
		if k in self.m字典:
			return self.m字典[k]
		else:
			return None
	def __delitem__(self, k):
		del self.m字典[k]
	def f清空(self):
		self.m字典.clear()
