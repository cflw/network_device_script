from . import 模式
class C序列号页:
	"""适用于: ad 7.0.3"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def fg网关序号(self):
		self.m设备.f切换模式(模式.C模式ad70.c系统配置_序列号)
		w网关序号 = self.m设备.f查找("//*[@id=\"sn_id\"]")
		return w网关序号.fg文本()
	def fg基本授权序列号(self):
		self.m设备.f切换模式(模式.C模式ad70.c系统配置_序列号)
		w序列号 = self.m设备.f查找("//*[@id=\"base_sn\"]")
		return w序列号.fg文本()
	def fgSSL卸载授权序列号(self):
		self.m设备.f切换模式(模式.C模式ad70.c系统配置_序列号)
		w序列号 = self.m设备.f查找("//*[@id=\"ssl_sn\"]")
		return w序列号.fg文本()
	def fgTCP单边加速授权序列号(self):
		self.m设备.f切换模式(模式.C模式ad70.c系统配置_序列号)
		w序列号 = self.m设备.f查找("//*[@id=\"tcp_sn\"]")
		return w序列号.fg文本()
	def fgHTTP缓存授权序列号(self):
		self.m设备.f切换模式(模式.C模式ad70.c系统配置_序列号)
		w序列号 = self.m设备.f查找("//*[@id=\"http_sn\"]")
		return w序列号.fg文本()
	def fg智能DNS全局授权序列号(self):
		self.m设备.f切换模式(模式.C模式ad70.c系统配置_序列号)
		w序列号 = self.m设备.f查找("//*[@id=\"gfad_sn\"]")
		return w序列号.fg文本()
	def fg软件升级授权序列号(self):
		self.m设备.f切换模式(模式.C模式ad70.c系统配置_序列号)
		w序列号 = self.m设备.f查找("//*[@id=\"update_sn\"]")
		return w序列号.fg文本()
