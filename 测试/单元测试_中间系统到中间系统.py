import unittest
import 网络设备脚本.基础接口.中间系统到中间系统 as 中间系统到中间系统
class C测试(unittest.TestCase):
	def test网络标识全写(self):
		ca参数 = [
			"00.0000.0000.0000.0000.00",
			"00.0000.192.168.000.001.00",
		]
		for v参数 in ca参数:
			v网络标识 = 中间系统到中间系统.S网络标识.fc字符串(v参数)
			print(v参数, v网络标识)
			self.assertTrue(v网络标识)
	def test网络标识三段(self):
		ca参数 = [
			("1", "1", "0"),
			(1, 1, 0),
			("00.0000", "0000.0000.0001", "00"),
			("00.0000", "192.168.000.001", "00"),
		]
		for v参数 in ca参数:
			v网络标识 = 中间系统到中间系统.S网络标识.fc三段(*v参数)
			print(v参数, v网络标识)
			self.assertTrue(v网络标识)
if __name__ == "__main__":
	unittest.main()