import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 接口 as 南向接口
#s交换机v3
ca接口名称_sv3 = 北向接口.ca接口名称 | {
	北向接口.E类型.e空: "null",
	北向接口.E类型.e环回: "loopback",
	北向接口.E类型.e快速以太网: "fastethernet",
	北向接口.E类型.e聚合: "port-channel",
	北向接口.E类型.e吉以太网: "gigaethernet",
	北向接口.E类型.e十吉以太网: "tengigabitethernet",
	北向接口.E类型.e虚拟局域网: "vlan",
	北向接口.E类型.e堆叠: "isf-port",
}
ca接口缩写_sv3 = ca接口名称_sv3 | {
	北向接口.E类型.e环回: "LO",
	北向接口.E类型.e堆叠: "ISF",
	北向接口.E类型.e聚合: "PC",
	北向接口.E类型.e吉以太网: "GE",
	北向接口.E类型.e十吉以太网: "TGE",
	北向接口.E类型.e快速以太网: "FE",
}
f生成接口_sv3, f创建接口_sv3,  = 北向接口.F接口工厂(ca接口名称_sv3)
f生成接口缩写_sv3, f创建接口缩写_sv3 = 北向接口.F接口工厂(ca接口缩写_sv3)
