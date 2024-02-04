from ..网页接口 import 设备
class C设备(设备.I设备):
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.ma模式 = {0:(), 1:(), 2:(0,0), 3:(0,), 4:(0,), 5:(0,), 6:(0,)}	#每个顶级模式都保存一份自己的模式状态
		self.m当前顶级模式 = 0
	def f切换模式(self, aa模式: tuple):
		v新长度 = len(aa模式)
		#顶部
		if vi切换顶级 := self.m当前顶级模式 != aa模式[0]:	#切换顶级模式
			self.f点击按钮(self.f顶栏模式路径(aa模式[0]))
			self.m当前顶级模式 = aa模式[0]
		if v新长度 == 1:
			return
		#侧栏
		v原主长度 = len(self.m当前主要模式)
		def f折叠():
			if self.m当前主要模式[0] != aa模式[1] and v原主长度 == 2:	#折叠
				self.f点击按钮(self.f侧栏折叠路径(self.m当前顶级模式, self.m当前主要模式[0]))
		if v新长度 == 2:
			f折叠()
			self.f点击按钮(self.f侧栏模式路径1(aa模式[0], aa模式[1]))
		elif v新长度 == 3:
			f折叠()
			self.f点击按钮(self.f侧栏折叠路径(aa模式[0], aa模式[1]))
			self.f点击按钮(self.f侧栏模式路径2(aa模式[0], aa模式[1], aa模式[2]))
		else:
			raise RuntimeError()
		self.m当前主要模式 = aa模式[1:]
	def f等待可用(self):	#检测是否存在<div class="x-mask">
		self.f等待不存在('//div[@class="x-mask"]')
	def fg当前主要模式(self):
		return self.ma模式[self.m当前顶级模式]
	def fs当前主要模式(self, aa模式: tuple):
		self.ma模式[self.m当前顶级模式] = aa模式
	m当前主要模式 = property(fg当前主要模式, fs当前主要模式)
	def f点击按钮(self, a路径: str):
		w按钮 = self.f查找(a路径)
		w按钮.f点击()
		self.f等待可用()
class C模式路径_p:
	@staticmethod
	def f顶栏模式路径(a序号0: int):
		return  f"/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[{a序号0+1}]/span"
	@staticmethod
	def f侧栏模式路径1(a序号0: int, a序号1: int):
		return f"/html/body/div[2]/div[2]/div/table/tbody/tr[{a序号1+1}]/td/div/a"
	@staticmethod
	def f侧栏模式路径2(a序号0: int, a序号1: int, a序号2: int):
		return f"/html/body/div[2]/div[2]/div/table/tbody/tr[{a序号1+a序号2+2}]/td/div/a"
	@staticmethod
	def f侧栏折叠路径(a序号0: int, a序号1: int):
		return f"/html/body/div[2]/div[2]/div/table/tbody/tr[{a序号1+1}]/td/div/img[1]"
class C设备_p(C设备, C模式路径_p):
	"""适用于: 山石SG-6000-P1242(v5.5)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式_p(self)
class C模式路径_a:
	def __init__(self):
		self.m顶栏字典 = {}	#进入一次顶级模式记录当前顶级模式的顺序
	def f顶栏模式路径(self, a序号0: int):
		return  f"/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div[{a序号0+1}]/span"
	def f侧栏模式路径1(self, a序号0: int, a序号1: int):	#侧栏菜单的中间div会随着点击顶栏菜单而按顺序增加
		return f"/html/body/div[2]/div[1]/div/div/div{self.f侧栏中间顺序字符(a序号0)}/div[2]/div/table/tbody/tr[{a序号1+1}]/td/div/a"
	def f侧栏模式路径2(self, a序号0: int, a序号1: int, a序号2: int):
		return f"/html/body/div[2]/div[1]/div/div/div{self.f侧栏中间顺序字符(a序号0)}/div[2]/div/table/tbody/tr[{a序号1+a序号2+2}]/td/div/a"
	def f侧栏折叠路径(self, a序号0: int, a序号1: int):
		return f"/html/body/div[2]/div[1]/div/div/div{self.f侧栏中间顺序字符(a序号0)}/div[2]/div/table/tbody/tr[{a序号1+1}]/td/div/img[2]"
	def f顶栏顺序(self, a序号0: int):
		if a序号0 in self.m顶栏字典:
			return self.m顶栏字典[a序号0]
		else:
			v顺序 = len(self.m顶栏字典) + 1
			self.m顶栏字典[a序号0] = v顺序
			return v顺序
	def f侧栏中间顺序字符(self, a序号0):
		v顶栏顺序 = self.f顶栏顺序(a序号0)
		if len(self.m顶栏字典) <= 1:
			return ""
		else:
			return f"[{v顶栏顺序}]"
class C设备_a(C设备, C模式路径_a):
	"""适用于: 山石SG-6000-A5100(v5.5)"""
	def __init__(self, a连接, a型号, a版本):
		C设备.__init__(self, a连接, a型号, a版本)
		C模式路径_a.__init__(self)
	#模式
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式_a(self)
