def twoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i+1, j+1)

def twoSum2(numbers, target):
    map = {}
    for i in range(len(numbers)):
        x = numbers[i]
        if target - x in map:
            return (map[target - x] + 1, i + 1)
        map[x] = i

#sorted
def twoSum3(numbers, target):
    for i in range(len(numbers)):
        j = bsearch(numbers, target - numbers[i], i + 1)
        if j != -1:
            return(i+1, j+1)

def bsearch(arrays, x, start):
    l = start
    r = len(arrays) - 1
    while l < r:
        m = int((l + r)/2)
        if arrays[m] > x:
            r = m
        else:
            l = m + 1
    if l == r and arrays[l] == x:
        return l
    else:
        return -1

def twoSum4(numbers, target):
    numbers.sort()
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] > target:
            j = j - 1
        elif numbers[i] + numbers[j] < target:
            i = i + 1
        else:
            return (i + 1, j + 1)

class TwoSum:
    numbers = {}
    def add(self, number):
        if number in self.numbers:
            count = self.numbers[number]
        else:
            count = 0
        self.numbers[number] = count + 1
    def find(self, target):
        for i in self.numbers:
            if target - i == i:
                if self.numbers[i] > 1:
                    return True
            elif target - i in self.numbers:
                return True
        return False

print(twoSum4((1,2,3,4,5), 9))

two_sum = TwoSum()
two_sum.add(1)
two_sum.add(1)
two_sum.add(5)
print(two_sum.find(2))
print(two_sum.find(7))
