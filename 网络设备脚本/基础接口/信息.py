import enum
import re
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
class I版本信息:	#废弃
	def fg版本s(self)->str:
		"完整的版本字符串"
		raise NotImplementedError()
	def fg版本号(self)->str:
		raise NotImplementedError()
	def fg编译日期(self):
		"""返回time.struct_time对象
		如果找不到,返回None"""
		raise NotImplementedError()
	def fg运行时间(self):
		"""返回datetime.timedelta对象"""
		raise NotImplementedError()
	def fg开机日期(self):
		"""返回time.struct_time对象"""
		raise NotImplementedError()
class E物理地址类型(enum.Enum):
	e动态 = 0
	e静态 = 1
	e安全 = 2
	e黑洞 = 3
class E地址解析协议类型(enum.Enum):
	e动态 = 0
	e静态 = 1
	e接口 = 2	#本端接口
#===============================================================================
# 解析
#===============================================================================
def f解析数字(a数字: str):
	"""可解析: 整数, 小数, 百分数, 非数字(返回0)"""
	if not a数字:
		return 0
	elif a数字[-1] == "%":	#百分数
		return float(a数字[:-1]) * 0.01
	elif "." in a数字:
		return float(a数字)
	elif a数字.isdigit():
		return int(a数字)
	else:
		return 0
def f解析起宕状态(a状态: str)->bool:
	"up为真"
	return "up" in a状态.lower()
def F解析管理状态(a起: str = "", a宕: str = ""):
	if a起:
		return lambda x: a起 in x
	elif a宕:
		return lambda x: not a宕 in x
	else:
		raise ValueError()
def f解析双工模式(a双工: str)->bool:
	"full为真"
	v双工 = a双工.lower()
	if "full" in v双工:
		return True
	elif "half" in v双工:
		return False
	return None	#未知
c速率正则 = re.compile(r"(\d+)([GMk])")
def f解析速率(a速率: str)->int:
	"解析带单位的速率"
	if v速率 := c速率正则.search(a速率):
		v数字 = int(v速率[1])
		v倍数 = 1
		if v速率.lastindex >= 2:
			v单位 = v速率[2]
			if v单位 == "G":
				v倍数 = 10 ** 9
			elif v单位 == "M":
				v倍数 = 10 ** 6
			elif v单位 == "k":
				v倍数 = 10 ** 3
			# else:
			# 	v倍数 = 1
		return v数字 * v倍数
	return 0
def f解析链路类型(a类型: str):
	from . import 虚拟局域网
	v类型 = a类型.lower()
	if "access" in v类型:
		return 虚拟局域网.E链路类型.e接入
	elif "trunk" in v类型:
		return 虚拟局域网.E链路类型.e中继
	elif "hybrid" in v类型:
		return 虚拟局域网.E链路类型.e混合
	else:
		return 虚拟局域网.E链路类型.e无
def f解析虚拟局域网(a数字: str)->int:
	if a数字.isdigit():
		return int(a数字)
	else:
		return 0	#不是二层口
ca物理地址类型 = {
	"static": E物理地址类型.e静态,
	"dynamic": E物理地址类型.e动态,
	"security": E物理地址类型.e安全,
	"blackhole": E物理地址类型.e黑洞
}
def f解析物理地址类型(a类型: str):
	return ca物理地址类型.get(a类型.lower(), None)
ca地址解析协议类型 = {
	"static": E地址解析协议类型.e静态,
	"dynamic": E地址解析协议类型.e动态,
}
def f解析地址解析协议类型(a类型: str):
	return ca物理地址类型.get(a类型.lower(), None)
def f解析网络地址4(a地址: str):
	if "unassigned" in a地址:	#思科华为设备接口没地址会显示unassigned
		return None
	if "--" in a地址:	#华三设备没地址会显示--
		return None
	if "/" in a地址:
		return 地址.S网络地址4.fc地址前缀长度字符串(a地址)
	else:
		return 地址.S网络地址4.fc主机地址字符串(a地址)