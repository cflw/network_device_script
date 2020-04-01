import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 信息
from ..基础接口 import 数据表
from ..命令行接口 import 设备 as 南向设备
from . import 接口 as 实现接口
#===============================================================================
# 接口表
#===============================================================================
def f解析网络地址4(a地址: str):
	if "--" in a地址:
		return None
	else:
		return 地址.S网络地址4.fc主机地址字符串(a地址)
def f判断有效行(a行: str):
	return len(a行) >= 50
class F接口表r4(数据表.I解析表格管线):
	"""display interface brief
	适用于: 路由器"""
	c接口 = 0
	c链路 = 21
	c协议 = 26
	c地址 = 35
	c描述 = 51
	ca列 = 序列.C切片组(c接口, c链路, c协议, c地址, c描述)
	c标题行 = "Interface            Link Protocol Primary IP      Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表r4.ca列.F切片(0), 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表r4.ca列.F切片(1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F接口表r4.ca列.F切片(2), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, F接口表r4.ca列.F切片(3), f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端描述, F接口表r4.ca列.F切片(4), str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(f判断有效行)
f接口表r4 = F接口表r4()
class F接口表s(数据表.I解析表格管线):
	"""display interface brief
	适用于: 交换机"""
	c接口 = 0
	c链路 = 21
	c速率 = 26
	c双工 = 34
	c类型 = 41
	c虚拟局域网 = 46
	c描述 = 51
	ca列 = 序列.C切片组(c接口, c链路, c速率, c双工, c类型, c虚拟局域网, c描述)
	c标题行 = "Interface            Link Speed   Duplex Type PVID Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表s.ca列.F切片(0), 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表s.ca列.F切片(1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端速率, F接口表s.ca列.F切片(2), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端双工模式, F接口表s.ca列.F切片(3), lambda s: s == "F")
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F接口表s.ca列.F切片(5), int)
		self.f添加字段(数据表.E字段.e本端描述, F接口表s.ca列.F切片(6), str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(f判断有效行)
f接口表s = F接口表s()
#===============================================================================
# 网络接口表
#===============================================================================
class F网络接口表4(数据表.I解析表格管线):
	"""display ip interface brief
	适用于:msr36系列"""
	c接口 = 0
	c物理 = 25
	c协议 = 34
	c地址 = 43
	c描述 = 59
	ca列 = 序列.C切片组(c接口, c物理, c协议, c地址, c描述)
	c标题行 = "Interface                Physical Protocol IP Address      Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列.F切片(0), 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4.ca列.F切片(1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列.F切片(2), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列.F切片(3), f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端描述, F网络接口表4.ca列.F切片(4), str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(f判断有效行)
f网络接口表4 = F网络接口表4()
