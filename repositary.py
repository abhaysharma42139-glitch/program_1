def function(str1,chr):
    for i in range(len(str1)-1):
        if str1[i]==chr:
            return i
    return "not found"
a=input()
b=input()
print(function(a,b))