def z_func(s):
	out = []
	if not s: return out
	i, slen = 1, len(s)
	out.append(0)
	while i < slen:
		left, right = 0, i
		while right < slen and s[left] == s[right]:
			left += 1
			right += 1
		out.append(left)
		i += 1
	return out
#def solo(A, B):
#	i, Blen = 0,len(B)
#	k1=''
#	k2=''
#	s=''
#	if (A==B):
#		return 0
#	else:
#		i+=1
#		while i < Blen:
#			k1=A[-i:]
#			k2=A[:-i]
#			s=k1+k2	
#			if(s==B):
#				return Blen - i
#			i+=1
#	return -1
a = input()
b = input()
c = b + "#" + a + a
z = [0]*len(c)
left = right = 0
for i in range(1,len(c)):
	x = min(z[i-left],right-i+1) if i<= right else 0
	while i+x < len(c) and c[x] == c[i+x]:
		x+=1
	if i+x-1 > right:
		left,right = i, i+x-1
	z[i] = x
for j in range(len(a)+1,len(c)):
	if z[j] >= len(a):
		d = j - (len(a)+1)
		break
	else:
		d= -1
print(d)
