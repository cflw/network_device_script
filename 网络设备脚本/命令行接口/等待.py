import time
c超时 = 2
class I等待:
	def __init__(self, a超时 = c超时):
		self.m超时 = a超时
		self.m间隔 = a超时 / 10
		self.m计时 = 0
	def f继续等待(self):
		self.m计时 += self.m间隔
		time.sleep(self.m间隔)
	def f重置计时(self):
		self.m计时 = 0
	def fi未超时(self):
		return self.m计时 < self.m超时
	def fi超时(self):
		"""如果超时则无视结束条件强制恢复"""
		return self.m计时 >= self.m超时
	def fi结束(self, a接收: str):
		"""判断接收到的数据,决定是否继续等待或结束."""
		raise NotImplementedError()
class C无(I等待):	#不等待,立即恢复
	def fi结束(self, a接收):
		return True
class C固定(I等待):	#固定等待一段时间
	def fi结束(self, a接收):
		return False
class C短(I等待):	#有输出则恢复,否则等到到超时
	def fi结束(self, a接收):
		return bool(a接收)
class C长(I等待):	#有输出重置等待时间,直到没输出为止
	def fi结束(self, a接收):
		if bool(a接收):
			self.f重置计时()
			return False
		return True
class C直到(I等待):	#出现指定词立即恢复
	def __init__(self, a指定词, a超时 = c超时):
		I等待.__init__(self, a超时)
		self.m指定词 = a指定词
	def fi结束(self, a接收):
		return self.m指定词 in a接收
class C命令(I等待):	#首次是时间较长的长等待,后面是时间较短的短等待.用来解决命令执行时间过长时等待时间不等的问题
	def __init__(self, a超时 = c超时, a首次超时 = c超时 * 5):
		I等待.__init__(self, a首次超时)
		self.m首次超时 = a首次超时
		self.m再次超时 = a超时
	def f重置计时(self):
		self.m计时 = 0
		self.m超时 = self.m首次超时
	def fi结束(self, a接收):
		if bool(a接收):
			self.m计时 = 0
			self.m超时 = self.m再次超时
			return False
		return True
def f解析等待(a)->I等待:
	v类型 = type(a)
	if issubclass(v类型, I等待):
		return a
	elif v类型 == bool:
		return C长()
	elif v类型 in (int, float):
		return C长(a)
	else:
		raise TypeError("无法识别的类型")