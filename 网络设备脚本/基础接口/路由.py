import enum
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_运算 as 运算
class E路由类型(enum.Enum):
	e无 = 0
	#网络层
	e本地 = 1
	e直连 = 2
	e静态 = 3
	e邻居发现协议 = 4	#ndp
	e热备份路由协议 = 5	#hsrp
	#动态路由协议
	e路由信息协议 = 10	#rip
	e开放最短路径优先 = 11	#ospf
	e边界网关协议 = 12	#bgp
	e增强内部网关路由协议 = 13	#eigrp
	e中间系统到中间系统 = 14	#isis
	#其它
	e按需路由 = 20	#odr
	e下一跳解析协议 = 21	#nhrp
	e移动 = 22	#nemo
	e定位与身份分离协议 = 23	#lisp