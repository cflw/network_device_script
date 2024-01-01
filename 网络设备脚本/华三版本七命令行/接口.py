from ..基础接口 import 接口 as 北向接口
from ..华三命令行 import 接口 as 旧接口
#===============================================================================
# 常量&函数
#===============================================================================
#接口名称_v7
ca接口名称_v7 = 旧接口.ca接口名称 | {
	北向接口.E类型.e管理: "M-GigabitEthernet",
	北向接口.E类型.e聚合: "Bridge-Aggregation",
	北向接口.E类型.e三层聚合: "Route-Aggregation",
	北向接口.E类型.e万兆以太网: "Ten-GigabitEthernet",
	北向接口.E类型.e四万兆以太网: "FortyGigE",
	北向接口.E类型.e十万兆以太网: "HundredGigE",
}
f生成接口v7, f创建接口v7 = 北向接口.F接口工厂(ca接口名称_v7)
#接口缩写v7
ca接口缩写v7 = 旧接口.ca接口缩写 | {	#适用于:
	北向接口.E类型.e管理: "MGE",	#M-GigabitEthernet
	北向接口.E类型.e聚合: "BAGG",	#Bridge-Aggregation
	北向接口.E类型.e三层聚合: "RAGG",	#Route-Aggregation
	北向接口.E类型.e万兆以太网: "XGE",	#Ten-GigabitEthernet
	北向接口.E类型.e四万兆以太网: "FGE",	#FortyGigE
	北向接口.E类型.e十万兆以太网: "HGE",	#HundredGigE
}
ca接口缩写s9v7 = 旧接口.ca接口缩写 | {	#适用于: 华三S9810(v7.1.*)
	北向接口.E类型.e管理: "M-GE",	#M-GigabitEthernet
	北向接口.E类型.e聚合: "BAGG",	#Bridge-Aggregation
	北向接口.E类型.e三层聚合: "RAGG",	#Route-Aggregation
	北向接口.E类型.e万兆以太网: "XGE",	#Ten-GigabitEthernet
	北向接口.E类型.e四万兆以太网: "FGE",	#FortyGigE
	北向接口.E类型.e十万兆以太网: "HGE",	#HundredGigE
}
f生成接口缩写v7, f创建接口缩写v7 = 北向接口.F接口工厂(ca接口缩写v7)
f生成接口缩写s9v7, f创建接口缩写s9v7 = 北向接口.F接口工厂(ca接口缩写s9v7)
#===============================================================================
# 接口配置模式
#===============================================================================
class C接口v7(旧接口.C接口):
	pass