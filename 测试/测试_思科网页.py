import time
import selenium.webdriver	#selenium
import 网络设备脚本.思科 as 思科
def main():
	v连接 = selenium.webdriver.Firefox()
	v连接.get("http://asdf:1234@192.168.1.10")
	v设备 = 思科.f创建设备(v连接, 思科.E型号.c7200, 15.2)
	v用户模式 = v设备.f模式_用户()
	v用户模式.f登录()
	v全局配置 = v用户模式.f模式_全局配置()
	v接口配置 = v全局配置.f模式_接口("l0")
	v接口配置.fs网络地址4("1.1.1.1/24")
	v接口配置.f显示_当前模式配置()
if __name__ == "__main__":
	main()