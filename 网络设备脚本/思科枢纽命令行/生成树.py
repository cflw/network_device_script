import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 数据表
from ..基础接口 import 生成树 as 北向生成树
from . import 接口 as 实现接口
ca端口角色nv7 = {
	"Root": 北向生成树.E端口角色.e根,
	"Desg": 北向生成树.E端口角色.e指定,
}
ca端口状态nv7 = {
	"FWD": 北向生成树.E端口状态.e转发,
}
class C接口表nv7:
	"""show spanning-tree
	show spanning-tree brief
	适用于: 浪潮cn8000系列(v7.3)"""
	c接口 = 0
	c角色 = 17
	c状态 = 22
	c开销 = 26
	c优先级 = 36
	c类型 = 45
	ca列开始 = (c接口, c角色, c状态, c开销, c优先级, c类型)
	c标题行0 = "Interface        Role Sts Cost      Prio.Nbr Type"
	c标题行1 = "---------------- ---- --- --------- -------- --------------------------------"
	def __init__(self, a文本):
		self.m文本 = a文本
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		v虚拟局域网 = None
		for v行 in self.m文本.split("\n"):
			if v行[:4] == "VLAN":	#VLAN0001
				v虚拟局域网 = int(v行[4:])
			if len(v行) < 46:
				continue
			if not v行[C接口表nv7.c开销].isdigit():
				continue
			if not all(v行[i] == " " for i in (16, 21, 25, 35, 44)):
				continue
			v接口s, v角色s, v状态s, v开销s, v优先级s, v类型s = 字符串.fe按位置分割(v行, *C接口表nv7.ca列开始)
			v接口 = 实现接口.f创建接口缩写nv7(v接口s)
			v端口角色 = ca端口角色nv7[v角色s]
			v端口状态 = ca端口状态nv7[v状态s]
			yield 数据表.C记录({
				数据表.E字段.e本端生成树实例: v虚拟局域网,
				数据表.E字段.e本端接口: v接口,
				数据表.E字段.e本端生成树角色: v端口角色,
				数据表.E字段.e本端生成树状态: v端口状态,
			})