import time
import selenium.webdriver	#selenium
#包装元素类
class C元素:
	"""对selenium网页元素的封装"""
	def __init__(self, a元素):
		self.m元素 = a元素
	def f查找(self, a找, a包装 = True):
		return f包装(self.m元素.find_element_by_xpath(a找), a包装)
	def fe查找(self, a找, a包装 = True):
		f包装0 = F包装(a包装)
		for v元素 in self.m元素.find_elements_by_xpath(a找):
			yield f包装0(v元素)
	def f点击(self):
		self.m元素.click()
		time.sleep(0.1)
	def f清除(self):
		self.m元素.clear()
		time.sleep(0.1)
	def f输入(self, a, a清除 = True):
		if a清除:
			self.m元素.clear()
		self.m元素.send_keys(a)
		time.sleep(0.1)
	def f下拉选择(self, a索引):
		s = selenium.webdriver.support.select.Select(self.m元素)
		s.select_by_index(a索引)
		time.sleep(0.1)
	def fg文本(self):
		return self.m元素.text
#包装函数
def f有包装(a元素):
	return a元素 if type(a元素) == C元素 else C元素(a元素)
def f没包装(a元素):
	return a元素.m元素 if type(a元素) == C元素 else a元素
def F包装(a包装: bool):
	return f有包装 if a包装 else f没包装
def f包装(a元素, a包装: bool = True):
	if type(a元素) == C元素:
		return a元素 if a包装 else a元素.m元素
	else:	#selenium的原始元素类型
		return C元素(a元素) if a包装 else a元素