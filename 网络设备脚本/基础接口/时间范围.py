import enum
class E日子(enum.IntEnum):
	e一 = 0
	e二 = 1
	e三 = 2
	e四 = 3
	e五 = 4
	e六 = 5
	e日 = 6
	e工作日 = 8
	e周末 = 9
	e每天 = 7
class S时间范围:
	def __init__(self, a开始时间, a结束时间):
		self.m绝对 = True
		self.m开始时间 = a开始时间
		self.m结束时间 = a结束时间
	@staticmethod
	def fc定期(a日子, a开始时间, a结束时间):
		"""
		a日子: E日子\n
		a开始时间: str, tuple(时, 分)\n
		a结束时间: str, tuple(时, 分)
		"""
		v = S时间范围(a开始时间, a结束时间)
		v.m绝对 = False
		v.m日子 = a日子
		return v
	@staticmethod
	def fc绝对(a开始时间, a结束时间):
		v = S时间范围(a开始时间, a结束时间)
		return v
class I时间范围配置:
	def fs值(self, a时间范围, a操作):
		raise NotImplementedError()
