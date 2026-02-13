nums=[1,2,3,4,5,6]
nums_filter=list(filter(lambda x : x % 2 !=0 , nums))
print(*nums_filter)