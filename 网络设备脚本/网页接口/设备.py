import time
from ..基础接口 import 设备
from . import 元素
class I设备(设备.I设备):
	"支持selenium库的网页设备"
	def __init__(self, a连接):
		self.m连接 = a连接
		self.m查找缓冲 = ""
		self.m元素缓冲 = None
	def fs地址(self, a地址):
		self.m连接.get(a地址)
		time.sleep(0.1)
	def fg地址(self):
		"返回统一资源定位符"
		return self.m连接.current_url
	def f查找(self, a找: str, a包装 = True):
		if self.m查找缓冲 == a找:
			return 元素.f包装(self.m元素缓冲, a包装)
		self.m元素缓冲 = self.m连接.find_element_by_xpath(a找)
		if self.m元素缓冲:
			self.m元素缓冲 = 元素.C元素(self.m元素缓冲)
		return 元素.f包装(self.m元素缓冲, a包装)
	def fe查找(self, a找: str, a包装 = True):
		f包装0 = 元素.F包装(a包装)
		for v元素 in self.m连接.find_elements_by_xpath(a找):
			yield f包装0(v元素)
	def f等待载入完成(self):
		time.sleep(1)