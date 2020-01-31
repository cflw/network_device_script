from ..命令行接口 import 全局显示
class C全局显示(全局显示.I全局显示):
	#显示设备状态
	def f显示_时间(self):
		v命令 = 命令.C命令("display clock")
		v输出 = self.m设备.f执行显示命令(v命令)	#15:14:12 UTC Tue 04/16/2019
		#过滤时区
		v空格位置 = 字符串.f全部找(v输出, " ")
		v行结束 = v输出.find("\n")
		if v行结束 > 0:	#如果有换行符,截取到行结束
			v输出 = v输出[0:v空格位置[0]] + v输出[v空格位置[1]:v行结束]
		else:	#如果没有换行符,截取到字符串结束
			v输出 = v输出[0:v空格位置[0]] + v输出[v空格位置[1]:]	#12:06:32 Wed 04/26/2000
		v时间 = time.strptime(v输出, "%H:%M:%S %a %m/%d/%Y")
		return v时间
	def f显示_版本(self):
		raise NotImplementedError()
	def f显示_当前配置(self):
		v输出 = self.f执行命令("display current-configuration", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出)
		return C配置信息(v输出)
	def f显示_设备名称(self):
		v输出 = self.f执行命令("display current-configuration | include sysname", a等待 = 5)
		return C输出分析.f从配置取设备名称(v输出)
	def f显示_设备版本(self):	#需要重写
		v输出 = self.f执行命令("display version", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出, a转列表 = True)
		v字典 = dict()
		v字典["版本号"] = v输出[1][26:29]
		v字典["发行号"] = v输出[1][40:43]
		v字典["版权"] = v输出[2]
		v第四行分段 = v输出[3].split(" ")
		v字典["平台"] = v第四行分段[0] + " " + v第四行分段[1]
		v字典["更新时间"] = 南向设备.f时间(v第四行分段[4], v第四行分段[6], v第四行分段[8], v第四行分段[10])
		return v字典
	def f显示_中央处理器利用率(self):
		"返回字典，键=槽位，值=5分钟利用率"
		v输出 = self.f执行命令("display cpu-usage", a自动换页 = True)
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
		v输出 = self.f执行命令("display memory")
		v输出 = 南向设备.f去头尾行(v输出, a转列表 = True)
		return 南向设备.f取数字(v输出[3])[0]
	def f显示_温度(self):
		v输出 = self.f执行命令("display environment", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出, p尾行 = 2, a转列表 = True)
		v输出 = v输出[3:]
		v字典 = dict()
		for v in v输出:
			v槽位 = int(v[1:5])
			v温度 = int(v[17:27])
			v字典[v槽位] = v温度
		return v字典
	def f显示_运行时间(self):
		raise NotImplementedError()
	def f显示_开机日期(self):
		raise NotImplementedError()
	def f显示_序列号(self):
		raise NotImplementedError()
	def f显示_出厂日期(self):
		raise NotImplementedError()
	#显示程序状态
	def f显示_路由表(self):
		v输出 = self.f执行命令("display ip routing-table", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出, a转列表 = True)
	def f显示_默认路由(self):
		v输出 = self.f执行命令("display ip routing-table 0.0.0.0")
		v输出 = 南向设备.f去头尾行(v输出, a转列表 = True)
		v输出 = v输出[5]
		return (ipaddress.IPv4Network("0.0.0.0/0"), v输出[20:25], int(v输出[27:30]), int(v输出[32:42]), ipaddress.IPv4Address(v输出[45:61]), v输出[61:70])
	def f显示_链路层发现协议(self):
		v输出 = self.f执行命令("display lldp neighbor-information", a自动换页 = True)
