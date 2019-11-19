import time
from ..基础接口 import 时间 as 北向时间
c时间格式 = "%H:%M:%S %m/%d/%Y"	#(v6.x)
def f解析时间ev6(a时间: str):
	#16:00:01 11/18/2019
	return time.strptime(a时间, c时间格式)
class C时间ev6(北向时间.I时间配置):
	"""适用于: 浪潮s5350(v6.x)"""
	c日期时间路径 = "/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[10]/td[3]/input"
	c日期时间应用路径 = "/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[10]/td[6]/input"
	c时间名称路径 = "/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[12]/td[3]/input"
	c时区偏移符号路径 = "/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[13]/td[3]/select[1]"
	c时区偏移时路径 = "/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[13]/td[3]/select[2]"
	c时区偏移分路径 = "/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[13]/td[3]/select[3]"
	c时区偏移秒路径 = "/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[13]/td[3]/select[4]"
	def __init__(self, a设备):
		self.m设备 = a设备
	def fs日期时间(self, a日期时间):
		self.m设备.f切换模式(模式.C模式ev6.c系统管理_系统配置)
		w日期时间 = self.m设备.f网页_查找(C时间ev6.c日期时间路径)
		w日期时间.f输入(time.strftime(c时间格式, a日期时间))
		w应用 = self.m设备.f网页_查找(C时间ev6.c应用路径)
		w应用.f点击()
	def fs时区(self, a时区):
		self.m设备.f切换模式(模式.C模式ev6.c系统管理_系统配置)
		raise NotImplementedError()