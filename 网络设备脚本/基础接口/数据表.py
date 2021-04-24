import enum
import re
import copy
import pandas	#pandas
import cflw代码库py.cflw字符串 as 字符串
#===============================================================================
# 字段
#===============================================================================
class E字段(enum.Enum):
	c本端 = 0x10000000
	c对端 = 0x20000000
	#信息
	c信息 = 0x00000000
	e名称 = c信息 + 0x01
	e本端名称 = c本端 + e名称
	e对端名称 = c对端 + e名称
	e描述 = c信息 + 0x02
	e本端描述 = c本端 + e描述
	e对端描述 = c对端 + e描述
	e索引 = c信息 + 0x03
	e本端索引 = c本端 + e索引
	e对端索引 = c对端 + e索引
	c型号 = c信息 + 0x04
	e本端型号 = c本端 + c型号
	c序列号 = c信息 + 0x05
	e本端序列号 = c本端 + c序列号
	#硬件
	c硬件 = 0x00010000
	e本端单元 = c本端 + c硬件 + 0x00	#单元,插槽,槽位
	c电源 = c硬件 + 0x0100
	e本端输出功率 = c本端 + c电源 + 0x01	#功率单位:瓦
	e本端输入功率 = c本端 + c电源 + 0x02
	e本端额定功率 = c本端 + c电源 + 0x03
	e本端电源电流 = c本端 + c电源 + 0x04	#电流单位:安
	e本端电源电压 = c本端 + c电源 + 0x05	#电压单位:伏
	e本端电源状态 = c本端 + c电源 + 0x10
	e本端电源类型 = c本端 + c电源 + 0x11
	c风扇 = c硬件 + 0x0200
	e本端风扇 = c本端 + c风扇 + 0x01
	e本端风扇方向 = c本端 + c风扇 + 0x02
	e本端风扇状态 = c本端 + c风扇 + 0x03
	e本端风扇转速 = c本端 + c风扇 + 0x04
	c温度 = c硬件 + 0x0300
	e本端温度 = c本端 + c温度 + 0x01	#温度单位:摄氏度
	e本端传感器 = c本端 + c温度 + 0x02
	e本端温度状态 = c本端 + c温度 + 0x03
	e本端高温阈值 = c本端 + c温度 + 0x10
	e本端严重高温阈值 = c本端 + c温度 + 0x11
	e本端低温阈值 = c本端 + c温度 + 0x12
	#地址
	c地址 = 0x40000000
	c物理地址 = c地址 + 0x0010
	e本端物理地址 = c本端 + c物理地址
	e对端物理地址 = c对端 + c物理地址
	c物理地址类型 = c地址 + 0x0013
	# e本端物理地址类型 = c本端 + e物理地址类型	#应该不存在本端物理地址类型
	e对端物理地址类型 = c对端 + c物理地址类型
	c网络地址4 = c地址 + 0x0011
	e本端网络地址4 = c本端 + c网络地址4
	e对端网络地址4 = c对端 + c网络地址4
	c网络地址6 = c地址 + 0x0012
	e本端网络地址6 = c本端 + c网络地址6
	e对端网络地址6 = c对端 + c网络地址6
	c地址解析协议类型 = c地址 + 0x0013
	e本端地址解析协议类型 = c本端 + c地址解析协议类型
	#路由
	c网络号 = c地址 + 0x0020
	e目标网络号 = c对端 + c网络号
	c下一跳 = c地址 + 0x0021
	e目标下一跳 = c对端 + c下一跳
	c路由类型 = c地址 + 0x0022
	e目标路由类型 = c对端 + c路由类型
	c管理距离 = c地址 + 0x0023
	e目标管理距离 = c对端 + c管理距离
	c度量值 = c地址 + 0x0024
	e目标度量值 = c对端 + c度量值
	c路由器号 = c地址 + 0x0030
	e本端路由器号 = c本端 + c路由器号
	e对端路由器号 = c对端 + c路由器号
	c自治系统号 = c地址 + 0x0031
	e本端自治系统号 = c本端 + c自治系统号
	e对端自治系统号 = c对端 + c自治系统号
	c虚拟路由转发 = c地址 + 0x0032
	e本端虚拟路由转发 = c本端 + c虚拟路由转发
	#接口
	c接口 = 0x80000000	#分类
	c接口1 = c接口 + 0x0030	#字段
	e本端接口 = c本端 + c接口1
	e对端接口 = c对端 + c接口1
	c虚拟局域网 = c接口 + 0x0031
	e本端虚拟局域网 = c本端 + c虚拟局域网
	e对端虚拟局域网 = c对端 + c虚拟局域网
	c出接口 = c接口 + 0x0032
	e本端出接口 = c本端 + c出接口
	c入接口 = c接口 + 0x0033
	e本端入接口 = c本端 + c入接口
	c双工模式 = c接口 + 0x0034
	e本端双工模式 = c本端 + c双工模式
	c速率 = c接口 + 0x0035	#速率是一种物理速度
	e本端速率 = c本端 + c速率	#单位: bps
	c带宽 = c接口 + 0x0036	#带宽是一种逻辑速度
	e本端带宽 = c本端 + c带宽
	c最大传输单元 = c接口 + 0x0037
	e本端最大传输单元 = c本端 + c最大传输单元
	c链路类型 = c接口 + 0x0040	#access/trunk
	e本端链路类型 = c本端 + c链路类型
	e对端链路类型 = c对端 + c链路类型
	#接口数据
	c接口接收数据 = c接口 + 0x1000
	c接口发送数据 = c接口 + 0x2000
	#接口数据(接收)
	c每秒接收字节数 = c接口接收数据 + 1
	e本端每秒接收字节数 = c本端 + c每秒接收字节数
	c每秒接收包数 = c接口接收数据 + 2
	e本端每秒接收包数 = c本端 + c每秒接收包数
	c接收字节数 = c接口接收数据 + 3
	e本端接收字节数 = c本端 + c接收字节数
	c接收包数 = c接口接收数据 + 4
	e本端接收包数 = c本端 + c接收包数
	c接收错误数 = c接口接收数据 + 5
	e本端接收错误数 = c本端 + c接收错误数
	c接收利用率 = c接口接收数据 + 6
	e本端接收利用率 = c本端 + c接收利用率
	#接口数据(发送)
	c每秒发送字节数 = c接口发送数据 + 1
	e本端每秒发送字节数 = c本端 + c每秒发送字节数
	c每秒发送包数 = c接口发送数据 + 2
	e本端每秒发送包数 = c本端 + c每秒发送包数
	c发送字节数 = c接口发送数据 + 3
	e本端发送字节数 = c本端 + c发送字节数
	c发送包数 = c接口发送数据 + 4
	e本端发送包数 = c本端 + c发送包数
	c发送错误数 = c接口发送数据 + 5
	e本端发送错误数 = c本端 + c发送错误数
	c发送利用率 = c接口发送数据 + 6
	e本端发送利用率 = c本端 + c发送利用率
	#状态
	c状态 = 0x0050
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
	c生成树 = 0x0060
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
	c寿命 = c时间 + 4	#age, expire time, 倒计时
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
#有效行/记录
def F有效长度(a长度: int):
	"""达到一定长度才算有效"""
	def f行长度(a行: str):
		return len(a行) >= a长度
	return f行长度
