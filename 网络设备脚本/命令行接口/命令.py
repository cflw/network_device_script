import copy
class C命令:	#快速添加命令参数
	def __init__(self, *t):
		self.m字符串 = ""
		self.f添加(*t)
	def __eq__(self, a):
		if type(a) != C命令:
			return False
		return self.m字符串 == a.m字符串
	def __add__(self, a):
		v命令 = copy.copy(self)
		v命令 += a
		return v命令
	def __iadd__(self, a):
		v类型 = type(a)
		if v类型 in (tuple, list):
			self.f添加(*a)
		else:
			self.f添加(a)
		return self
	def __radd__(self, a):
		v命令 = copy.copy(self)
		v类型 = type(a)
		if v类型 in (tuple, list):
			v命令.f前面添加(*a)
		else:
			v命令.f前面添加(a)
		return v命令
	def __str__(self):
		return self.m字符串
	def f添加(self, *a):
		for v in a:
			if self.m字符串 and self.m字符串[-1] != ' ':	#添加空格
				self.m字符串 += " "
			self.m字符串 += str(v)
		return self
	def f前面添加(self, *a):
		if not a:
			raise TypeError()
		for v in a:
			v命令 = str(v)
			if v命令[-1] == ' ':
				self.m字符串 = v命令 + self.m字符串
			else:
				self.m字符串 = v命令 + " " + self.m字符串
		return self
	def f前置肯定(self, a判断: bool, a命令):
		"如果判断为真则添加命令"
		if a判断:
			self.f前面添加(a命令)
		return self
	def f前置否定(self, a判断: bool, a命令):
		"如果判断为假则添加命令"
		if not a判断:
			self.f前面添加(a命令)
		return self
	def f复制(self):
		return copy.copy(self)
def F检测命令异常(a列表):
	def f检测命令异常(self, a输出):
		def f返回异常(ax):
			if type(ax) == type:
				v异常 = ax(a输出)
			else:
				v异常 = ax
			if self.m异常开关:
				raise v异常
			return v异常
		for v文本, vt异常 in a列表:
			if v文本 in a输出:
				return f返回异常(vt异常)
		return None
	return f检测命令异常
