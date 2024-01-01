import enum
class E链路聚合协议(enum.Enum):
	e无 = enum.auto()
	e静态 = enum.auto()
	e端口聚合协议 = enum.auto()	#pagp
	e链路聚合控制协议 = enum.auto()	#lacp
ca链路聚合协议 = {
	"none": E链路聚合协议.e无,
	"on": E链路聚合协议.e静态,
	"pagp": E链路聚合协议.e端口聚合协议,
	"lacp": E链路聚合协议.e链路聚合控制协议,
}