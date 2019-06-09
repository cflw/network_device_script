from selenium import webdriver
import 网络设备脚本.水星 as 水星
def main():
	v连接 = webdriver.Firefox()
	v连接.get("http://192.168.1.254")
	print("开始")
	v设备 = 水星.f创建设备(v连接, 水星.E型号.mw155r)
	v用户 = v设备.f模式_用户()
	v用户.f登录(a密码 = "12345678")
	v全局配置 = v用户.f模式_全局配置()
	v静态路由 = v全局配置.f模式_静态路由()
	# for v路由 in v静态路由.f显示_路由表():
	# 	print(v路由)
	v静态路由.fs路由("192.168.10.0/24", "192.168.1.1")
	print("结束")
if __name__ == "__main__":
	main()