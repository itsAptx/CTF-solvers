from Crypto.Util.number import *
from gmpy2 import invert
import math
from sympy import nextprime

def verify_keys(a,b):
	while True:
		if a%4==3:
			while b%4!=3:
				b=nextprime(b)
			return a,b
		if b%4==3:
			while a%4!=3:
				a=nextprime(a)
			return a,b
		a,b=nextprime(a),nextprime(b)

def dec(msg, bs, ll, mds):
	x = 15564066497424
	c = ''
	for i in range(ll):
		x = pow(x,2,mds)
		p = (bin(x)[2:])[-bs:] #ekher block
		c_i = int(p,2)^int(msg[i*bs:(i+1)*bs],2)
		ci_bin = format(c_i, '0' + str(bs) + 'b') #bin
		c += ci_bin
	return c

#Part1 : Boneh Durfee
n = 136925867715334350539351541819374303153581861883077425871381479619256902280896182751175418274848819117804106313526390171733172646719203781502341411544996240718046559322020330755493739123717974336861438650061159088512867158495809372652057009979517497499951599965613535967213529497308200114836792389883404448987
d = 23974584842546960047080386914966001070087596246662608796022581200084145416583
c = 46282600628982824130530839707152802257095678655388901777970530297126873677669029302844975736419114037407828011895452774978714646752289839556387176301641119447701609034322702222708553203047498652811019927150942380861621605039714510498733535604972160616786208389979609391313009722848684563568437967800442928084

part1 = long_to_bytes(pow(c1,d1,n))


#Recover p given n,e,d
p = 0
k = e*d - 1
g = 2
while True:
	t = k
	g = nextprime(g)
	print g
	while t%2 == 0:
		t = t//2
		x = pow(g,t,n)
		if x>1:
			g = gcd(x-1,n)
			if g>1:
				p = g
				break

p = 11391686090403905599695015583829755003551766728158057028281938682097322841603835874354540607209988671617182359012432600907514677996087087987893334356043831
q = n/p
assert p*q == n

p2, q2 = verify_keys(p,q)
N = p2*q2

cipher2 = '101110100011010000110010100100000011001110110001010101100101000000100111011010010010110101000101000110000100011001001100111011111011101001110111100001100011101010101111101100001000010111111000110110110010110100000001001011100010011000110100111100001100111001101110001111001100010001001111100110110110100001011100011100110101001000011100100011011110011000010100110010100111000010101101110101011100010110000100001101101101001111000101011100101100100110110011101000100010101000010001010010110110101011111101110011101110010000101001000111000000100100001010110111001011110001010100100001101111010010111101111001001001111010001100000111000010000100110101100010001111100011111100100100001010010100111010100010000101110000110101000101100'

block_size = 9
block_nbre = len(cipher2)/9

flag = dec(cipher2, 9, block_nbre, N)
print long_to_bytes(int(flag,2))