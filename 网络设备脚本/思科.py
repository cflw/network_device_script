import enum
import cflw代码库py.cflw工具 as 工具
from .基础接口 import 连接层
#===============================================================================
# 工厂
#===============================================================================
class E型号(enum.IntEnum):
	c路由器 = 0x10000000
	c交换机 = 0x20000000
	c防火墙 = 0x40000000	#ASA系列
	c虚拟0 = 0x00010000	#Dynamips支持的型号
	c虚拟1 = 0x00020000	#IOS on Unix
	c虚拟2 = 0x00040000	#QEMU
	c连结 = 0x01000000	#Nexus系列.系统为NX-OS
	c路由 = 0x02000000	#CSR系列,ASR系列,XR系列.系统为IOS-XR,不知道XR中的X指的是什么
	#iou
	l2iou = c交换机 + c虚拟1 + 2
	l3iou = c路由器 + c虚拟1 + 3
	#c
	c1710 = c交换机 + c虚拟0 + 1710
	c2950 = c交换机 + c虚拟0 + 2950
	c2960 = c交换机 + c虚拟0 + 2960
	c3560 = c交换机 + c虚拟0 + 3560
	c7200 = c路由器 + c虚拟0 + 7200	#cisco 7200,ios版本12.x-15.x
	#nexus系列数据中心交换机
	n3k = c交换机 + c连结 + 3000	#nexus 3000
	n5k = c交换机 + c连结 + 5000	#nexus 7000
	n7k = c交换机 + c连结 + 7000	#nexus 7000
	n9k = c交换机 + c连结 + 9000	#nexus 9000
	nxosv9k = c交换机 + c连结 + c虚拟2 + 9000	#nxos v9000
	#xr系列运营商路由器
	c12000 = c路由器 + c路由 + 12000	#cisco 12000
	xrv7k = c路由器 + c路由 + c虚拟2 + 7000	#xrv7000
	xrv9k = c路由器 + c路由 + c虚拟2 + 9000	#xrv9000
	xr12000 = c路由器 + c路由 + 12000	#cisco xr 12000
	csr1kv = c路由器 + c虚拟2 + 1000	#csr1000v,iosxe版本3.x,ios版本15.x
	csr1kvng = c路由器 + c虚拟2 + 1001	#csr1000vng,iosxe版本16.x,ios版本16.x
def f创建设备(a连接, a型号: int = 0, a版本 = 0):
	v版本 = 工具.S版本号.fc自动(a版本)
	if 连接层.fi命令行(a连接):	#命令行
		if a型号 & E型号.c连结:
			from .思科连结命令行 import 设备
			if v版本 >= 9:
				return 设备.C设备_nv9(a连接, a型号, v版本)
			elif v版本 >= 7:
				return 设备.C设备_nv7(a连接, a型号, v版本)
			raise ValueError("不支持的版本")
		else:
			from .思科命令行 import 设备
			return 设备.C设备(a连接, a型号, v版本)
	elif 连接层.fi网页(a连接):	#网页
		if a型号 & E型号.c虚拟0:
			from .思科网页 import 命令行设备
			return 命令行设备.C设备(a连接, a型号, v版本)
	elif 连接层.fi简单网管(a连接):	#简单网管
		from .思科简单网管 import 设备
		return 设备.C设备(a连接, a型号, v版本)
	raise ValueError("不支持的连接,型号,版本")