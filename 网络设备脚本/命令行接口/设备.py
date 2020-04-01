import time
import random
import re
import weakref
import cflw代码库py.cflw时间 as 时间
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 连接
from ..基础接口 import 设备
from ..基础接口 import 操作
from ..基础接口 import 异常
from ..命令行接口 import 模式
#===============================================================================
# 准备
#===============================================================================
c等待 = 2
c间隔 = c等待 / 10
c网络终端换码 = "\x1b["	#vt100控制码
class S连接栈元素:	#连接栈的元素
	def __init__(self, a连接, a设备):
		self.m连接 = weakref.proxy(a连接)
		self.m设备 = weakref.proxy(a设备)
#===============================================================================
# 设备
#===============================================================================
class I设备(设备.I设备):
	"命令行设备接口"
	def __init__(self, a连接):
		设备.I设备.__init__(self)
		#设备设置
		self.m等待 = c等待
		self.m间隔 = c间隔
		self.m注释 = "#"
		self.m自动提交 = 操作.E自动提交.e不提交
		#连接状态
		self.m连接 = a连接	#当前连接
		v连接栈元素 = S连接栈元素(a连接, self)
		if isinstance(a连接, 连接.I连接包装):	#跳板
			self.m公共连接栈 = a连接.m设备.m公共连接栈	#同一个连接栈中的所有设备共同控制的栈
			self.m当前连接栈 = a连接.m设备.m当前连接栈 + (v连接栈元素,)	#当前连接在连接栈的位置
		else:	#新连接
			self.m公共连接栈 = []
			self.m当前连接栈 = (v连接栈元素,)
		#设备状态
		self.ma模式 = []
		self.m自动换页文本 = ''
		self.m历史命令 = ""	#防止连续执行相同命令
		self.m历史输出 = ""	#如果执行了相同的命令,则返回相同的输出
		self.mf自动登录 = None	#
	def __del__(self):
		if not self.m连接:
			return
		#收集信息
		vi自动提交 = self.m自动提交 != 操作.E自动提交.e不提交
		#安全关闭
		if vi自动提交:
			self.f关闭()
	#设备状态
	def fs延迟(self, a间隔 = c间隔):
		self.m间隔 = a间隔
		self.m等待 = a间隔 * 10
	def fs自动换页(self, a文本):
		"设置自动换页标记"
		self.m自动换页文本 = a文本
		self.m自动换页替换 = None
	def f关闭(self):
		"执行清理操作, 然后关闭连接. f关闭 只能调用一次"
		assert(self.fi当前连接())
		while self.ma模式:
			self.f退出模式()
		self.f退出()
		self.m连接.f关闭()
		self.m公共连接栈.pop()
	def f设备_回显(self, a内容):
		"输出时自动调用"
		if self.m回显:
			print(a内容, end = '', flush = True)
		self.f设备_停顿()
	def f设备_等待回显(self):
		"手动调用,在需要等待的地方调用,显示一个点"
		if self.m等待回显:
			print(".", end = '', flush = True)
	def f设备_停顿(self, a倍数 = 1):
		time.sleep(self.m间隔 * a倍数)
	def fs已登录(self):
		self.mi登录 = True
	#输入输出
	def f输入(self, a文本):
		self.f设备_停顿()
		self.m连接.f写(a文本)
	def f输出(self, a等待 = False):
		"读取输出缓存中的内容, 清除输出缓存"
		#不等待
		if not a等待:
			v内容 = self.m连接.f读_最新()
			self.f设备_回显(v内容)
			return v内容
		#有等待
		v计数 = 0
		v内容 = ""
		while True:
			v读 = self.m连接.f读_最新()
			if v读:
				v内容 += v读
				time.sleep(self.m间隔)
				continue
			else:
				v计数 += 1
				if v计数 >= 10:
					break
				else:
					time.sleep(self.m间隔)
					continue
		self.f设备_回显(v内容)
		return v内容
	def f输入_回车(self, a数量 = 1, a等待 = 1):
		if a数量 > 0:
			for i in range(a数量):
				self.m连接.f写('\r')
				self.f设备_停顿(2)
		elif a数量 == 0:
			pass	#什么都不做
		else:	#循环,有内容或时间到时结束
			v阻塞 = 时间.C循环阻塞(a等待)
			while v阻塞.f滴答():
				self.m连接.f写('\r')
				v输出 = self.f输出()
				if v输出:
					break
	def f输入_退格(self, a数量 = 1):
		self.f输入('\b' * a数量)
	def f输入_空格(self, a数量 = 1):
		self.f输入(' ' * a数量)
	def f输入_任意键(self, a数量 = 1):
		v字符 = random.choice("qwertyuiopasdfghjklzxcvbnm")
		self.f输入(v字符)
	def f输入_注释(self):
		self.f输入(self.m注释)
	def f输入_结束符(self):
		raise NotImplementedError()
		#实现示例:
		#self.f输入('\x1a')	#ctrl+z
		#self.f输入('\x03')	#ctrl+c
	def f刷新(self):
		"清除正在输入的命令, 清除输出缓存"
		self.f设备_停顿()
		v输出 = self.m连接.f读_最新()
	def f等待响应(self, a时间 = 5):
		v输出 = self.m连接.f读_直到('', a时间)
		if self.m回显 and v输出:	#回显
			print(v输出, end = '', flush = True)
			return
	def f检查命令(self, a命令):
		"判断命令能不能执行"
		raise NotImplementedError()
	def f执行命令(self, a命令):
		"输入一段字符按回车, 并返回输出结果"
		#准备命令
		v命令 = str(a命令)
		self.m历史命令 = v命令
		#执行
		self.f刷新()
		self.f输入(v命令)
		self.f输入_回车()
		self.m历史输出 = self.f输出()
		return self.m历史输出
	def f执行配置命令(self, a命令, a自动提交 = True):
		self.f执行命令(a命令)
		if a自动提交:
			self.f自动提交(操作.E自动提交.e立即)
	def f执行显示命令(self, a命令, a自动换页 = True):
		"有自动换页功能"
		#准备命令
		v命令 = str(a命令)
		if v命令 == self.m历史命令:
			return self.m历史输出
		self.m历史命令 = v命令
		#执行
		self.f刷新()
		self.f输入(v命令)
		self.f输入_回车()
		return self.f输出显示结果(a自动换页)
	def f输出显示结果(self, a自动换页 = True, a最小等待 = 1):
		v输出 = ''
		v计时 = 时间.C秒表()
		if a自动换页 and self.m自动换页文本:
			while True:
				v读 = self.f输出(a等待 = True)
				v输出 += v读
				if self.m自动换页文本 in v读:	#还有更多
					self.f输入_空格()
					self.f设备_等待回显()
					continue
				else:	#没有更多
					if v计时.f滴答() < a最小等待:
						continue
					else:
						break
			v输出 = self.f自动换页替换(v输出)
		else:
			v输出 = self.f输出(a等待 = True)
		self.m历史输出 = v输出.replace("\r\n", "\n")
		return self.m历史输出
	def f处理显示结果(self, a输出):
		"""根据具体设备对显示结果进行处理"""
		return a输出	# 默认不处理,原样返回
	def f自动换页替换(self, a字符串: str):
		v替换位置 = a字符串.find(self.m自动换页文本)
		if v替换位置 < 0:
			return a字符串	#找不到,不处理
		if not self.m自动换页替换:	#没有则生成
			v退格结束位置 = 字符串.f连续找最后(a字符串, c网络终端换码, c网络终端换码, "D", a开始 = v替换位置)
			if v退格结束位置 >= 0:	#telnetlib
				self.m自动换页替换 = a字符串[v替换位置 : v退格结束位置+1]
			elif '\x08' in a字符串:	#退格字符
				v行首位置 = a字符串.rfind("\r\n", 0, v替换位置) + 2
				v行尾位置 = a字符串.find("\r", v替换位置)
				v退格位置 = a字符串.rfind('\x08', v行首位置, v行尾位置)
				self.m自动换页替换 = a字符串[v行首位置 : v退格位置+1]
			else:	#回车覆盖
				v回车位置 = a字符串.find(" \r", v替换位置)
				self.m自动换页替换 = a字符串[v替换位置 : v回车位置 + 1]
		return a字符串.replace(self.m自动换页替换, '')
	#模式操作
	def fg当前模式(self):
		if self.ma模式:
			return self.ma模式[-1]
		else:
			return None
	def f进入模式(self, a模式):
		if not isinstance(a模式, 模式.I模式):
			raise TypeError("a模式 必须是一个 模式.I模式 对象")
		v命令 = a模式.fg进入命令()
		if v命令:
			self.f执行命令(v命令)
		self.ma模式.append(a模式)
		a模式.f事件_进入模式()
	def f退出模式(self):
		v模式 = self.ma模式[-1]
		v模式.f事件_退出模式()
		if type(v模式).fg退出命令 != 模式.I模式.fg退出命令:
			self.f执行命令(v模式.fg退出命令())
		else:
			self.f退出()
		self.ma模式.pop()
	def f切换模式(self, aa模式):	#aa模式 必需是强引用, 而 模式.I模式.m模式栈 全是弱引用需要转换
		"自动退出当前模式并进入新模式"
		v现模式长度 = len(self.ma模式)
		v新模式长度 = len(aa模式)
		v最大长度 = max(v现模式长度, v新模式长度)
		v进入位置 = 0
		#判断模式是否一样,并退出现模式
		for i in range(v最大长度):
			#找不同模式的位置,然后退出到有相同模式的位置为止
			#如果新模式是现模式的更深一层模式,不退出,直接进入新模式
			if i >= v现模式长度:
				break
			if i >= v新模式长度 or self.ma模式[i] != aa模式[i]:
				for j in range(v现模式长度 - i):
					self.f退出模式()
				break
		v进入位置 = i
		#进入模式
		for i in range(v进入位置, v新模式长度):
			self.f进入模式(aa模式[i])
	def f抛出模式异常(self):
		raise 异常.X模式(self.fg当前模式())
	#连接操作
	def f切换到当前连接(self):
		#切换连接的过程类似切换模式
		if self.fi当前连接():
			return
		v现连接长度 = len(self.m公共连接栈)
		v新连接长度 = len(self.m当前连接栈)
		v最大长度 = max(v现连接长度, v新连接长度)
		v进入位置 = 0
		for i in range(v最大长度):
			if i >= v现连接长度:
				break
			if i >= v新连接长度 or self.m公共连接栈[i] != self.m当前连接栈[i]:
				for j in range(v现连接长度 - i):
					self.m公共连接栈[-1].m设备.f关闭()
				break
		v进入位置 = i
		for i in range(v进入位置, v新连接长度):
			v当前连接 = self.m当前连接栈[i]
			v当前连接.m连接.f连接()
			self.m公共连接栈.append(v当前连接)
			if v当前连接.m设备.mf自动登录:	#自动登录
				v当前连接.m设备.mf自动登录()
	def fi当前连接(self):
		if not self.m公共连接栈:	#没有连接
			return False
		return self.m当前连接栈[-1] == self.m公共连接栈[-1]	#偷懒,直接比较最后一个
	#动作&命令
	def f自动适应延迟(self, a测试字符: str = '#'):
		"发送字符测试延迟,根据响应时间确定间隔"
		v和 = 0
		v秒表 = 时间.C秒表()
		for i in range(10):
			v秒表.f重置()
			self.m连接.f写(a测试字符)
			self.m连接.f读_直到(a测试字符, 2)
			v和 = v秒表.f滴答()
		self.fs延迟(v和 / 5)	#间隔设置为平均响应时间的2倍
	def f退出(self, a关闭 = False):
		"""设备默认退出当前模式行为, 如果模式重写了 fg退出命令 则不调用该函数\n
		如果当前模式是用户模式, 则退出登录"""
		raise NotImplementedError()	#实现示例: self.f执行命令("exit")
	def fg提示符(self):
		raise NotImplementedError()
	def fs自动提交(self, a):
		"""设置自动提交行为:
		0:不自动提交, 1:退出配置模式时自动提交, 2:退出当前模式时自动提交, 3:执行配置命令后立即提交"""
		self.m自动提交 = a
	def f提交(self):
		"""手动提交"""
		raise NotImplementedError()	#实现示例: self.f执行命令("commit")
	def f自动提交(self, a级别):
		"""判断级别确定是否提交"""
		if not 操作.f自动提交(self.m自动提交, a级别):
			return
		v模式 = self.ma模式[-1]
		if type(v模式).fg提交命令 != 模式.I模式.fg提交命令:
			self.f执行命令(v模式.fg提交命令())
		else:
			self.f提交()
	#显示.当存在可以在任何模式使用的命令,直接重写这里的函数
	def f显示_当前模式配置(self):
		raise NotImplementedError()
