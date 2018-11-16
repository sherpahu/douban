lst = '''
嗯
啊
嗻
是
欸
呦
噢
嘿
别挨骂了
去你的吧
就这个呀
还真是
我呀
您等等儿吧
'''.split('\n')
import random
while 42:
	line = input('甲: ')
	if line == '（鞠躬下台':
		print('乙: （鞠躬下台')
		break
	else:
		print('乙: '+random.choice(lst))

#作者：Bimos
#链接：https://zhuanlan.zhihu.com/p/35231261
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
