import enum
import cflw代码库py.cflw字符串 as 字符串
#===============================================================================
# 基础
#===============================================================================
c问候时间 = 10
c死亡时间 = 40
c重传时间 = 5
c传输时间 = 1
class E链路状态通告类型(enum.IntEnum):
	"OSPF LSA类型"
	e全部 = 0
	e路由器 = 1
	e网络 = 2
	e网络汇总 = 3
	e区域边界路由器汇总 = 4
	e自治系统外部 = 5
	e组成员 = 6
	e非纯末节区域外部 = 7
	e外部属性 = 8
	e本地链路不透明 = 9
	e本地区域不透明 = 10
	e自制系统不透明 = 11
	#ospfv3
	e链路 = 8
	e区域内前缀 = 9
class E邻居状态(enum.IntEnum):
	e关闭 = 0
	e尝试 = 1
	e初始 = 2
	e双向 = 3
	e预启动 = 4
	e交换 = 5
	e加载 = 6
	e完成 = 7
class E选举状态(enum.IntEnum):
	e无 = 0
	e指定 = 1
	e备用 = 2
	e非指定 = 3
class S邻居表项:
	def __init__(self, a邻居标识, a优先级, a邻居状态, a选举状态, a死亡时间, a对端地址, a接口):
		self.m邻居标识 = a邻居标识
		self.m优先级 = a优先级
		self.m邻居状态 = a邻居状态
		self.m选举状态 = a选举状态
		self.m死亡时间 = a死亡时间
		self.m对端地址 = a对端地址
		self.m接口 = a接口
	def __str__(self):
		return 字符串.ft字符串(self.m邻居标识, self.m优先级, self.m邻居状态, self.m选举状态, self.m死亡时间, self.m对端地址, self.m接口)
#===============================================================================
# 配置
#===============================================================================
class I进程配置:
	c模式名 = "开放最短路径优先进程配置模式"
	#模式
	def f模式_区域(self, a区域, a操作):
		raise NotImplementedError()
	def f模式_接口(self, a接口):
		raise NotImplementedError()
	def f模式_虚链路(self, a区域, a对端, a操作):
		raise NotImplementedError()
	#显示
	def f显示_路由表(self):
		raise NotImplementedError()
	def f显示_邻居(self):
		raise NotImplementedError()
	def f显示_数据库(self, a类型):
		raise NotImplementedError()
	#操作
	def f重启进程(self):
		raise NotImplementedError()
	def fs路由器号(self, a):
		raise NotImplementedError()
	def fs通告默认路由(self, a总是, a开销, a操作):
		raise NotImplementedError()
	def fs通告网络(self, a网络号, a区域号, a操作):
		raise NotImplementedError()
	def fs通告接口(self, a接口, a区域号, a操作):
		raise NotImplementedError()
class I区域配置:
	c模式名 = "开放最短路径优先区域配置模式"
	def fs通告网络(self, a网络号, a操作):
		raise NotImplementedError()
	def fs通告接口(self, a接口, a操作):
		raise NotImplementedError()
	def fs认证(self, a认证方式, a密码, a操作):
		raise NotImplementedError()
class I接口配置:
	c模式名 = "开放最短路径优先接口配置模式"
	def fs通告接口(self, a区域号, a操作):
		raise NotImplementedError()
	def fs认证(self, a认证方式, a密码, a操作):
		raise NotImplementedError()
	def fs问候时间(self, a时间):
		raise NotImplementedError()
	def fs死亡时间(self, a时间):
		raise NotImplementedError()
	def fs重传时间(self, a时间):
		raise NotImplementedError()
	def fs传输时间(self, a时间):
		raise NotImplementedError()
	def fs开销(self, a开销):
		raise NotImplementedError()
	def fs网络类型(self, a类型):
		raise NotImplementedError()
	def fs检查最大传输单元(self, a):
		raise NotImplementedError()
	def fs接口多协议标签交换同步(self, a):
		raise NotImplementedError()
class I虚链路配置:
	c模式名 = "开放最短路径优先虚链路配置模式"
	def fs认证(self, a认证方式, a密码, a操作):
		raise NotImplementedError()
	def fs问候时间(self, a时间):
		raise NotImplementedError()
	def fs死亡时间(self, a时间):
		raise NotImplementedError()
	def fs重传时间(self, a时间):
		raise NotImplementedError()
	def fs传输时间(self, a时间):
		raise NotImplementedError()
