class I用户模式:
	def f模式_全局配置(self):
		raise NotImplementedError()
	def f模式_全局显示(self):
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
		"把当前配置保存到设备"
		raise NotImplementedError()
	def f导出配置(self, a目录 = "", a文件名 = ""):
		"把当前配置保存到本地电脑"
		raise NotImplementedError()
	def f清除配置(self, a重启 = False):
		"清除启动配置, 重启生效"
		raise NotImplementedError()	
	def fs终端监视(self, a开关):
		"terminal monitor"
		raise NotImplementedError()
