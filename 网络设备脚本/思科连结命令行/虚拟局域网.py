import pandas
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 数据表
from . import 接口 as 实现接口
class C表nv7:	#需重写
	"""show vlan
	适用于: 浪潮cn8000系列(v7.3)"""
	c号 = 0
	c名称 = 5
	c状态 = 38
	c端口 = 48
	ca列开始 = (c号, c名称, c状态, c端口)
	c标题行0 = "VLAN Name                             Status    Ports"
	c标题行1 = "---- -------------------------------- --------- -------------------------------"
	def __init__(self, a文本):
		v位置 = 字符串.f连续找最后(a文本, C表nv7.c标题行0, C表nv7.c标题行1, "\n")
		self.m文本 = a文本[v位置 + 1 :]
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		v虚拟局域网 = None
		va接口 = []
		v接口缓冲 = {}
		for v行 in self.m文本.split("\n"):
			v虚拟局域网s, v名称s, v状态s, v端口s = 字符串.fe按位置分割(v行, *C表nv7.ca列开始)
			if v虚拟局域网s.isdigit():	#开始
				if v虚拟局域网:
					yield {
						数据表.E字段.e本端虚拟局域网: v虚拟局域网,
						数据表.E字段.e本端接口: va接口,
					}
				v虚拟局域网 = int(v虚拟局域网s)
				va接口 = []
			elif not v虚拟局域网s:	#空的
				pass
			else:	#其它字符
				break
			for v接口s in v端口s.split(","):
				v接口s = v接口s.strip()
				if v接口s in v接口缓冲:
					va接口.append(v接口缓冲[v接口s])
				else:
					v接口 = 实现接口.f创建接口缩写nv7(v接口s)
					v接口缓冲[v接口s] = v接口
					va接口.append(v接口)
		if v虚拟局域网:
			yield {
				数据表.E字段.e本端虚拟局域网: v虚拟局域网,
				数据表.E字段.e本端接口: va接口,
			}
def f虚拟局域网nv7(a文本: str):	#需重写
	v表 = C表nv7(a文本)
	return pandas.DataFrame(v表.fe行())