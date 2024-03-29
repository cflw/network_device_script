import collections
import pathlib
import xml.etree.ElementTree as ET
S模式 = collections.namedtuple("S模式", ["m序号", "m名称", "m路径"])
def f创建模式树(a模式栈: tuple, a序号: int, a父: ET.Element):
	#模式栈为父级的元素:(序号, 元素)
	#返回树状结构,每个节点包含(S模式, [子节点])
	v子侧栏 = False
	va子节点 = []
	if len(a父) > 0:
		v子序号 = 0
		for v子 in a父:
			v子模式栈 = a模式栈 + ((a序号, a父),)
			v子节点 = f创建模式树(v子模式栈, v子序号, v子)
			va子节点.append(v子节点)
			v子侧栏 |= v子.get("名称") == "侧栏"
			v子序号 += 1
	v名称 = a父.get("名称")
	match a父.tag:
		case "模式":	#根
			return S模式(a序号, v名称, None), va子节点
		case "顶栏":
			v路径 = f"/html/body/div[1]/div[2]/span[{a序号+1}]"
			return S模式(a序号, v名称, v路径), va子节点
		case "侧栏":
			if v子侧栏:
				return S模式(a序号, v名称, None), va子节点
			else:	#这是最后一级侧栏,创建侧栏模式
				va侧栏序号 = []
				v侧栏层级 = 1
				for v序号, v元素 in a模式栈[2:]:
					va侧栏序号.append(v序号)
					v侧栏层级 += 1
				match v侧栏层级:
					case 1:
						v路径 = f"/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/ul/li[{a序号+1}]/a/em"
					case 2:
						v路径 = f"/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/ul/li[{va侧栏序号[0]+1}]/ul/li[{a序号+1}]/a/em"
					case 3:
						v路径 = f"/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/ul/li[{va侧栏序号[0]+1}]/ul/li[{va侧栏序号[1]+1}]/ul/li[{a序号+1}]/a"
					case _:
						raise ValueError("侧栏层级错误")
				return S模式(a序号, v名称, v路径), va子节点
		case "标签栏":
			v路径 = f"/html/body/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/ul/li[{a序号+1}]/a[2]/em/span/span"
			return S模式(a序号, v名称, v路径), va子节点
		case "工具栏":
			v路径 = f"/html/body/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[{a序号+1}]/table/tbody/tr[2]/td[2]/em/button/span"
			return S模式(a序号, v名称, v路径), va子节点
		case _:
			raise ValueError("标签名错误")
def f创建模式类(a模式树):
	v对象 = type("C模式_af8035", (object,), {})()	#创建空白对象
	def f创建模式类0(a模式树0, a常量名称0, a模式栈0):
		v模式, va子节点 = a模式树0
		#添加属性
		if v模式.m名称:	#子
			v常量名称 = a常量名称0 + v模式.m名称
		else:
			v常量名称 = a常量名称0
		if v模式.m路径:
			v模式栈 = a模式栈0 + (v模式,)
			setattr(v对象, v常量名称, v模式栈)
		else:	#没有路径,说明不用点击,跳过
			v模式栈 = a模式栈0
		#遍历子节点
		if len(v模式栈) > 0:
			v常量名称 += "_"
		for v子节点 in va子节点:
			f创建模式类0(v子节点, v常量名称, v模式栈)
	f创建模式类0(a模式树, "c", ())
	return v对象
def f创建模式():
	v模块路径 = pathlib.Path(__file__)
	v模块目录 = v模块路径.parent
	v文件名 = v模块目录 / "模式.xml"
	v树 = ET.parse(v文件名)
	v根 = v树.getroot()
	v模式树 = f创建模式树((), 0, v根)
	v对象 = f创建模式类(v模式树)
	return v对象
C模式_af8035 = f创建模式()