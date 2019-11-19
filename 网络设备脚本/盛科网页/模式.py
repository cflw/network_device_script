import enum
class E模式ev6(enum.IntEnum):
	"""适用于: 浪潮s5350(v6.x)"""
	e设备概况 = enum.auto()

	e系统管理 = enum.auto()
	e系统管理_文件管理 = enum.auto()
	e系统管理_系统配置 = enum.auto()
	e系统管理_加载配置 = enum.auto()
	e系统管理_日志管理 = enum.auto()
	e系统管理_SNMP配置 = enum.auto()
	e系统管理_SNMPTrap配置 = enum.auto()

	e端口 = enum.auto()
	e端口_端口状态 = enum.auto()
	e端口_端口统计 = enum.auto()
	e端口_链路聚合 = enum.auto()
	e端口_链路聚合_全局配置 = enum.auto()
	e端口_链路聚合_端口配置 = enum.auto()
	e端口_风暴控制 = enum.auto()
	e端口_流量控制 = enum.auto()
	e端口_端口隔离 = enum.auto()
	e端口_端口隔离_全局配置 = enum.auto()
	e端口_端口隔离_端口配置 = enum.auto()
	e端口_端口监测 = enum.auto()

	e服务管理 = enum.auto()

	e服务管理_VLAN = enum.auto()
	e服务管理_VLAN_VLAN状态 = enum.auto()
	e服务管理_VLAN_VLAN添加删除 = enum.auto()
	e服务管理_VLAN_VLANIF端口 = enum.auto()
	e服务管理_VLAN_AccessTrunk端口 = enum.auto()

	e服务管理_VLAN分类 = enum.auto()
	e服务管理_VLAN分类_状态 = enum.auto()
	e服务管理_VLAN分类_规则 = enum.auto()
	e服务管理_VLAN分类_组 = enum.auto()
	e服务管理_VLAN分类_应用 = enum.auto()

	e服务管理_MAC = enum.auto()
	e服务管理_MAC_MAC地址表 = enum.auto()
	e服务管理_MAC_MAC全局配置 = enum.auto()
	e服务管理_MAC_MAC学习 = enum.auto()
	e服务管理_MAC_静态MAC地址表 = enum.auto()
	e服务管理_MAC_黑洞MAC地址表 = enum.auto()
	e服务管理_MAC_端口安全 = enum.auto()
	e服务管理_MAC_静态安全MAC地址表 = enum.auto()

	e服务管理_生成树 = enum.auto()
	e服务管理_生成树_生成树信息 = enum.auto()
	e服务管理_生成树_全局配置 = enum.auto()
	e服务管理_生成树_生成树端口 = enum.auto()
	e服务管理_生成树_MST域 = enum.auto()

	e服务管理_ERPS = enum.auto()
	e服务管理_ERPS_ERPS配置 = enum.auto()
	e服务管理_ERPS_ERPS状态 = enum.auto()

	e服务管理_端口镜像 = enum.auto()
	e服务管理_端口镜像_概况 = enum.auto()
	e服务管理_端口镜像_全局配置 = enum.auto()
	e服务管理_端口镜像_镜像配置 = enum.auto()
	e服务管理_端口镜像_远程镜像MACEscape = enum.auto()

	e组播 = enum.auto()
	e组播_IGMPSnooping功能 = enum.auto()
	e组播_IGMPSnooping信息 = enum.auto()

	eIP路由 = enum.auto()
	eIP路由_IPv4路由表 = enum.auto()
	eIP路由_IPv4静态路由 = enum.auto()

	e安全 = enum.auto()
	e安全_蠕虫攻击防护 = enum.auto()
	e安全_DDoS攻击防护 = enum.auto()
	e安全_ARP攻击防护 = enum.auto()
	e安全_当前会话 = enum.auto()
	e安全_用户管理 = enum.auto()

	e工具 = enum.auto()
	e工具_Ping = enum.auto()
	e工具_Traceroute = enum.auto()

	e重启保存 = enum.auto()
