from ..网页接口 import 设备
class C设备(设备.I设备):
	"""适用于: SG-6000-P1242(v5.5)"""
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.ma模式 = {0:(), 1:(), 2:(0,0), 3:(0,), 4:(0,), 5:(0,), 6:(0,)}	#每个顶级模式都保存一份自己的模式状态
		self.m当前顶级模式 = 0
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式(self)
	def f切换模式(self, aa模式: tuple):
		C切换模式.f切换模式(self, aa模式)
	def f等待可用(self):	#检测是否存在<div class="x-mask">
		self.f等待不存在('//div[@class="x-mask"]')
	def fg当前主要模式(self):
		return self.ma模式[self.m当前顶级模式]
	def fs当前主要模式(self, aa模式: tuple):
		self.ma模式[self.m当前顶级模式] = aa模式
	m当前主要模式 = property(fg当前主要模式, fs当前主要模式)
class C切换模式:
	"""静态类"""
	@staticmethod
	def f切换模式(a设备, aa模式: tuple):
		v新长度 = len(aa模式)
		#顶部
		if vi切换顶级 := a设备.m当前顶级模式 != aa模式[0]:	#切换顶级模式
			C切换模式.f点击按钮(a设备, C切换模式.f顶栏模式路径(aa模式[0]))
			a设备.m当前顶级模式 = aa模式[0]
		if v新长度 == 1:
			return
		#侧栏
		v原主长度 = len(a设备.m当前主要模式)
		def f折叠():
			if a设备.m当前主要模式[0] != aa模式[1] and v原主长度 == 2:	#折叠
				C切换模式.f点击按钮(a设备, C切换模式.f侧栏折叠路径(a设备.m当前主要模式[0]))
		if v新长度 == 2:
			f折叠()
			C切换模式.f点击按钮(a设备, C切换模式.f侧栏模式路径1(aa模式[1]))
		elif v新长度 == 3:
			f折叠()
			C切换模式.f点击按钮(a设备, C切换模式.f侧栏折叠路径(aa模式[1]))
			C切换模式.f点击按钮(a设备, C切换模式.f侧栏模式路径2(aa模式[1], aa模式[2]))
		else:
			raise RuntimeError()
		a设备.m当前主要模式 = aa模式[1:]
	@staticmethod
	def f点击按钮(a设备, a路径: str):
		w按钮 = a设备.f查找(a路径)
		w按钮.f点击()
		a设备.f等待可用()
	@staticmethod
	def f顶栏模式路径(a序号0: int):
		return  f"/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[{a序号0+1}]/span"
	@staticmethod
	def f侧栏模式路径1(a序号1: int):
		return f"/html/body/div[2]/div[2]/div/table/tbody/tr[{a序号1+1}]/td/div/a"
	@staticmethod
	def f侧栏模式路径2(a序号1: int, a序号2: int):
		return f"/html/body/div[2]/div[2]/div/table/tbody/tr[{a序号1+a序号2+2}]/td/div/a"
	@staticmethod
	def f侧栏折叠路径(a序号1: int):
		return f"/html/body/div[2]/div[2]/div/table/tbody/tr[{a序号1+1}]/td/div/img[1]"
