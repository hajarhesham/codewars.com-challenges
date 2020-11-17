def countBits(n):
    count = 0
    num= bin(n)
    number= num[2:]
    for x in number:
        if x == "1":
            count +=1
    return count
