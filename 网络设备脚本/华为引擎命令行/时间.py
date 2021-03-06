import time
def f解析时间(a文本: str):
	"""display clock
	适用于: 华为ne40e(v8.180)"""
	#2021-02-27 18:48:20
	#Saturday
	#Time Zone(DefaultZoneName) : UTC
	v时间s = a文本.split("\n")[0]
	v时间 = time.strptime(v时间s, "%Y-%m-%d %H:%M:%S")
	return v时间
