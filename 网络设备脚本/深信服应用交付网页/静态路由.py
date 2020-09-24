import time
import pandas	#pandas
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 静态路由
from ..基础接口 import 路由
from ..基础接口 import 数据表
from . import 模式
def f解析路由条目(a元素):	#div
	"""适用于: ad 7.0.8"""
	#选择	名称	网络号	掩码/前缀	网关地址	网关状态	权重	支持重分发	网关健康检查	启/禁用	操作
	v选择s, v名称s, v网络号s, v掩码前缀s, v网关地址s, v网关状态s, v权重s, v支持重分发s, v网关健康检查s, v启禁用s, v操作s = map(lambda x: x.fg文本(), a元素.fe查找("td"))
	return {
		数据表.E字段.e目标路由类型: 路由.E路由类型.e静态,
		数据表.E字段.e目标网络号: 地址.S网络地址4.fc地址前缀长度(v网络号s, int(v掩码前缀s)),
		数据表.E字段.e目标下一跳: 地址.S网络地址4.fc地址前缀长度(v网关地址s, 32),
		数据表.E字段.e目标度量值: int(v权重s),
	}
class C静态路由ad705(静态路由.I静态路由配置):
	"""适用于: ad 7.0.8"""
	c工具栏路径 = "/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr"
	c表格路径 = "/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div"
	def __init__(self, a设备):
		self.m设备 = a设备
	def f切换到当前模式(self):
		self.m设备.f切换模式(模式.C模式ad705.c网络部署_静态路由)
	def f显示_路由表(self):
		self.f切换到当前模式()
		time.sleep(1)	#表格会一直变化,元素会失效
		w表格 = self.m设备.f查找(C静态路由ad705.c表格路径)
		def fe行():
			for w行 in map(lambda x: x.f查找("table/tbody/tr"), w表格.fe查找("div")):
				yield f解析路由条目(w行)
		return pandas.DataFrame(fe行())