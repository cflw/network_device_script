from ..基础接口 import 设备
from . import 元素
class I设备(设备.I设备):
	"支持selenium库的网页设备"
	def __init__(self, a连接):
		self.m连接 = a连接
		self.m查找缓冲 = ""
		self.m元素缓冲 = None
	def f查找(self, a找: str, a包装 = True):
		if self.m查找缓冲 == a找:
			return 元素.f包装(a包装, self.m元素缓冲)
		self.m元素缓冲 = self.m连接.find_element_by_xpath(a找)
		if self.m元素缓冲:
			self.m元素缓冲 = 元素.C元素(self.m元素缓冲)
		return 元素.f包装(a包装, self.m元素缓冲)