import enum
class E协议(enum.IntEnum):
	#应用层协议
	c应用层协议 = 0x07000000
	e文件传输协议 = c应用层协议 + 21
	e安全外壳 = c应用层协议 + 22
	e网络终端 = c应用层协议 + 23
	e动态主机配置协议服务端 = c应用层协议 + 67
	e动态主机配置协议客户端 = c应用层协议 + 68
	e简单文件传输协议 = c应用层协议 + 69
	e超文本传输协议 = c应用层协议 + 80
	ftp = e文件传输协议
	ssh = e安全外壳
	telnet = e网络终端
	dhcp_s = e动态主机配置协议服务端
	dhcp_c = e动态主机配置协议客户端
	tftp = e简单文件传输协议
	http = e超文本传输协议
	#表示层协议
	c表示层协议 = 0x06000000
	e安全套接层 = c表示层协议 + 0x0100
	e传输层安全 = c表示层协议 + 0x0200
	ssl = e安全套接层
	tls = e传输层安全
	#会话层协议
	c会话层协议 = 0x05000000
	e袜子5 = c会话层协议 + 0x0105
	socks5 = e袜子5
	#传输层协议
	c传输层协议 = 0x04000000
	e传输控制协议 = c传输层协议 + 0x0100
	e用户数据报协议 = c传输层协议 + 0x0200
	tcp = e传输控制协议
	udp = e用户数据报协议
	#路由协议
	c路由协议 = 0x03010000
	e路由信息协议 = c路由协议 + 0x0100
	e下一代路由信息协议 = c路由协议 + 0x0103
	e开放最短路径优先 = c路由协议 + 0x0200
	e开放最短路径优先2 = e开放最短路径优先
	e开放最短路径优先3 = c路由协议 + 0x0203
	e增强内部网关路由协议 = c路由协议 + 0x0300
	e中间系统到中间系统 = c路由协议 + 0x0400
	e边界网关协议 = c路由协议 + 0x9999
	rip =e路由信息协议
	ripng = e下一代路由信息协议
	ospf = e开放最短路径优先
	ospfv2 = e开放最短路径优先2
	ospfv3 = e开放最短路径优先3
	eigrp = e增强内部网关路由协议
	isis = e中间系统到中间系统
	bgp = e边界网关协议
	#网络层协议
	c网络层协议 = 0x03000000
	e网络协议 = c网络层协议
	e网络协议4 = c网络层协议 + 0x0400
	e网络协议6 = c网络层协议 + 0x0600
	ip = e网络协议
	ipv4 = e网络协议4
	ipv6 = e网络协议6
	#数据链路层协议
	c数据链路层协议 = 0x02000000
	e以太网 = c数据链路层协议 + 1
	e地址解析协议 = c数据链路层协议 + 0x0806
	e虚拟局域网 = c数据链路层协议 + 0x8100
	e点对点协议 = c数据链路层协议 + 0x880b
	e链路层发现协议 = c数据链路层协议 + 0x88cc
	vlan = e虚拟局域网
	ppp = e点对点协议
	lldp = e链路层发现协议
	#物理层协议
	c物理层协议 = 0x01000000
def f取协议层(a协议):
	if a协议 & E协议.c网络层协议:
		return 3
	elif a协议 & E协议.c传输层协议:
		return 4
	elif a协议 & E协议.c数据链路层协议:
		return 2
	elif a协议 & E协议.c物理层协议:
		return 1
	elif a协议 & E协议.c应用层协议:
		return 7
	elif a协议 & E协议.c会话层协议:
		return 5
	elif a协议 & E协议.c表示层协议:
		return 6
	raise ValueError()
ca端口号字符串到数字 = {
	"bgp": 179,
	"biff": 512,
	"bootpc": 68,
	"bootps": 67,
	"chargen": 19,
	"cmd": 514,
	"daytime": 13,
	"discard": 9,
	"dns": 53,
	"dnsix": 90,
	"domain": 53,
	"echo": 7,
	"exec": 512,
	"finger": 79,
	"ftp": 21,
	"ftp-data": 20,
	"gopher": 70,
	"hostname": 101,
	"irc": 194,
	"klogin": 543,
	"kshell": 544,
	"login": 513,
	"lpd": 515,
	"mobilip-ag": 434,
	"mobilip-mn": 435,
	"nameserver": 42,
	"netbios-dgm": 138,
	"netbios-ns": 137,
	"netbios-ssn": 139,
	"nntp": 119,
	"ntp": 123,
	"pop2": 109,
	"pop3": 110,
	"rip": 520,
	"smtp": 25,
	"snmp": 161,
	"snmptrap": 162,
	"sunrpc": 111,
	"syslog": 514,
	"tacacs": 49,
	"tacacs-ds": 65,
	"talk": 517,
	"telnet": 23,
	"tftp": 69,
	"time": 37,
	"uucp": 540,
	"who": 513,
	"whois": 43,
	"www": 80,
	"xdmcp": 177,
}
def f解析端口号(a端口号):
	v类型 = type(a端口号)
	if v类型 == int:
		return a端口号
	elif v类型 == str:
		if a端口号.isdigit():
			return int(a端口号)
		elif a端口号 in ca端口号字符串到数字:
			return ca端口号字符串到数字[a端口号]
		else:
			raise ValueError("无法解析的端口号")
	else:
		raise TypeError("无法解析的类型")