class C模式ev6:
	"""适用于: 浪潮s5350(v6.x)"""
	c设备概况 = "web_device.cgi"
	c系统管理_文件管理 = "web_file.cgi"
	c系统管理_系统配置 = "web_mgmt_set.cgi"
	c系统管理_加载配置 = "web_cfg_load.cgi"
	c系统管理_日志管理 = "web_log.cgi"
	c系统管理_SNMP配置 = "web_snmp.cgi"
	c系统管理_SNMPTrap配置 = "web_trap.cgi"
	c端口_端口状态 = "web_interface.cgi"
	c端口_端口统计 = "web_interface_stats.cgi"
	c端口_链路聚合_全局配置 = "web_linkagg_glb.cgi"
	c端口_链路聚合_端口配置 = "web_linkagg.cgi"
	c端口_风暴控制 = "web_ratelimit.cgi"
	c端口_流量控制 = "web_flowcontrol.cgi"
	c端口_端口隔离_全局配置 = "web_port_isolate_glb.cgi"
	c端口_端口隔离_端口配置 = "web_port_isolate.cgi"
	c端口_端口监测 = "web_errdisable.cgi"
	c服务管理_VLAN_VLAN状态 = "web_vlan.cgi"
	c服务管理_VLAN_VLAN添加删除 = "web_vlan_add_del.cgi"
	c服务管理_VLAN_VLANIF端口 = "web_vlan_if.cgi"
	c服务管理_VLAN_AccessTrunk端口 = "web_vlan_port.cgi"
	c服务管理_VLAN分类_状态 = "web_vlan_class.cgi"
	c服务管理_VLAN分类_规则 = "web_vlan_class_add_rule.cgi"
	c服务管理_VLAN分类_组 = "web_vlan_class_add_group.cgi"
	c服务管理_VLAN分类_应用 = "web_vlan_class_add_interface.cgi"
	c服务管理_MAC_MAC地址表 = "web_macaddr_tbl.cgi"
	c服务管理_MAC_MAC全局配置 = "web_mac_glb.cgi"
	c服务管理_MAC_MAC学习 = "web_mac_learning.cgi"
	c服务管理_MAC_静态MAC地址表 = "web_mac_static.cgi"
	c服务管理_MAC_黑洞MAC地址表 = "web_mac_filter.cgi"
	c服务管理_MAC_端口安全 = "web_security.cgi"
	c服务管理_MAC_静态安全MAC地址表 = "web_mac_security.cgi"
	c服务管理_生成树_生成树信息 = "web_stp_information.cgi"
	c服务管理_生成树_全局配置 = "web_stp_glb.cgi"
	c服务管理_生成树_生成树端口 = "web_stp_interface.cgi"
	c服务管理_生成树_MST域 = "web_stp_inst.cgi"
	c服务管理_ERPS_ERPS配置 = "web_erps_config.cgi"
	c服务管理_ERPS_ERPS状态 = "web_erps_status.cgi"
	c服务管理_端口镜像_概况 = "web_mirror.cgi"
	c服务管理_端口镜像_全局配置 = "web_mirror_config.cgi"
	c服务管理_端口镜像_镜像配置 = "web_mirror_new.cgi"
	c服务管理_端口镜像_远程镜像MACEscape = "web_mirror_r_escape.cgi"
	c组播_IGMPSnooping功能 = "web_igmp_snooping_global.cgi"
	c组播_IGMPSnooping信息 = "web_igmp_snooping_vlan.cgi"
	cIP路由_IPv4路由表 = "web_routetbl_ipv4.cgi"
	cIP路由_IPv4静态路由 = "web_routetbl_ipv4_static.cgi"
	c安全_蠕虫攻击防护 = "web_worm.cgi"
	c安全_DDoS攻击防护 = "web_ddos.cgi"
	c安全_ARP攻击防护 = "web_arp.cgi"
	c安全_当前会话 = "web_userlist.cgi"
	c安全_用户管理 = "web_user.cgi"
	c工具_Ping = "web_ping.cgi"
	c工具_Traceroute = "web_tracert.cgi"
	c重启保存 = "web_maintenance.cgi"