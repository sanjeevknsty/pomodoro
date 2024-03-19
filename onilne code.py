def printLongestSubstring(s: str) -> None:
	n = len(s)
	l, r = 0, 0
	visited = set()
	maxStr = 0
	maxL, maxR = 0, 0
	while r < n:
		if s[r] not in visited:
			visited.add(s[r])
			if r - l + 1 > maxStr:
				maxStr = r - l + 1
				maxL, maxR = l, r
			r += 1
		else:
			visited.remove(s[l])
			l += 1
	print(s[maxL:maxR+1])

str = "GEEKSFORGEEKS"
printLongestSubstring(str)
