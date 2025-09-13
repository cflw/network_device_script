import enum
import cflw代码库py.cflw工具_运算 as 运算
#===============================================================================
# 枚举
#===============================================================================
class E服务类型(enum.IntEnum):
	e无 = 0x00
	e终端 = 0x01	#terminal
	e网络终端 = 0x02	#telnet
	e安全外壳 = 0x04	#ssh
	e网页 = 0x08	#web
	e超文本 = 0x10	#http
	e全部 = 0xff
def f解析服务类型(a):
	"""把参数转换成 E服务类型 列表"""
	v类型 = type(a)
	if v类型 == int:
		return 运算.f位拆分(a)
	elif v类型 in (tuple, list):
		return a
	else:
		raise ValueError("无法解析的类型")
class E用户权限(enum.Enum):
	e最低 = 0
	e最高 = 1
#===============================================================================
# 模式
#===============================================================================
class I用户配置:
	c模式名 = "用户配置模式"
	def fs密码(self, a密码, a操作):
		raise NotImplementedError()
	def fs权限(self, a权限, a操作):
		raise NotImplementedError()
	def fs服务类型(self, a服务类型, a操作):
		raise NotImplementedError()
class I用户显示:
	def fg用户名(self):
		raise NotImplementedError()
	def fg密码(self):	#基本上只能显示密文密码
		raise NotImplementedError()
	def fg权限(self):
		raise NotImplementedError()
	def fg服务类型(self):
		raise NotImplementedError()
#===============================================================================
# 助手
#===============================================================================
class I权限级别助手:
	@staticmethod
	def fg最低级别()->int:
		raise NotImplementedError()
	@staticmethod
	def fg最高级别()->int:
		raise NotImplementedError()
def f级别转换(a源级别, a源助手: I权限级别助手, a目标助手: I权限级别助手):
	v类型 = type(a源级别)
	if v类型 == E用户权限:
		if a源级别 == E用户权限.e最低:
			return a目标助手.fg最低级别()
		elif a源级别 == E用户权限.e最高:
			return a目标助手.fg最高级别()
		else:
			raise ValueError()
	elif v类型 == int:	#把源区间转成目标区间
		return ((a源级别 - a源助手.fg最低级别()) / a源助手.fg最高级别()) * a目标助手.fg最高级别() + a目标助手.fg最低级别()