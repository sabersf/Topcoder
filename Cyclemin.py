import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class Cyclemin:
	def shift(self, s, k):
		return str(s[-k:] + s[:-k])
	def bestmod(self, s, k):
		n = len(s)
		if k >= n:
			return k*'a'
		result = s
		for i in range(0,n-1):
			temp = re.sub(r'[^a]','a',self.shift(s,i),k)
			if k == 0:
				temp = self.shift(s,i)
			if temp < result:
				result = temp	
		return result
