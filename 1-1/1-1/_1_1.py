def number_length(num):
    count = 0
    if num == 0:
        return 1
    while(num != 0):
        count+=1
        num  = num//10
    return count

n = int(input())
print(number_length(n))
