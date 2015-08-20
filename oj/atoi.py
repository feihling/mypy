'''
Created on 2015-3-25

@author: lingfeihua
'''
def strstr(ainput, substr):
    m = len(ainput)
    n = len(substr)
    i = 0
    while (i <= m - n):
        j = 0
        while j < n:
            if substr[j] != ainput[i + j]:
                break
            j = j + 1
        if j == n:
            return i
        
        i = i + 1
    return -1

def reverse(ainput):
    output = []
    i = len(ainput) - 1
    while(i >= 0):
        j = i
        while ainput[j] != ' ':
            j = j - 1            
        if j != i:
            output.append(ainput[j:i + 1])
            i = j
        else:
            i = i - 1
    return ' '.join(output)

def custom_atoi(ainput):
    ainput = ainput.strip()
    number = 0
    for i in range(len(ainput)):
        if ainput[i].isdigit():
            number = number * 10 + int(ainput[i])
        else:
            break
    return number

def longsubstring1(ainput):
    sublist = []
    maxlen = 0
    for i in range(len(ainput)):
        for j in range(i, len(ainput)):
            if ainput[j] not in sublist:
                sublist.append(ainput[j])
                if len(sublist) > maxlen:
                    maxlen = len(sublist)
            else:
                sublist = []
                break
    return maxlen

def longsubstring(ainput):
    alphadic = {}
    maxlen = 0

    return maxlen
                   
def longsubstring2(ainput):
    maxlen = 0
    sublist = []
    for i in range(len(ainput)):
        for j in range(i, len(ainput)):
            if ainput[j] not in sublist:
                if len(sublist) <= 2:
                    sublist.append(ainput[j])
                else:
                    break
            if j - i > maxlen:
                maxlen = j - i
    return maxlen

print strstr('abcdefg', '')
print reverse(' no  news is good news ')
print reverse(' no ')
print custom_atoi('11234a')
print longsubstring1('abcdefdabfg')
print longsubstring2('eceba')