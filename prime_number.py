#-*-coding: utf-8-*-
#生成素数
def _odd_iter():#3开始的奇数序列生成器
	n=1
	while True:
		n=n+2
		yield n 
def _not_divisible(n):#筛选函数
	return lambda x:x%n>0
def primes():#生成器，不断返回素数
	yield 2
	it=_odd_iter()#初始序列
	while True:
		n=next(it)#返回序列的第一个数
		yield n
		it=filter(_not_divisible(n),it)#构造新序
#打印1000以内素数
i=0
for n in primes():
	if n<1000:
		print(n)
		i=i+1
	else:
		print('共有%d个素数'%(i))
		break