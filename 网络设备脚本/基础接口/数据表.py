import enum
import pandas	#pandas
import cflw代码库py.cflw字符串 as 字符串
#===============================================================================
# 字段
#===============================================================================
class E字段(enum.Enum):
	c本端 = 0x10000000
	c对端 = 0x20000000
	#信息
	c信息 = 0
	e名称 = c信息 + 1
	e本端名称 = c本端 + e名称
	e对端名称 = c对端 + e名称
	e描述 = c信息 + 2
	e本端描述 = c本端 + e描述
	e对端描述 = c对端 + e描述
	e索引 = c信息 + 3
	e本端索引 = c本端 + e索引
	e对端索引 = c对端 + e索引
	#地址
	c地址 = 0x40000000
	e物理地址 = c地址 + 0x0010
	e本端物理地址 = c本端 + e物理地址
	e对端物理地址 = c对端 + e物理地址
	e物理地址类型 = c地址 + 0x0013
	# e本端物理地址类型 = c本端 + e物理地址类型	#应该不存在本端物理地址类型
	e对端物理地址类型 = c对端 + e物理地址类型
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
	e路由类型 = c本端 + 0x0022
	e路由器号 = c地址 + 0x0025
	e本端路由器号 = c本端 + e路由器号
	e对端路由器号 = c对端 + e路由器号
	e自治系统号 = 0x0026
	e本端自治系统号 = c本端 + e自治系统号
	e对端自治系统号 = c对端 + e自治系统号
	#接口
	c接口 = 0x80000000	#分类
	c接口1 = c接口 + 0x0030	#字段
	e本端接口 = c本端 + c接口1
	e对端接口 = c对端 + c接口1
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
	e本端速率 = c本端 + e速率	#单位: bps
	c链路类型 = c接口 + 0x0036	#access/trunk
	e本端链路类型 = c本端 + c链路类型
	c对端链路类型 = c对端 + c链路类型
	#状态
	c状态 = 0x0040
	c协议状态 = c状态 + 1
	e本端协议状态 = c本端 + c协议状态
	e对端协议状态 = c对端 + c协议状态
	c链路状态 = c状态 + 2
	e本端链路状态 = c本端 + c链路状态
	e对端链路状态 = c对端 + c链路状态
	c管理状态 = c状态 + 3
	e本端管理状态 = c本端 + c管理状态
	e对端管理状态 = c对端 + c管理状态
	#交换
	c生成树 = 0x0050
	c生成树实例 = c生成树 + 1
	e本端生成树实例 = c本端 + c生成树实例
	c生成树角色 = c生成树 + 2
	e本端生成树角色 = c本端 + c生成树角色
	c生成树状态 = c生成树 + 3
	e本端生成树状态 = c本端 + c生成树状态
	#时间
	c时间 = 0x01000000
	c运行时间 = c时间 + 1	#uptime, 正计时
	e本端运行时间 = c本端 + c运行时间
	c建立时间 = c时间 + 2	#setup time, 正计时
	e本端建立时间 = c本端 + c建立时间
	c保持时间 = c时间 + 3	#hold time, 正计时
	e本端保持时间 = c本端 + c保持时间
	c寿命 = c时间 + 4	#age, 倒计时
	e本端寿命 = c本端 + c寿命
def fi本端(a字段):
	return bool(a字段 & E字段.c本端)
def fi对端(a字段):
	return bool(a字段 & E字段.c对端)
def fi无端(a字段):
	"""判断一个字段是否既不是本端也不是对端"""
	return (not fi本端(a字段)) and (not fi对端(a字段))
def f字段字符串(a字段: E字段):
	return 字符串.f提取字符串之间(str(a字段), "e", None)
def fe字段字符串(aa字段):
	return (f字段字符串(v字段) for v字段 in aa字段)
#===============================================================================
# 数据表通用函数
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
#有效行
def F有效行长度(a长度: int):
	"""达到一定长度才算有效行"""
	def f行长度(a行: str):
		return len(a行) >= a长度
	return f行长度
#结束判断
def fi空行(a行: str):
	return not bool(a行)
#字段管线
def F关键字(a文本: str):
	def f关键字(a行):
		return a文本 in a行
	return f关键字
#===============================================================================
# 表格管线
#===============================================================================
def Fe一行记录数据表(af初始处理, af有效行, aa每行处理, af结束 = fi空行):	#废弃
	@staticmethod
	def fe行(a文本):
		v文本 = af初始处理(a文本)
		for v行 in v文本.split("\n"):
			if not afi有效行(v行):
				continue
			if afi结束(v行):
				break
			v字典 = dict([vf行处理(v行) for vf行处理 in aa每行处理])
			yield v字典
	return fe行
class I解析表格管线:
	"""控制点:	\n
	f初始处理(self, a文本: str)->str	\r
	fe分割行(self, a文本: str)->str		\r
	fi有效行(self, a行: str)->bool	\r
	fi结束(self, a行: str)->bool	\r
	ma列, 包含(字段, 取列函数, 解析函数), 通过 f添加字段 添加"""
	class C列:
		def __init__(self, a字段, af取列, af解析):
			self.m字段 = a字段
			self.mf取列 = af取列
			self.mf解析 = af解析
		def f解析(self, a行):
			v文本 = self.mf取列(a行).strip()
			v值 = self.mf解析(v文本)
			return self.m字段, v值
	def __init__(self):
		self.ma列 = []
	def __call__(self, a文本):
		return self.f解析(a文本)
	def f解析(self, a文本):
		v文本 = self.f初始处理(a文本)
		def fe行():
			for v行 in self.fe分割行(v文本):
				if not self.fi有效行(v行):
					continue
				if self.fi结束(v行):
					break
				yield dict([v列.f解析(v行) for v列 in self.ma列])
		v数据帧 = pandas.DataFrame(fe行())
		return v数据帧
	def f添加字段(self, a字段, af取列, af解析):
		self.ma列.append(I解析表格管线.C列(a字段, af取列, af解析))
	def f初始处理(self, a文本):
		"""先把文本做初步处理"""
		return a文本	#默认不处理
	def fe分割行(self, a文本: str):
		"""如何分割文本,返回生成器"""
		return a文本.split("\n")	#默认按换行符分割
	def fi有效行(self, a行):
		"""判断行是否有效,有效行加入解析"""
		return True	#全部有效
	def fi结束(self, a行):
		"""判断是否到达表格结尾,结束解析"""
		return False	#不中途结束
#===============================================================================
# 列表管线
#===============================================================================
class I解析列表管线:
	"""控制点:	\n
	f初始处理()	\r
	fi新记录()	\r
	fi结束()	\r
	ma字段, 包含(字段, 判断函数, 取值函数, 解析函数)
	"""
	class C字段:
		def __init__(self, a字段, af判断, af取值, af解析):
			self.m字段 = a字段
			self.mf判断 = af判断
			self.mf取值 = af取值
			self.mf解析 = af解析
		def f判断(self, a行):
			return self.mf判断(a行)
		def f解析(self, a行):
			v文本 = self.mf取值(a行).strip()
			v值 = self.mf解析(v文本)
			return self.m字段, v值
	def __init__(self):
		self.ma字段 = []
	def __call__(self, a文本):
		self.f解析(a文本)
	def f解析(self, a文本):
		v文本 = self.f初始处理(a文本)
		def fe记录():
			pass	#未完成
		v数据帧 = pandas.DataFrame(fe记录())
		return v数据帧
	def fi新记录(self, a行):
		return False
	def fi结束(self, a行):
		return False
#===============================================================================
# 记录
#===============================================================================
class C记录:	#废弃
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
