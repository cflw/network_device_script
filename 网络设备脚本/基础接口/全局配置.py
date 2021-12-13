class I全局配置:
	c模式名 = "全局配置模式"
	#模式 系统
	def f模式_设备(self):
		raise NotImplementedError()
	def f模式_时间(self):
		raise NotImplementedError()
	def f模式_日志(self):
		raise NotImplementedError()
	def f模式_接口(self, a接口, a操作):
		raise NotImplementedError()
	def f模式_用户(self, a用户名, a操作):
		raise NotImplementedError()
	def f模式_登录(self, a方式, a范围, a操作):	#废弃
		raise NotImplementedError()
	def f模式_串口登录(self, a操作):
		raise NotImplementedError()
	def f模式_远程登录(self, a协议, a范围, a操作):
		raise NotImplementedError()
	def f模式_时间范围(self, a名称, a操作):
		raise NotImplementedError()
	def f模式_地址解析协议(self):
		raise NotImplementedError()
	#模式 路由
	def f模式_静态路由(self, a版本, a虚拟路由转发):
		raise NotImplementedError()
	def f模式_路由信息协议(self, a进程号, a版本, a接口, a操作):	#rip
		raise NotImplementedError()
	def f模式_开放最短路径优先(self, a进程号, a版本, a接口, a操作):	#ospf
		raise NotImplementedError()
	def f模式_增强内部网关路由协议(self, a名称, a版本, a接口, a操作):	#eigrp
		raise NotImplementedError()
	def f模式_中间系统到中间系统(self, a进程号, a版本, a接口, a操作):	#isis
		raise NotImplementedError()
	def f模式_边界网关协议(self, a自治系统号, a操作):	#bgp
		raise NotImplementedError()
	def f模式_热备份路由协议(self, a接口, a组号, a操作):	#hsrp
		raise NotImplementedError()
	def f模式_虚拟路由器冗余协议(self, a接口, a组号, a操作):	#vrrp
		raise NotImplementedError()	
	def f模式_网关负载均衡协议(self, a接口, a组号, a操作):	#glbp
		raise NotImplementedError()
	#模式 交换
	def f模式_虚拟局域网(self, a序号, a操作):	#vlan
		raise NotImplementedError()
	def f模式_生成树(self, a模式, a接口, a操作):	#stp
		raise NotImplementedError()
	def f模式_端口安全(self, a操作):
		raise NotImplementedError()
	#模式 数据结构
	def f模式_访问控制列表(self, a名称, a类型, a操作):
		raise NotImplementedError()
	def f模式_前缀列表(self, a名称, a类型, a操作):
		raise NotImplementedError()
	def f模式_虚拟路由转发(self, a名称, a接口, a操作):
		raise NotImplementedError()
	def f模式_策略路由(self, a名称, a操作):
		raise NotImplementedError()
	def f模式_路由策略(self, a名称, a操作):
		raise NotImplementedError()
	#模式 服务质量
	def f模式_流量分类(self, a名称, ai匹配全部, a操作):
		raise NotImplementedError()
	def f模式_流量行为(self, a名称, a操作):
		raise NotImplementedError()
	def f模式_流量策略(self, a名称, a操作):
		raise NotImplementedError()
	#模式 服务
	def f模式_网络终端(self):	#telnet
		raise NotImplementedError()
	def f模式_安全外壳(self):	#ssh
		raise NotImplementedError()
	def f模式_网络协议地址池(self, a名称, a操作):	#ip pool
		raise NotImplementedError()
	def f模式_动态主机配置协议地址池(self, a名称, a操作):	#dhcp pool
		raise NotImplementedError()
	def f模式_动态主机配置协议(self):	#dhcp
		raise NotImplementedError()
	def f模式_域名系统(self):	#dns
		raise NotImplementedError()
	def f模式_网络时间协议(self, a端, a操作):	#ntp
		raise NotImplementedError()
	def f模式_简单网络管理协议(self, a端, a操作):	#snmp
		raise NotImplementedError()
	def f模式_以太网上的点对点协议(self):	#pppoe
		raise NotImplementedError()
	def f模式_多协议标签交换(self):	#mpls
		raise NotImplementedError()
	def f模式_第二层隧道协议(self, a名称):	#l2tp
		raise NotImplementedError()