def F有效行数(a数量: int):
	"""达到一定行数才算有效"""
	def f行数(a文本: str):
		return a文本.count("\n") >= a数量
	return f行数
#结束判断
def fi空行(a行: str):
	return not bool(a行)
#字段管线控制
def F下一记录(a找: str):
	def f下一记录(a文本1: str, a开始位置:int)->int:
		v下一行位置 = a文本1.find("\n", a开始位置) + 1
		if v下一行位置 > a开始位置:
			return a文本1.find(a找, v下一行位置)
		else:
			return -1
	return f下一记录
def f下一记录_直接结束(a文本: str, a开始位置: int)->int:
	return -1
def f下一记录_下一行(a文本: str, a开始位置: int)->int:
	v下一行位置 = a文本.find("\n", a开始位置) + 1
	if v下一行位置 > a开始位置:
		return v下一行位置
	else:
		return -1
#字段管线记录
def F列表字段(a字段: str, a结束: str = "\n", a分隔符 = ":"):
	"""针对"键: 值"的格式
	字段不用包含冒号"""
	v正则 = re.compile(f"\\s*({a字段})\\s*{a分隔符}\\s*(.*?)\\n")
	def f提取(a文本: str)->str:
		if v匹配 := v正则.search(a文本):
			return v匹配[2]
		else:
			return ""
	return f提取
