import copy
from ..基础接口 import 操作
from ..基础接口 import 异常
#===============================================================================
# 命令类
#===============================================================================
class C命令:	#快速添加命令参数
	def __init__(self, *a文本):
		self.m字符串 = ""
		self.f添加(*a文本)
	def __eq__(self, a):
		v类型 = type(a)
		if v类型 == C命令:
			return self.m字符串 == a.m字符串
		elif v类型 == str:
			return self.m字符串 == a
		else:
			return False
	def __add__(self, a):
		"添加"
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
	def __sub__(self, a):
		"附(负)加"
		v命令 = copy.copy(self)
		v命令 -= a
		return v命令
	def __isub__(self, a):
		v类型 = type(a)
		if v类型 in (tuple, list):
			self.f附加(*a)
		else:
			self.f附加(a)
		return self
	def __rsub__(self, a):
		v命令 = copy.copy(self)
		v类型 = type(a)
		if v类型 in (tuple, list):
			v命令.f前面附加(*a)
		else:
			v命令.f前面附加(a)
		return v命令
	def __ior__(self, a: tuple):
		"""添加参数(或加,有实参才添加)
		用法: v命令 |= "-l", v用户名"""
		self.f添加参数(*a)
		return self
	def __str__(self):
		return self.m字符串
	def __repr__(self):
		return f"\"{self.m字符串}\""
	def __bool__(self):
		return bool(self.m字符串)
	def __len__(self):
		return len(self.m字符串)
	def f添加(self, *a):
		"{m字符串}(空格){a字符串}"
		for v in a:
			if v == None:
				continue
			v命令 = str(v)
			if not v命令:
				continue
			if self.m字符串 and self.m字符串[-1] != ' ':	#添加空格
				self.m字符串 += " "
			self.m字符串 += v命令
		return self
	def f添加参数(self, *a):
		"有实参则添加"
		if a[-1]:
			self.f添加(*a)
		return self
	def f前面添加(self, *a):
		"{a字符串}(空格){m字符串}"
		if not a:
			raise TypeError()
		for v in a:
			if v == None:
				continue
			v命令 = str(v)
			if not v命令:
				continue
			elif v命令[-1] == ' ' or self.m字符串[0] == ' ':
				self.m字符串 = v命令 + self.m字符串
			else:
				self.m字符串 = v命令 + " " + self.m字符串
		return self
	def f附加(self, *a):
		"{m字符串}{a字符串}"
		for v in a:
			if v == None:
				continue
			self.m字符串 += str(v)
		return self
	def f前面附加(self, *a):
		"{a字符串}{m字符串}"
		if not a:
			raise TypeError()
		for v in a:
			if v == None:
				continue
			self.m字符串 = str(v) + self.m字符串
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
#===============================================================================
# 检测命令异常
#===============================================================================
def F检测命令异常(a列表):
	def f检测命令异常(self, a输出):
		if not self.m检测异常:
			return
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
#===============================================================================
# 命令函数
#===============================================================================
def f命令补全(a, *a元组):
	v匹配程度 = 0
	v匹配字符串 = ''
	for v字符串 in a元组:
		v当前匹配程度 = 0
		for i in range(min(len(a), len(v字符串))):
			if a[i] == v字符串[i]:
				v当前匹配程度 += 1
			else:
				break
		if v当前匹配程度 > v匹配程度:
			v匹配程度 = v当前匹配程度
			v匹配字符串 = v字符串
	return v匹配字符串
def F生成开关命令(a命令, ai开命令, a不):
	if ai开命令:
		def f(a操作):
			v命令 = C命令(a命令)
			v操作 = 操作.f解析操作(a操作)
			if 操作.fi开操作(v操作):
				pass
			elif 操作.fi关操作(v操作):
				v命令.f前面添加(a不)
			else:
				raise 异常.X操作()
			return v命令
	else:
		def f(a操作):
			v命令 = C命令(a命令)
			v操作 = 操作.f解析操作(a操作)
			if 操作.fi开操作(v操作):
				v命令.f前面添加(a不)
			elif 操作.fi关操作(v操作):
				pass
			else:
				raise 异常.X操作()
			return v命令
	return f
def F生成描述命令(a命令, a不):
	def f(a描述, a操作):
		v命令 = C命令(a命令)
		v操作 = 操作.f解析操作(a操作)
		if v操作 == 操作.E操作.e设置:
			v命令 += a描述
		elif v操作 == 操作.E操作.e删除:
			v命令.f前面添加(a不)
	return f