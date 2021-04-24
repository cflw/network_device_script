from ..基础接口 import 设备模式
from ..命令行接口 import 模式
from . import 系统信息
from . import 硬件信息
class C设备显示v5(设备模式.I设备显示, 模式.I显示模式):
	"""适用于:"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#硬件
	def f显示_设备名(self):
		v输出 = self.m设备.f执行命令("display current-configuration | include sysname", a等待 = 5)
		return C输出分析.f从配置取设备名称(v输出)
	def f显示_温度(self):
		v输出 = self.m设备.f执行命令("display environment", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出, p尾行 = 2, a转列表 = True)
		v输出 = v输出[3:]
		v字典 = dict()
		for v in v输出:
			v槽位 = int(v[1:5])
			v温度 = int(v[17:27])
			v字典[v槽位] = v温度
		return v字典
	#系统
	def f显示_中央处理器利用率(self):
		"返回字典，键=槽位，值=5分钟利用率"
		v输出 = self.m设备.f执行命令("display cpu-usage", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出, a转列表 = True)
		print(v输出)
		v字典 = dict()
		i = 0
		while i < len(v输出):
			v槽位 = int(C实用工具.f取数字(v输出[i])[0])
			v利用率 = int(C实用工具.f取数字(v输出[i+3])[0])
			v字典[v槽位] = v利用率
			i += 5
		return v字典
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行命令("display memory")
		v输出 = 南向设备.f去头尾行(v输出, a转列表 = True)
		return 南向设备.f取数字(v输出[3])[0]
	def f显示_设备版本(self):	#需要重写
		v输出 = self.m设备.f执行命令("display version", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出, a转列表 = True)
		v字典 = dict()
		v字典["版本号"] = v输出[1][26:29]
		v字典["发行号"] = v输出[1][40:43]
		v字典["版权"] = v输出[2]
		v第四行分段 = v输出[3].split(" ")
		v字典["平台"] = v第四行分段[0] + " " + v第四行分段[1]
		v字典["更新时间"] = 南向设备.f时间(v第四行分段[4], v第四行分段[6], v第四行分段[8], v第四行分段[10])
		return v字典