def F正则字段(a正则, a索引):
	#正则
	v类型 = type(a正则)
	if v类型 == str:
		v正则 = re.compile(a正则)
	elif v类型 == re.Pattern:
		v正则 = a正则
	else:
		raise TypeError()
	#函数
	def f提取(a文本: str)->str:
		if v结果 := v正则.search(a文本):
			if type(a索引) in (list, tuple):	#多个
				return v结果.group(*a索引)
			else:	#一个
				return v结果.group(a索引)
		return ""
	return f提取
def F指定行列(af取行, af取列):	#取行可以用 字符串.F提取包含行, 取列可以用 数据表.C切割列.F切片
	def f提取(a文本: str)->str:
		return af取列(af取行(a文本))
	return f提取
#取列
class C切割列:	#相对于通用的 序列.C切片组 , 数据表.C切割列 增加了自动移除字符串头尾空白功能
	def __init__(self, *aa索引):
		if aa索引[0] == 0:
			self.ma索引 = aa索引
		else:
			self.ma索引 = (0,) + aa索引
		self.m长度 = len(self.ma索引)
	def __getitem__(self, k):
		return self.F切片(k)
	def fg切片(self, k):
		if self.m长度 > k + 1:
			return slice(self.ma索引[k], self.ma索引[k+1])
		elif self.m长度 == k + 1:
			return slice(self.ma索引[k], None)
		else:
			raise IndexError()
	def F切片(self, k):
		v切片 = self.fg切片(k)
		def f切片(a行: str):
			return a行[v切片].strip()
		return f切片
#===============================================================================
# 表格管线
#===============================================================================
class C列:
	def __init__(self, a字段, af取列, af解析):
		self.m字段 = a字段
		self.mf取列 = af取列
		self.mf解析 = af解析
	def f解析(self, a行: str):
		v列 = self.mf取列(a行)
		v值 = self.mf解析(v列)
		return v值
class C行:	#一行有多列
	def __init__(self):
		self.ma列 = []
	def f解析(self, a行: str):
		return dict([(v列.m字段, v列.f解析(a行)) for v列 in self.ma列])
	def f添加字段(self, a字段, af取列, af解析 = lambda x: x):
		self.ma列.append(C列(a字段, af取列, af解析))
