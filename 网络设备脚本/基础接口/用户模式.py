class I用户模式:
	def f模式_全局配置(self):
		raise NotImplementedError()
	#显示设备状态
	def f显示_版本(self):
		raise NotImplementedError()
	def f显示_时间(self):
		"返回time.struct_time对象"
		raise NotImplementedError()
	def f显示_启动配置(self):
		raise NotImplementedError()
	def f显示_当前配置(self):
		raise NotImplementedError()
	def f显示_设备名称(self):
		"返回字符串"
		raise NotImplementedError()
	def f显示_日志(self):
		raise NotImplementedError()
	def f显示_设备版本(self):
		"返回字符串"
		raise NotImplementedError()
	def f显示_中央处理器使用率(self):
		raise NotImplementedError()
	def f显示_内存使用率(self):
		"返回数字"
		raise NotImplementedError()
	def f显示_温度(self):
		"返回字典，键=槽位，值=温度"
		raise NotImplementedError()
	def f显示_运行时间(self):
		"从开机到现在所经过的时间, 返回datetime.timedelta对象"
		raise NotImplementedError()
	def f显示_开机日期(self):
		"返回time.struct_time对象"
		raise NotImplementedError()
	def f显示_序列号(self):
		"返回字符串"
		raise NotImplementedError()
	def f显示_出厂日期(self):
		"返回time.struct_time对象"
		raise NotImplementedError()
	#显示具体
	def f显示_路由表4(self):
		raise NotImplementedError()
	def f显示_默认路由4(self):
		raise NotImplementedError()
	def f显示_链路层发现协议(self):
		"返回列表，列表包含邻居字典"
		raise NotImplementedError()
	def f显示_接口表(self):
		"返回接口表,应能迭代出 S接口表项"
		raise NotImplementedError()
	def f显示_网络接口表4(self):
		"返回网络接口表,应能迭代出 S网络接口表项"
		raise NotImplementedError()
	def f显示_网络接口表6(self):
		"返回网络接口表,应能迭代出 S网络接口表项"	
		raise NotImplementedError()
	def f显示_接口详细(self, a接口 = None):
		raise NotImplementedError()
	def f显示_网络接口详细4(self, a接口 = None):
		raise NotImplementedError()
	def f显示_网络接口详细6(self, a接口 = None):
		raise NotImplementedError()
	def f显示_物理地址表(self, a接口 = None):	#mac表
		raise NotImplementedError()
	def f显示_地址解析表(self, a接口 = None):	#arp表
		raise NotImplementedError()
	def f显示_网络地址转换表(self):	#nat表
		raise NotImplementedError()
	#连接
	def f连接_网络终端(self, a地址, **a参数):
		raise NotImplementedError()
	def f连接_安全外壳(self, a地址, **a参数):
		raise NotImplementedError()
	def f连接_集群(self, a名称):
		raise NotImplementedError()
	#动作
	def f登录(self, a用户名, a密码):
		raise NotImplementedError()
	def f提升权限(self, a密码, a级别):
		raise NotImplementedError()
	def f重新启动(self):
		"该函数只重启设备, 不保存配置. 要在重启前保存配置应调用 f保存配置"
		raise NotImplementedError()
	def f保存配置(self):
		raise NotImplementedError()
	def f清除配置(self):
		"清除启动配置, 重启生效"
		raise NotImplementedError()	
	def fs终端监视(self, a开关):
		"terminal monitor"
		raise NotImplementedError()
