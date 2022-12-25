import time
import pandas	#pandas
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 无线局域网
from . import 模式
class C无线电接口配置(无线局域网.I接口配置):
	"""适用于: 普联wdr5620"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_主机表(self):
		return f主机表(self.m设备)
def f主机表(a设备):
	"""适用于: 普联wdr5620"""
	def fe主机():
		a设备.f切换模式(模式.C模式wdr5620.c设备管理)
		i = 0
		while True:
			va元素 = list(a设备.fe查找("//*[@id='eptMngList']/div[@class='eptConC']"))
			if i >= len(va元素):
				break
			v元素 = va元素[i]
			w管理 = v元素.f查找("div/div/input[1]")
			w管理.f点击()	#进入主机管理
			w详细 = a设备.f查找("//*[@id='eptMngDetail']")
			w名称 = w详细.f查找("div[1]/p/span/pre")
			v名称 = w名称.fg文本()
			w标题 = w详细.f查找("div[1]/span")
			v网络地址s, v物理地址s, v连接方式s = w标题.fg文本().split("|")	#IP：192.168.0.5 | MAC：80-CB-BC-0F-97-8F | 2.4G无线连接
			v网络地址 = 地址.S网络地址4.fc主机地址字符串(v网络地址s.strip()[3:])
			v物理地址 = 地址.S物理地址.fc字符串(v物理地址s.strip()[4:])
			v上传速度s = w详细.f查找("div[2]/ul/li[1]/p").fg文本()	#298KB/s
			v下载速度s = w详细.f查找("div[2]/ul/li[2]/p").fg文本()	#2MB/s
			yield {
				数据表.E字段.e对端名称: v名称,
				数据表.E字段.e对端网络地址4: v网络地址,
				数据表.E字段.e对端物理地址: v物理地址,
			}
			#结束,返回列表
			w主人网络 = a设备.f查找("//*[@id='linkedEpt_rsMenu']")
			w主人网络.f点击()
			i += 1
	return pandas.DataFrame(fe主机())