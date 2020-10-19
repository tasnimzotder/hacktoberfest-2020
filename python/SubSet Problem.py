def PrintDP(dp):
	for i in dp:
		for j in i:
			print(j,end="\t")
		print("")

def Subset(n,S,arr):
	dp=[[-1 for i in range(S+1)] for j in range(n+1)]

	for i in range(S+1):
		dp[0][i]=False

	for j in range(n+1):
		dp[j][0]=True

	for i in range(1,n+1):
		for j in range(1,S+1):
			if(arr[i-1]>j):
				dp[i][j]=dp[i-1][j]
			else:
				dp[i][j]= dp[i-1][j] or dp[i-1][j-arr[i-1]]
	PrintDP(dp)
	PrintSubSets(dp,n,S,arr)
	return(dp[n][S])

def PrintSubSets(dp,n,S,arr):
	if(n==0 or S==0):
		print("")
		return
	
	if(not dp[n][S]):
		return
	
	if(arr[n-1]>S):
		PrintSubSets(dp,n-1,S,arr)
		return
	else:
		#Involved Case
		if(dp[n-1][S-arr[n-1]] ):
			print(arr[n-1],"(",n,S,")",end="IC")
			PrintSubSets(dp,n-1,S-arr[n-1],arr)
		#Not Involved Case
		if(dp[n-1][S]):
			PrintSubSets(dp,n-1,S,arr)
		else:
			print(arr[n-1],"(",n,S,")",end="NIC")
		
arr=[1,2,3,4]
S=7
print(Subset(4,7,arr))