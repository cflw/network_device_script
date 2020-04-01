import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 信息
from ..基础接口 import 数据表
from ..基础接口 import 接口 as 北向接口
from . import 接口 as 实现接口
#===============================================================================
# 物理接口表
#===============================================================================
class F接口表(数据表.I解析表格管线):
	"""display interface brief"""
	c标题行0 = "Interface                   PHY   Protocol InUti OutUti   inErrors  outErrors"
	c接口 = 0
	c物理 = 28
	c协议 = 34
	c输入率 = 43
	c输出率 = 49
	c输入错误 = 58
	c输出错误 = 68
	ca列 = 序列.C切片组(c接口, c物理, c协议, c输入率, c输出率, c输入错误, c输出错误)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表.ca列.F切片(0), 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表.ca列.F切片(1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F接口表.ca列.F切片(2), 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效行长度(len(c标题行0)))
f接口表 = F接口表()
#===============================================================================
# 网络接口表
#===============================================================================
def f解析网络地址4(a地址: str):
	if "unassigned" in a地址:
		return None
	return 地址.S网络地址4.fc地址前缀长度字符串(a地址)
class F网络接口表4(数据表.I解析表格管线):
	"""display ip interface brief"""
	c标题行0 = "Interface                         IP Address/Mask      Physical   Protocol  "
	c接口 = 0
	c地址 = 34
	c物理 = 55
	c协议 = 66
	ca列 = 序列.C切片组(c接口, c地址, c物理, c协议)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列.F切片(0), 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列.F切片(1), f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4.ca列.F切片(2), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列.F切片(3), 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效行长度(c协议))	
f网络接口表4 = F网络接口表4()