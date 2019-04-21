import time
import cflw网络连接 as 连接
import cflw网络设备_华为 as 华为
ca设备信息 = [
	("ensp.localhost", 2000, 华为.E型号.ar201),
	("ensp.localhost", 2001, 华为.E型号.ar201),
	("ensp.localhost", 2002, 华为.E型号.ar201),
	("ensp.localhost", 2003, 华为.E型号.ar201),
]
def main():
	#初始化
	va设备 = []
	for v设备信息 in ca设备信息:
		v连接 = 连接.C网络终端(v设备信息[0], v设备信息[1])
		v设备 = 华为.f创建设备(v连接, v设备信息[2])
		va设备.append(v设备)
		v用户 = v设备.f模式_用户()
		v设备.m设备名称 = v用户.f显示_设备名称()
	#开始监视
	va状态 = {}
	print("开始监视")
	while True:
		for v设备 in va设备:
			v用户 = v设备.f模式_用户()
			v接口表 = v用户.f显示_接口表()
			for v行 in v接口表.fe行():
				v接口名称 = str(v行.m接口)
				v键 = (v设备, v接口名称)
				if v键 in va状态:
					v状态 = va状态[v键]
					if v行.m状态 != v状态:
						print("状态变化: %s/%s %s->%s" % (v设备.m设备名称, v接口名称, v状态, v行.m状态))
				va状态[v键] = v行.m状态
		time.sleep(0.5)
if __name__ == "__main__":
	main()