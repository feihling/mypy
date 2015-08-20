def Palindrome(input):
    i = 0
    j = len(input) - 1
    while i < j:
        while i < j and not input[i].isalpha():
            i = i + 1
        while i < j and not input[j].isalpha():
            j = j - 1
        if input[i].lower() != input[j].lower():
            return False
        i = i + 1
        j = j - 1
    return True

def strstr(input, substr):
    for i in range(len(input)):
        for j in range(len(substr)):
            if substr[j] != input[i + j]
            
print(Palindrome('A man,[ a plan, a canal: Panama'))
