
class C用户配置(设备.I用户配置):
	def __init__(self, a, a用户名):
		设备.I用户配置.__init__(self, a, a用户名)
	def fs密码(self, a密码, a加密等级):
		v加密等级 = C实用工具.f加密等级(a加密等级)
		v命令 = 'username %s password %s %s' % (self.m用户名, v加密等级, a密码)
		self.m设备.f执行命令(v命令)
