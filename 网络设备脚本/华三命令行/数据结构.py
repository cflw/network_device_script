class C网络地址池(设备.I网络协议地址池, 设备.C同级模式):
	def __init__(self, a, a名称):
		设备.I网络协议地址池.__init__(self, a, a名称)
	def fs地址范围(self, a开始, a结束 = None):
		v命令 = self.fg命令前缀()
		v命令 += a开始
		if a结束:
			v命令 += a结束
		self.f切换到当前模式()
		self.m设备.f执行命令(v命令)
	def fs默认网关(self, p网关):
		v命令 = self.fg命令前缀()
		v命令.f添加("gateway", p网关)
		self.f切换到当前模式()
		self.m设备.f执行命令(v命令)
	def fg命令前缀(self):
		return 命令.C命令("ip pool " + self.m名称)
