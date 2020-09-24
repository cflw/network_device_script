import enum
class E模式ad70(enum.IntEnum):
	"""适用于: ad 7.0.3"""
	e主页 = 1	#/html/body/div[1]/ul[一级]/a
	e系统概况 = 2
	e系统概况_活动查看 = 0	#/html/body/div[1]/ul[一级+1]/li[二级+1]/a
	e系统概况_大屏可视 = 1
	e系统概况_虚拟服务详情 = 2
	e系统概况_智能DNS统计 = 3
	e系统概况_DDoS攻击分析 = 4
	e系统概况_链路状态 = 5
	e系统概况_链路状态_总览 = 0
	e系统概况_链路状态_所有链路状态 = 1
	e系统概况_链路状态_虚拟服务链路状态 = 2
	e系统概况_节点状态 = 6
	e系统概况_接口状态 = 7
	e系统概况_DNS状态 = 8
	e系统概况_智能路由状态 = 9
	e系统概况_虚拟IP池状态 = 10
	e系统概况_动态路由表 = 11
	e系统概况_日志查看 = 12
	e报表配置 = 4
	e报表配置_报表生成 = 0
	e报表配置_报表中心 = 1
	e公共对象 = 6
	e公共对象_应用规则库 = 0
	e公共对象_用户地址集 = 1
	e公共对象_域名地址集 = 2
	e公共对象_IP地址集 = 3
	e公共对象_时间计划 = 4
	e公共对象_脚本规则 = 5
	e公共对象_自定义内容 = 6
	e数据中心 = 8
	e数据中心_状态概览 = 0
	e数据中心_数据中心 = 1
	e数据中心_本地服务设备 = 2
	e应用负载 = 10
	e应用负载_服务 = 0
	e应用负载_IP组 = 1
	e应用负载_会话保持 = 2
	e应用负载_节点监视器 = 3
	e应用负载_节点池 = 4
	e应用负载_SSL = 5
	e应用负载_策略 = 6
	e应用负载_虚拟服务 = 7
	e智能DNS = 12
	e智能DNS_DNS服务器 = 0
	e智能DNS_DNS记录 = 1
	e智能DNS_虚拟IP池 = 2
	e智能DNS_DNS映射 = 3
	e智能DNS_LDNS集合 = 4
	e智能DNS_静态就近性 = 5
	e智能DNS_全局配置还原 = 6
	e路由配置 = 14
	e路由配置_智能路由 = 0
	e路由配置_静态路由 = 1
	e路由配置_虚拟IP路由 = 2
	e路由配置_IP_Anycast = 3
	e路由配置_RIP = 4
	e路由配置_OSPF = 5
	e路由配置_BGP = 6
	e路由配置_OSPFV3 = 7
	e网络配置 = 16
	e网络配置_网络接口 = 0
	e网络配置_链路监视器 = 1
	e网络配置_源地址转换 = 2
	e网络配置_端口映射 = 3
	e网络配置_DNS代理 = 4
	e网络配置_网络安全 = 5
	e网络配置_ACL配置 = 6
	e系统配置 = 18
	e系统配置_设备管理 = 0
	e系统配置_序列号 = 1
	e系统配置_用户 = 2
	e系统配置_SMTP服务器 = 3
	e系统配置_SNMP = 4
	e系统配置_告警 = 5
	e系统配置_日志设置 = 6
	e系统配置_系统更新 = 7
	e配置向导 = 20
	e配置向导_应用负载模板 = 0
	e配置向导_智能路由向导 = 1
	e高可用性 = 22
	e高可用性_模式 = 0
	e高可用性_主备 = 1
