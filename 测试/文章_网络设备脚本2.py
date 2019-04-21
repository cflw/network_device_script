import cflw网络连接 as 连接
import cflw网络地址 as 地址
import cflw网络设备 as 设备
import cflw网络设备_思科 as 思科
import cflw网络设备_华为 as 华为
import cflw网络设备_华三 as 华三

def main():
	v连接 = 连接.C网络终端("gns3.localhost", 5000)
	v设备 = 思科.f创建设备(v连接, 思科.E型号.c7200, 15.2)
	v设备.fs回显(True)
	#用户
	v用户模式 = v设备.f模式_用户()
	v用户模式.f显示_时间()
	#全局配置
	v全局配置 = v用户模式.f模式_全局配置()
	#接口配置f0/0
	v接口配置 = v全局配置.f模式_接口配置("f0/0")
	v接口配置.fs网络地址4("12.0.0.1/24")
	v接口配置.f开关(True)
	v接口配置.f显示_当前模式配置()
	#用户配置
	v用户配置 = v全局配置.f模式_用户配置("asdf")
	v用户配置.fs密码("123456")
	v用户配置.f显示_当前模式配置()
	#结束
	v用户模式.f显示_时间()

if __name__ == "__main__":
	main()