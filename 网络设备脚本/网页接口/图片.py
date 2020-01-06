import io
import tkinter
import PIL.Image	#pillow
import cflw代码库py.cflw时间 as 时间
from . import 元素
def f取元素图片(a设备, a元素):
	v数据 = a设备.get_screenshot_as_png()
	v输入 = io.BytesIO(v数据)
	v图片 = PIL.Image.open(v输入)
	v图片.crop(a元素.fg矩形())
	return v图片
def f手动输入验证码(a元素, a长度):
	"""使验证码输入框获得焦点,让用户输入验证码"""
	v元素 = 元素.f包装(a元素)
	v元素.f聚焦()
	v循环阻塞 = 时间.C循环阻塞(60, a间隔 = 1)
	while v循环阻塞.f滴答():
		if len(v元素.fg文本()) >= a长度:	#有输入
			return True
	else:	#没有输入
		return False
def f处理验证码(a图片):
	"""显示验证码并提示输入,返回输入的内容"""
	raise NotImplementedError()