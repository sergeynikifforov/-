def z_func(s):
	out = [0]
	if not s: return out
	i, slen = 1, len(s)
	k=0
	chet = 0
	while i < slen :
		if (s[k]!=s[i]):
			k=0
			out.append(0)			
		else:
			while i<slen and s[k]==s[i]:
				chet+=1
				k+=1
				i+=1
				out.append(chet)
		chet=0
		i+=1
	return out
u = input()
print(*z_func(u))
 