class I解析表格管线:
	"""可以解析的格式为常见表格\n
	控制点:	\n
	f初始处理(self, a文本: str)->str	\r
	fe分割行(self, a文本: str)->str		\r
	fi有效行(self, a行: str)->bool	\r
	fi结束(self, a行: str)->bool	\r
	ma列, 包含(字段, 取列函数, 解析函数), 通过 f添加字段 添加"""
	def __init__(self):
		self.m行 = C行()
	def __call__(self, a文本):
		return self.f解析(a文本)
	def f解析(self, a文本):	#解析完整文本
		v文本 = self.f初始处理(a文本)
		v数据帧 = pandas.DataFrame(self.fe记录(v文本))
		return v数据帧
	def f添加字段(self, a字段, af取列, af解析):
		self.m行.f添加字段(a字段, af取列, af解析)
	def f初始处理(self, a文本):
		"""先把文本做初步处理"""
		return a文本	#默认不处理
	def fe记录(self, a文本: str)->dict:
		"""解析出记录"""
		for v行 in self.fe分割行(a文本):
			if self.fi结束(v行):
				break
			if not self.fi有效行(v行):
				continue
			yield self.m行.f解析(v行)
	def fe分割行(self, a文本: str):
		"""如何分割文本,返回生成器"""
		return a文本.split("\n")	#默认按换行符分割
	def fi有效行(self, a行):
		"""判断行是否有效,有效行加入解析"""
		return True	#全部有效
	def fi结束(self, a行):
		"""判断是否到达表格结尾,结束解析"""
		return False	#不中途结束
class I解析多行表格管线:
	"""一个记录可能跨多行,或者每行格式各不相同,需要手动定义行,手动解析行	\n
	控制点:	\n
	f解析行	\r
	f初始处理	\r
	fe分割行	\r
	fi有效行	\r
	fi结束	\r
	fi新记录
	"""
	def __init__(self):
		self.ma上次结果 = {}
		self.ma这次结果 = {}
	def __call__(self, a文本: str):
		return self.f解析(a文本)
	def f解析(self, a文本: str):
		v文本 = self.f初始处理(a文本)
		v数据帧 = pandas.DataFrame(self.fe记录(v文本))
		return v数据帧
	def f解析行(self, a行: str)->dict:	#解析一行,返回字典
		raise NotImplementedError()
	def f初始处理(self, a文本):
		return a文本	#默认不处理
	def fe记录(self, a文本: str)->dict:
		for v行 in self.fe分割行(a文本):
			if self.fi结束(v行):
				break
			if not self.fi有效行(v行):
				continue
			if self.fi新记录(v行):
				if self.ma这次结果:
					yield self.ma这次结果
				self.ma上次结果 = self.ma这次结果
				self.ma这次结果 = {}
			self.ma这次结果 |= self.f解析行(v行)
		#结束
		if self.ma这次结果:
			yield self.ma这次结果
			self.ma这次结果 = {}
	def fe分割行(self, a文本: str):
		return a文本.split("\n")	#默认按换行符分割
	def fi有效行(self, a行: str):
		return True	#全部有效
	def fi结束(self, a行: str):
		return False	#不中途结束
	def fi新记录(self, a行: str):
		return True	#每行都是新记录
	def F上次结果(self, a字段):
		"""用于 C字段 的 af取值 中"""
		def f上次结果(a行_):
			return self.ma上次结果[a字段]
		return f上次结果
	def f上次结果(self, a字段):
		return self.ma上次结果[a字段]
#===============================================================================
# 列表管线
#===============================================================================
class C字段:
	def __init__(self, a字段, af取值, af解析):
		self.m字段 = a字段
		self.mf取值 = af取值
		self.mf解析 = af解析
	def f解析(self, a记录: str):
		v文本 = self.mf取值(a记录).strip()
		if v文本:
			return self.mf解析(v文本)
		return None
