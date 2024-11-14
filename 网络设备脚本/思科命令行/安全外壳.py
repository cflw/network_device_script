import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 安全外壳 as 北向安全外壳
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 安全外壳 as 南向安全外壳
from .常量 import *
from . import 接口 as 实现接口
class C安全外壳显示(北向安全外壳.I安全外壳显示, 模式.I显示模式):
	"""适用于: (模拟器)思科c7200(15.2(4)M11)
		浪潮s5960(12.2(5)I1), 浪潮s6650(11.12.1a)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def fg服务状态(self):
		v输出 = self.m设备.f执行显示命令("show ip ssh")
		#↓模拟器思科c7200(15.2(4)M11)显示的结果
		# SSH Enabled - version 2.0
		# Authentication timeout: 120 secs; Authentication retries: 3
		# Minimum expected Diffie Hellman key size : 1024 bits
		# IOS Keys in SECSH format(ssh-rsa, base64 encoded):
		# ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAYQC0R/hhtwaGaK3T6TQf8hgFLKRdmo5XL9iE2XOiPgPL
		# G/ZV8tqB5r76wIvdE6YlVlPsR663VL+4yukYgRuwxhpbKRAI8qO0Pt95L8rtdqLlbdhLsKf36zmRa+T5
		# bz0FQT8=          
		return v输出
	def fg开关(self):
		#有密钥即开启
		v输出 = self.m设备.f执行显示命令("show ip ssh")
		return "SSH Enabled" in v输出
	def fg访问列表(self):
		v输出 = self.m设备.f执行显示命令("show running-config | section line vty", a等待 = 5)
		# line vty 0 4
		#  access-class ssh in vrfname Mgmt-vrf
		#  transport input all
		# line vty 5 15
		v分割 = v输出.split("line vty")	#可能有多段line vty
		for v节 in v分割[1:]:
			v允许协议 = 字符串.f提取字符串之间(v节, "transport input ", "\n", a结束严谨 = False)
			if v允许协议 in ("all", "ssh", None):
				return 字符串.f提取字符串之间(v节, "access-class ", " ")
	def fg版本(self):
		v输出 = self.m设备.f执行显示命令("show running-config | include ip ssh version")
		# ip ssh version 2
		return int(v输出[15:])
	def fg日志记录(self):
		v输出 = self.m设备.f执行显示命令("show running-config | include ip ssh logging")
		# ip ssh logging events
		return bool(v输出)
class C安全外壳配置(南向安全外壳.I安全外壳配置, 模式.C同级模式):
	"""适用于: 思科c7200(15.2(4)M11)"""
	def __init__(self, a):
		南向安全外壳.I安全外壳配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		pass
	def f生成密钥(self, a长度 = 1024, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = "crypto key generate rsa"
		if v操作 in (操作.E操作.e删除, 操作.E操作.e关闭):
			self.f执行当前模式命令(c不 + v命令)
			return
		v输出 = self.f执行当前模式命令(v命令)
		if "% Please define a domain-name first" in v输出:
			self.fg上级模式().fs域名()
			self.f执行当前模式命令("crypto key generate rsa")
		#% You already have RSA keys defined named xxxx.xxxx.
		#% Do you really want to replace them? [yes/no]:
		if "replace" in v输出:
			if v操作 in (操作.E操作.e设置, 操作.E操作.e修改):
				v输出 = self.m设备.f执行命令("y")
			else:
				v输出 = self.m设备.f执行命令("n")
				return
		#The name for the keys will be: xxxx.xxxx
		#Choose the size of the key modulus in the range of 360 to 4096 for your
		#   General Purpose Keys. Choosing a key modulus greater than 512 may take
		#   a few minutes.

		#How many bits in the modulus [512]:
		if "modulus" in v输出:
			self.m设备.f执行命令(a长度)
		#% Generating 1024 bit RSA keys, keys will be non-exportable...
		#[OK] (elapsed time was 6 seconds)
		time.sleep(2)
		self.m设备.f输出(a等待 = True)
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("ip ssh version")
		v命令 += a版本
		self.f执行当前模式命令(v命令)
	def fs源接口(self, a接口, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip ssh source-interface")
		if 操作.fi加操作(v操作):
			v接口 = 实现接口.f创建接口(a接口)
			v命令 += v接口
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs连接数(self, a数量 = 5, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip ssh maxstartups")
		if 操作.fi加操作(v操作):
			v命令 += a数量
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs认证重试(self, a次数, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip ssh authentication-retries")
		if 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		else:
			v命令 += a次数
		self.f执行当前模式命令(v命令)
	def fs认证超时(self, a时间, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip ssh timeout")
		if 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		else:
			v命令 += a时间
		self.f执行当前模式命令(v命令)
