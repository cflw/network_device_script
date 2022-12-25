import time
from selenium.common import exceptions #selenium
from selenium.webdriver.common.by import By	#selenium
from ..基础接口 import 设备
from . import 元素
import cflw代码库py.cflw时间 as 时间
import cflw代码库py.cflw工具_运算 as 运算
class I设备(设备.I设备):
	"封装selenium库的网页设备类"
	def __init__(self, a连接):
		self.m连接 = a连接
		self.m连接.implicitly_wait(8)	#互联网8秒定律
	def fs地址(self, a地址):
		self.m连接.get(a地址)
		time.sleep(0.1)
	def fg地址(self):
		"返回统一资源定位符"
		return self.m连接.current_url
	def f查找(self, a找: str, a包装 = True):
		time.sleep(0.1)
		try:
			v元素 = self.m连接.find_element(By.XPATH, a找)
			return 元素.f包装(v元素, a包装)
		except exceptions.NoSuchElementException as e:
			return None
	def f查找_直到(self, a找, af条件 = 运算.f总是真, a超时: float = 10, a包装: bool = True):
		v计时 = 时间.C循环阻塞(a超时)
		while v计时.f滴答():
			if v元素 := self.f查找(a找, a包装):
				if af条件(v元素):
					return v元素
		return None
	def fe查找(self, a找: str, a包装 = True):
		f包装0 = 元素.F包装(a包装)
		for v元素 in self.m连接.find_elements(By.XPATH, a找):
			yield f包装0(v元素)
	def f等待存在(self, a找, a超时 = 10):
		v计时 = 时间.C循环阻塞(a超时)
		while v计时.f滴答():
			if self.f查找(a找):
				return
	def f等待不存在(self, a找, a超时 = 10):
		v计时 = 时间.C循环阻塞(a超时)
		while v计时.f滴答():
			if not self.f查找(a找):
				return