class I解析列表管线:
	"""格式:一行一个字段的列表.参考powershell的列表格式
	控制点:	\n
	f初始处理()	\r
	fi新记录()	\r
	fi结束()	\r
	ma字段, 包含(字段, 判断函数, 取值函数, 解析函数)
	"""
	def __init__(self):
		self.ma字段 = []
		self.ma上次结果 = {}
		self.ma这次结果 = {}
	def __call__(self, a文本: str):
		return self.f解析(a文本)
	def f解析(self, a文本: str):
		v文本 = self.f初始处理(a文本)
		v数据帧 = pandas.DataFrame(self.fe记录(v文本))
		return v数据帧
	def f添加字段(self, a字段, af取值, af解析):
		self.ma字段.append(C字段(a字段, af取值, af解析))
	def f初始处理(self, a文本: str):
		"""先把文本做初步处理"""
		return a文本	#默认不处理
	def fe记录(self, a文本: str):
		v开始位置 = 0
		while v开始位置 >= 0:
			#提取记录文本
			v结束位置 = self.f下一记录(a文本, v开始位置)
			if v结束位置 > v开始位置:
				v记录s = a文本[v开始位置 : v结束位置]
			else:
				v记录s = a文本[v开始位置:]
			v开始位置 = v结束位置
			if not self.fi有效记录(v记录s):
				continue
			#解析字段
			for v字段 in self.ma字段:
				if (v值 := v字段.f解析(v记录s)) != None:
					self.ma这次结果[v字段.m字段] = v值
			#暂回
			if self.ma这次结果:
				yield self.ma这次结果
				self.ma上次结果 = self.ma这次结果
				self.ma这次结果 = {}
	def f下一记录(self, a文本: str, a开始位置: int)->int:
		"""计算下一记录的位置, 默认返回结束位置"""
		raise NotImplementedError()
	def fi有效记录(self, a记录: str):
		return True
	def fi结束(self, a行):
		return False
	def F上次结果(self, a字段):
		"""用于 C字段 的 af取值 中"""
		def f上次结果(a行_):
			return self.ma上次结果[a字段]
		return f上次结果
	def f上次结果(self, a字段):
		return self.ma上次结果[a字段]
class I解析表格列表管线:
	"""记录中包含表格,需要一个解析表格管线来解析记录中的表格"""
	def __init__(self):
		self.ma字段 = []
		self.ma上次结果 = {}	#列表结果
		self.ma这次结果 = {}	#列表结果
		self.mf解析表格 = None
	def __call__(self, a文本: str):
		return self.f解析(a文本)
	def f解析(self, a文本: str):
		v文本 = self.f初始处理(a文本)
		v数据帧 = pandas.DataFrame(self.fe记录(v文本))
		return v数据帧
	def f添加字段(self, a字段, af取值, af解析):
		self.ma字段.append(C字段(a字段, af取值, af解析))
	def f添加表格(self, af解析表格: I解析表格管线):
		self.mf解析表格 = af解析表格
	def f初始处理(self, a文本: str):
		"""先把文本做初步处理"""
		return a文本	#默认不处理
	def fe记录(self, a文本: str):
		v开始位置 = 0
		while v开始位置 >= 0:
			#提取记录文本
			v结束位置 = self.f下一记录(a文本, v开始位置)
			if v结束位置 > v开始位置:
				v记录s = a文本[v开始位置 : v结束位置]
			else:
				v记录s = a文本[v开始位置:]
			v开始位置 = v结束位置
			if not self.fi有效记录(v记录s):
				continue
			#解析字段
			for v字段 in self.ma字段:
				if (v值 := v字段.f解析(v记录s)) != None:
					self.ma这次结果[v字段.m字段] = v值
			#暂回
			if self.ma这次结果:
				v表格文本 = self.mf解析表格.f初始处理(v记录s)
				for v表格记录 in self.mf解析表格.fe记录(v表格文本):
					yield self.ma这次结果 | v表格记录
				self.ma上次结果 = self.ma这次结果
				self.ma这次结果 = {}
	def f下一记录(self, a文本, a开始位置)->int:
		"""计算下一记录的位置"""
		raise NotImplementedError()
	def fi有效记录(self, a记录: str):
		return True
	def fi结束(self, a行):
		return False
	def F上次结果(self, a字段):
		"""用于 C字段 的 af取值 中"""
		def f上次结果(a行_):
			return self.ma上次结果[a字段]
		return f上次结果
	def f上次结果(self, a字段):
		return self.ma上次结果[a字段]
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
