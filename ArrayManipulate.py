class ArrayManipulate:
	def arrayManipulate(self, n:int, arr:list)->int:
		n=n+2;
		result=[]
		for i in range(0, n):
			result.append(0);
		for i in range(len(arr)):
			start=arr[i][0]
			end=arr[i][1]+1
			add=arr[i][2]
			result[start]=result[start]+add
			result[end]=result[end]-add
		maxV:int
		maxV=result[0]
		for i in range(1,n):
			result[i]=result[i]+result[i-1]
			if result[i]>maxV:
				maxV=result[i]
		return maxV
arr=ArrayManipulate()
print(arr.arrayManipulate(10, [[1,5,3], [4,8,7], [6,9,1]]))