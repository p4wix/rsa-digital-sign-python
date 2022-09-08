import numpy as np

def calcEntropy(tab):
	marg = np.histogramdd(np.ravel(tab), bins = 256)[0] / tab.size
	marg = list(filter(lambda p: p > 0, np.ravel(marg)))
	entropy = -np.sum(np.multiply(marg, np.log2(marg)))
	return entropy

def decimalToBinary(n):
	n = bin(n).replace("0b", "")
	if len(n) != 16:
		n = (16-len(n))*"0" + n
	if "-" in n:
		n = n.replace("-", "")
		n = "-" + n
	return n

def binToDecimal(n):
   return int(n, 2) 

def swapNibbles(x): 
   return ((x & 0x0F) << 4 | (x & 0xF0) >> 4)