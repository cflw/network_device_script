import cflw代码库py.cflw网络连接 as 连接
import 网络设备脚本.华为 as 华为
def main():
	#连接到设备,取配置
	v连接 = 连接.C网络终端("ensp.localhost", 2000)
	v设备 = 华为.f创建设备(v连接, 华为.E型号.ar201)
	v用户 = v设备.f模式_用户()
	v配置 = str(v用户.f显示_当前配置())
	print(v配置)
	#保存
	v文件 = open("d:/test/a.txt", "w")
	v文件.write(v配置)
	print("结束")
if __name__ == "__main__":
	main()