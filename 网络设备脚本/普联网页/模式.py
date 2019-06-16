import enum
class C模式wdr5620:
	"""适用于: wdr5620"""
	c网络状态 = ("netStateMbtn",)
	c设备管理 = ("routeMgtMbtn",)
	c设备管理_主人网络 = ("routeMgtMbtn", "linkedEpt_rsMenu")
	c设备管理_已禁设备 = ("routeMgtMbtn", "limitedEpt_rsMenu")
	c应用管理 = ("appsMgtMbtn",)
	c路由设置 = ("routerSetMbtn",)
	c路由设置_tplinkid = ("routerSetMbtn", "cloudAnt_rsMenu")
	c路由设置_上网设置 = ("routerSetMbtn", "network_rsMenu")
	c路由设置_无线设置 = ("routerSetMbtn", "wireless2G_rsMenu")
	c路由设置_lan口设置 = ("routerSetMbtn", "lanSet_rsMenu")
	c路由设置_dhcp服务器设置 = ("routerSetMbtn", "dhcpServer_rsMenu")
	c路由设置_修改管理员密码 = ("routerSetMbtn", "changeWebPwd_rsMenu")
	c路由设置_备份和载入配置 = ("routerSetMbtn", "bakRrestore_rsMenu")
	c路由设置_重启和恢复出厂 = ("routerSetMbtn", "reBootSet_rsMenu")
	c路由设置_系统日志 = ("routerSetMbtn", "sysLog_rsMenu")