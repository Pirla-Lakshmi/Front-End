str = input().split()
max_num,max_sum="",0
for i in str:
    sum=0
    for digit in i:
        sum=sum+int(digit)
    if sum>max_sum:
        max_sum=sum
        max_num=i
    elif max_sum==sum:
        max_num=max_num+" "+i
print(max_num)