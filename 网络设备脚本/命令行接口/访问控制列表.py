import ipaddress
import functools
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 访问控制列表
from . import 命令
from . import 模式
#===============================================================================
# 实用
#===============================================================================
#名称
def f解析名称和类型(a名称, a类型, a助手):
	def f返回(a名称1):	#解析类型
		if a类型:
			return a名称1, a类型
		else:
			return a名称1, a助手.f判断类型(a名称1)
	v名称类型 = type(a名称)
	if v名称类型 == int:
		return f返回(a名称)
	elif v名称类型 == str:
		if a名称.isdigit():
			return f返回(int(a名称))
		return f返回(a名称)
	elif v名称类型 == 访问控制列表.S统一编号:
		#检查序号
		if a名称.m特定编号:
			return f返回(a名称.m特定编号)
		elif a名称.m统一编号 == None:
			raise ValueError("没有序号")
		#计算特定编号
		v序号类型空 = a名称.m类型 == None
		v参数类型空 = a类型 == None
		if (not v序号类型空) and (not v参数类型空):
			raise ValueError("没有类型")
		elif v序号类型空 and v参数类型空:
			if a名称.m类型 != a类型:
				raise ValueError("类型不同")
		v类型 = a类型 if a类型 else a名称.m类型
		v特定编号 = a助手.ft特定编号(a名称.m统一编号, v类型)
		return f返回(v特定编号)
	else:
		raise TypeError("无法解析的类型")
#协议
ca协议到字符串4 = {
	协议.E协议.ipv4: "ip",
	协议.E协议.ipv6: "ipv6",
	协议.E协议.tcp: "tcp",
	协议.E协议.udp: "udp",
}
ca协议到字符串6 = {
	协议.E协议.ipv4: "ip",
	协议.E协议.ipv6: "ipv6",
	协议.E协议.tcp: "tcp",
	协议.E协议.udp: "udp",
}
ca字符串到协议 = {
	"ip": 协议.E协议.e网络协议4,
	"ipv6": 协议.E协议.e网络协议6,
	"tcp": 协议.E协议.e传输控制协议,
	"udp": 协议.E协议.e用户数据报协议,
}
def F生成协议(a字典):
	def f(a协议)->str:
		v类型 = type(a协议)
		if v类型 == int:
			return str(v类型)
		elif v类型 == 协议.E协议:
			return a字典[a协议]
		elif v类型 == str:
			return a协议
		else:
			raise TypeError()
	return f
f生成协议4 = F生成协议(ca协议到字符串4)
f生成协议6 = F生成协议(ca协议到字符串6)
#动作
c允许 = "permit"
c拒绝 = "deny"
c动作元组 = (c允许, c拒绝)
def F生成动作(a元组: tuple):
	def f(a动作)->str:
		if type(a动作) == str:
			if a动作 in a元组:
				return a动作
			raise ValueError()
		if a动作:
			return a元组[0]
		else:
			return a元组[1]
	return f
def F解析动作(a元组: tuple):
	def f(a字符串: str)->bool:
		if a字符串 == a元组[0]:
			return True
		elif a字符串 == a元组[1]:
			return False
		else:
			raise ValueError()
	return f
f生成动作 = F生成动作(c动作元组)
f解析动作 = F解析动作(c动作元组)
#地址
def f生成地址和通配符4(a地址)->str:
	v地址 = 地址.S网络地址4.fc自动(a地址)
	return "%s %s" % (v地址.fg网络号s(), v地址.fg反掩码s())
#===============================================================================
# 配置模式
#===============================================================================
class I列表配置(模式.I模式, 访问控制列表.I列表配置):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
