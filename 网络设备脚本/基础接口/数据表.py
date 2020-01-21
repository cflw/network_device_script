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
	e目标网络号 = c对端 + e网络号
	e下一跳 = c地址 + 0x0021
	e目标下一跳 = c对端 + e下一跳
	e路由协议 = c本端 + 0x0022
	e路由器号 = c地址 + 0x0025
	e本端路由器号 = c本端 + e路由器号
	e对端路由器号 = c对端 + e路由器号
	e自治系统号 = 0x0026
	e本端自治系统号 = c本端 + e自治系统号
	e对端自治系统号 = c对端 + e自治系统号
	#接口
	c接口 = 0x80000000
	e类型 = c接口 + 0x0030
	e本端接口 = c本端 + e类型
	e对端接口 = c对端 + e类型
	e虚拟局域网 = 0x0031
	e本端虚拟局域网 = c本端 + e虚拟局域网
	e对端虚拟局域网 = c对端 + e虚拟局域网
	e出接口 = c接口 + 0x0032
	e本端出接口 = c本端 + e出接口
	e入接口 = c接口 + 0x0033
	e本端入接口 = c本端 + e入接口
	e双工模式 = c接口 + 0x0034
	e本端双工模式 = c本端 + e双工模式
	e速率 = c接口 + 0x0035
	e本端速率 = c本端 + e速率
	#状态
	c状态 = 0x0040
	e本端状态 = c本端 + c状态
	e对端状态 = c对端 + c状态
	e协议状态 = 0x0041
	e本端协议状态 = c本端 + e协议状态
	e对端协议状态 = c对端 + e协议状态
	e链路状态 = 0x0042
	e本端链路状态 = c本端 + e链路状态
	e对端链路状态 = c对端 + e链路状态
	e管理状态 = 0x0043
	e本端管理状态 = c本端 + e管理状态
	e对端管理状态 = c对端 + e管理状态
	#交换
	c生成树 = 0x0050
	e生成树实例 = c生成树 + 0
	e本端生成树实例 = c本端 + e生成树实例
	e生成树角色 = c生成树 + 1
	e本端生成树角色 = c本端 + e生成树角色
	e生成树状态 = c生成树 + 2
	e本端生成树状态 = c本端 + e生成树状态
	#时间
	c时间 = 0x01000000
	c维持时间 = c时间 + 0x0060
	e本端维持时间 = c本端 + c维持时间
	
def fi本端(a字段):
	return bool(a字段 & E字段.c本端)
def fi对端(a字段):
	return bool(a字段 & E字段.c对端)
def fi无端(a字段):
	"""判断一个字段是否既不是本端也不是对端"""
	return (not fi本端(a字段)) and (not fi对端(a字段))
#===============================================================================
# 数据表
#===============================================================================
#初始处理
def F去标题行(*aa标题):
	def f去标题行(a文本: str):
		v位置 = 字符串.f连续找最后(a文本, *aa标题, "\n")
		return a文本[v位置 + 1 :]
	return f去标题行
#行处理
def F处理列(a字段, af取列, af解析):
	def f(a行: str):
		v文本 = af取列(a行).strip()
		v值 = af解析(v文本)
		return a字段, v值
	return f
#结束判断
def fi空行(a行: str):
	return not bool(a行)
#处理表
def Fe一行记录数据表(af初始处理, af有效行判断, aa每行处理, af结束判断 = fi空行):
	@staticmethod
	def fe(a文本):
		v文本 = af初始处理(a文本)
		for v行 in v文本.split("\n"):
			if not af有效行判断(v行):
				continue
			if af结束判断(v行):
				break
			v字典 = dict([vf行处理(v行) for vf行处理 in aa每行处理])
			yield C记录(v字典)
	return fe
#===============================================================================
# 记录
#===============================================================================
class C记录:
	"""一条记录"""
	def __init__(self, a字典 = {}):
		self.m字典 = {}
		for k, v in a字典.items():
			self.__setitem__(k, v)
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
			if type(v) == str:
				v值 = '"' + v + '"'
			else:
				v值 = str(v)
			v字符串 += f"{v键}: {v值}"
		v字符串 += "}"
		return v字符串
	def __repr__(self):
		return f"<记录: {repr(self.m字典)}>"
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
