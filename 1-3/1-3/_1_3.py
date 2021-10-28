def to_binary(hexNum):
    decNum =  int(hexNum,16)
    str(decNum)
    biNum = ""
    for i in range(8):
        biNum += str(decNum % 2)  
        decNum = decNum // 2
    return biNum[ ::-1]

hexNum = input() 
print(to_binary(hexNum))
