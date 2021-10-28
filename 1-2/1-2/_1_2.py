def encrypt(string):
    reversed_string =  string[::-1]
    reversed_string = reversed_string.replace("a","0")
    reversed_string = reversed_string.replace("e","1")
    reversed_string = reversed_string.replace("i","2")
    reversed_string = reversed_string.replace("u","2")
    reversed_string  = reversed_string.replace("o","3")

    return reversed_string + "aca"

word = input()
print(encrypt(word))
