class I全局显示:
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
	def f显示_中央处理器利用率(self):
		raise NotImplementedError()
	def f显示_内存利用率(self):
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
		raise NotImplementedError()
	def f显示_接口表(self):
		raise NotImplementedError()
	def f显示_网络接口表4(self):
		raise NotImplementedError()
	def f显示_网络接口表6(self):
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