class C模式ad70:
	"""适用于: ad 7.0.3
	左侧栏一个按钮是一个链接，主框架里面每个标签页也是一个链接"""
	c主页 = "/cgi-bin/main.cgi?action=wel&modify=0"

	c系统概况_活动查看 = "/cgi-bin/viewer/active_view/activity.cgi?action=view_sys"
	c系统概况_大屏可视 = "/cgi-bin/viewer/big_screen_view/big_screen.cgi?action=init"
	c系统概况_虚拟服务详情 = "/cgi-bin/viewer/vs_info/view_vs_state.cgi?action=init"
	c系统概况_智能DNS统计 = "/cgi-bin/viewer/gfad_domain/gfad_domain.cgi?action=view_domain"
	c系统概况_DDoS攻击分析 = "/cgi-bin/viewer/ddos_stat/ddos_analysis.cgi?action=init"
	c系统概况_链路状态 = "/cgi-bin/viewer/link_stat/view_whole.cgi?action=init"
	c系统概况_节点状态 = "/cgi-bin/viewer/node_pool_stat/pool_stat.cgi?action=init"
	c系统概况_接口状态 = "/cgi-bin/viewer/snmp_interface/snmp_interface.cgi?action=init"
	c系统概况_DNS状态 = "/cgi-bin/viewer/dns_view/dns_view.cgi?action=view"
	c系统概况_智能路由状态 = "/cgi-bin/viewer/policy_route_view/policy_route_view.cgi?action=init"
	c系统概况_虚拟IP池状态 = "/cgi-bin/viewer/ip_pool_stat/ip_pool_stat.cgi?action=list"
	c系统概况_动态路由表 = "/cgi-bin/viewer/route_table_stat/route_table.cgi?action=view"
	c系统概况_日志查看 = "/cgi-bin/webui_sys.cgi?requestname=18&cmd=0"
	# c报表配置 = 1
	c报表配置_报表生成 = 0
	c报表配置_报表中心 = 1
	# c公共对象 = 2
	c公共对象_应用规则库 = 0
	c公共对象_用户地址集 = 1
	c公共对象_域名地址集 = 2
	c公共对象_IP地址集 = 3
	c公共对象_时间计划 = 4
	c公共对象_脚本规则 = 5
	c公共对象_自定义内容 = 6
	# c数据中心 = 3
	c数据中心_状态概览 = 0
	c数据中心_数据中心 = 1
	c数据中心_本地服务设备 = 2
	# c应用负载 = 4
	c应用负载_服务 = 0
	c应用负载_IP组 = 1
	c应用负载_会话保持 = 2
	c应用负载_节点监视器 = 3
	c应用负载_节点池 = 4
	c应用负载_SSL = 5
	c应用负载_策略 = 6
	c应用负载_虚拟服务 = 7
	# c智能DNS = 5
	c智能DNS_DNS服务器 = 0
	c智能DNS_DNS记录 = 1
	c智能DNS_虚拟IP池 = 2
	c智能DNS_DNS映射 = 3
	c智能DNS_LDNS集合 = 4
	c智能DNS_静态就近性 = 5
	c智能DNS_全局配置还原 = 6
	# c路由配置 = 6
	c路由配置_智能路由 = 0
	c路由配置_静态路由 = 1
	c路由配置_虚拟IP路由 = 2
	c路由配置_IP_Anycast = 3
	c路由配置_RIP = 4
	c路由配置_OSPF = 5
	c路由配置_BGP = 6
	c路由配置_OSPFV3 = 7
	# c网络配置 = 7
	c网络配置_网络接口 = "/cgi-bin/net/net_interface/net_interface.cgi?action=list"
	c网络配置_链路监视器 = "/cgi-bin/ad/monitor/monitor.cgi?action=monitor_list"
	c网络配置_源地址转换 = "/cgi-bin/ad/snat/snat.cgi?action=list"
	c网络配置_端口映射 = "/cgi-bin/net/mapped/portMap.cgi?action=list"
	c网络配置_DNS代理 = "/cgi-bin/net/dns/dns.cgi?action=edit"
	c网络配置_网络安全 = "/cgi-bin/net/dos/dos.cgi?action=list"
	c网络配置_ACL配置 = "/cgi-bin/net/acl_basic/acl_basic.cgi?action=list"
	# c系统配置 = 8
	c系统配置_设备管理_管理网口 = "/cgi-bin/sys/adminif/systemAdminif.cgi?action=edit"
	c系统配置_设备管理_日期时间 = "/cgi-bin/sys/system_time/systemTime.cgi?action=edit"
	c系统配置_设备管理_配置备份与恢复 = "/cgi-bin/sys/backup/backup_conf.cgi?action=list"
	c系统配置_设备管理_关机重启 = "/cgi-bin/sys/reboot/systemReboot.cgi?action=list"
	c系统配置_设备管理_控制台 = "/cgi-bin/sys/console/web_console.cgi"
	c系统配置_设备管理_其他设置 = "/cgi-bin/sys/privacy/other.cgi?action=listsafe"
	c系统配置_序列号 = "/cgi-bin/sys/sn/adSNinfor.cgi?action=edit"
	c系统配置_用户_用户 = "/cgi-bin/sys/user/userAdmin.cgi?action=userlist"
	c系统配置_用户_角色 = "/cgi-bin/sys/user/userAdmin.cgi?action=rolelist"
	c系统配置_用户_外部认证登录 = "/cgi-bin/sys/external_auth/externalAuth.cgi?action=edit"
	c系统配置_SMTP服务器 = 3
	c系统配置_SNMP = 4
	c系统配置_告警 = 5
	c系统配置_日志设置 = 6
	c系统配置_系统更新 = 7
	# c配置向导 = 9
	c配置向导_应用负载模板 = 0
	c配置向导_智能路由向导 = 1
	# c高可用性 = 10
	c高可用性_模式 = 0
	c高可用性_主备 = 1

