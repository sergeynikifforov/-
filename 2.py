def zfun(A, B):
	out = []
	if not A or not B: return [-1]
	i, Blen = 0,len(B)
	while i < Blen:
		#left, right = 0, i
		#while right < slen and s[left] == s[right]:
		#	left += 1
		#	right += 1
		#out.append(left)
		#i += 1
		left,pos = 0, i
		k = i
		while left < len(A) and pos < len(B) and A[left] == B[pos]:
			left +=1
			pos  +=1
		if(len(A) == left):		
			out.append(k)
		i+=1
	if out==list():
		return [-1]
	return out
a = input()
b = input()
print(*zfun(a,b)) 