#===============================================================================
# 设备函数
#===============================================================================
c匹配数字 = re.compile(r'(?<!\w)\d+\.?\d*(?!\w)')
def f设备名_括号包围式(a文本):
	return a文本[1:-1]
def f设备名_前缀式(a文本):
	return re.split(r'>#(', a文本)[0]
def f时间(a周, a日, a时, a分):
	return (((int(a周) * 7 + int(a日)) * 24 + int(a时)) * 60 + int(a分)) * 60
def f取数字(a文本):
	v结果 = c匹配数字.findall(a文本)
	i = 0
	while i < len(v结果):
		if '.' in v结果[i]:
			v结果[i] = float(v结果[i])
		else:
			v结果[i] = int(v结果[i])
		i += 1
	return v结果
def f去头尾行(a文本, a头行 = 1, a尾行 = 1, a行分割符 = '\n', a转列表 = False):
	if a转列表:
		v文本 = a文本.split(a行分割符)
		if a头行:
			v文本 = v文本[a头行:]
		if a尾行:
			v文本 = v文本[:-a尾行]
		return v文本
	else:
		v头行位置 = 0
		for i in range(a头行):
			v头行位置 = a文本.find(a行分割符, v头行位置)
			if v头行位置 == -1:
				return ""
				#raise ValueError('头行位置超出范围')
			v头行位置 += 1
		v尾行位置 = len(a文本)
		for i in range(a尾行):
			v尾行位置 = a文本.rfind(a行分割符, v头行位置, v尾行位置)
			if v尾行位置 == -1:
				return ""
				#raise ValueError('尾行位置超出范围')
		return a文本[v头行位置 : v尾行位置]
def f参数等级(a, a最高):
	"不同厂商对于权限等级的定义不同。为了统一，参数限制为只能用[0,1]之间的值"
	v类型 = type(a)
	if v类型 == int:
		return v类型 * a最高
	elif v类型 == str:
		if '/' in a:	#分数
			v数字 = fractions.Fraction(a)
		else:
			v数字 = a
	else:
		v数字 = a
	return math.floor(float(v数字) * a最高 + 0.5)