class C模式ad705:
	"""适用于: ad 7.0.5~"""
	c运行概览_首页 = "/mod_runtime/homepage/index"
	c运行概览_虚拟服务 = "/mod_runtime/virtual_service/index"
	c运行概览_节点池 = "/mod_runtime/pool/index"
	c运行概览_业务主机 = "/mod_runtime/business/index"
	c运行概览_链路状态 = "/mod_runtime/link/index"
	c运行概览_全局负载 = "/mod_runtime/dns_overview/index"
	c运行概览_数据中心 = "/mod_runtime/data_center/index"
	c运行概览_设备状态 = "/mod_runtime/device/index"
	c运行概览_实时状态 = "/mod_runtime/status/index"
	c运行概览_日志查看 = "/mod_runtime/alarm_log/index"
	c应用负载_虚拟服务 = "/mod_ad/virtual_service/index"
	c应用负载_节点池 = "/mod_ad/node_pool/index"
	c应用负载_业务主机 = "/mod_ad/business/index"
	c应用负载_前置策略 = "/mod_ad/previous/index"
	c应用负载_SSL策略 = "/mod_ad/ssl/index"
	c应用负载_优化策略 = "/mod_ad/optimization/index"
	c应用负载_安全策略 = "/mod_ad/security/index"
	c应用负载_iPro = "/mod_ad/ipro/index"
	c链路负载_智能路由 = "/mod_link/intelligent_router/index"
	c链路负载_DNS代理 = "/mod_link/dns_proxy/index"
	c全局负载_DNS服务器 = "/mod_dns/dns_server/index"
	c全局负载_域名发布 = "/mod_dns/dns_server/index"
	c全局负载_静态就近性 = "/mod_dns/dns_server/index"
	c全局负载_数据中心配置 = "/mod_dns/dns_server/index"
	c资源管理_证书管理 = "/mod_object/certificate/index"
	c资源管理_自定义内容 = "/mod_object/http/index"
	c资源管理_规则地址库 = "/mod_object/rule/index"
	c网络部署_网络接口 = "/mod_network/interface/index"
	c网络部署_网络接口_链路IP配置 = (c网络部署_网络接口, "mod_network.interface.page.net_ip.tab")
	c网络部署_网络接口_链路健康检查= (c网络部署_网络接口, "mod_network.interface.page.net_check.tab")
	c网络部署_网络接口_端口聚合 = (c网络部署_网络接口, "mod_network.interface.page.wan.tab")
	c网络部署_网络接口_端口桥接 = (c网络部署_网络接口, "mod_network.interface.page.bridge.tab")
	c网络部署_网络接口_VLAN子接口 = (c网络部署_网络接口, "mod_network.interface.page.vlan.tab")
	c网络部署_网络接口_网口配置 = (c网络部署_网络接口, "mod_network.interface.page.speed_duplexing.tab")
	c网络部署_地址转换 = "/mod_network/nat/index"
	c网络部署_网络安全 = "/mod_network/security/index"
	c网络部署_静态路由 = "/mod_network/static_router/index"
	c网络部署_动态路由 = "/mod_network/dynamic_router/index"
	c系统管理_通用配置 = "/mod_system/common/index"
	c系统管理_SNMP = "/mod_system/snmp/index"
	c系统管理_告警日志配置 = "/mod_system/alarm/index"
	c系统管理_系统维护 = "/mod_system/maintenance/index"
	c系统管理_调试排障 = "/mod_system/debug/index"
	c系统管理_报表设置 = "/mod_system/report/index"
	c系统管理_补丁更新 = "/mod_system/patchupdate/index"
	c高可用性_模式 = "/mod_ha/mode/index"
	c高可用性_主备信息 = "/mod_ha/standby_manage/index"