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
	def f聚焦(self):
		"先用点击代替"
		self.m元素.click()
	def f选中(self, a选中 = True):
		"""选中复选框,单选框"""
		vi选中 = self.m元素.is_selected()
		if vi选中 != a选中:
			self.m元素.click()
		time.sleep(0.1)
	#取属性
	def fg文本(self):
		if self.m元素.tag_name in ("input",):	#表单控件从值属性取文本
			return self.m元素.get_attribute("value")
		return self.m元素.text
	def fg属性(self, a属性名):
		return self.m元素.get_attribute(a属性名)
	def fg标识(self):
		return self.m元素.get_attribute("id")
	def fg类名(self):
		return self.m元素.get_attribute("class")
	def fg矩形(self):
		x = self.m元素.localtion["x"]
		y = self.m元素.localtion["y"]
		v宽 = self.m元素.localtion["width"]
		v高 = self.m元素.localtion["height"]
		return x, y, x + v宽, y + v高
	def fi选中(self):
		return self.m元素.is_selected()
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