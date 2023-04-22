#Algorithms:  Sorting, Searching and Hashes

# 1

def selection_sort(numbers: list):
    for fill_slot in range(len(numbers)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location
        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp
        return numbers

# Usage
my_list = [3, 7, 5, 4, 2, 1, 6]
print(f"my list before sorting: {my_list}")
selection_sort(my_list)
print(f"my list after sorting: {my_list}")


# 2a (just for one string)

def binary_search(text: list, target: str) -> str:
    first = 0
    last = len(text) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if text[mid] == target:
            found = True
        else:
            if target < text[mid]:
                last = mid - 1
            else:
                first = mid + 1

    if found:
        return text[mid]
    else:
        return "Target string not found in the list"

# Usage
text = ['apple', 'banana', 'cherry', 'dates', 'grape', 'oranges']
target = 'cherry'

result = binary_search(text, target)
print(f"Result: {result}")


# 2 b (for several strings)
def binary_search(text_2: list, targets: list) -> str:
    text_2.sort()          # this one was reeaally challenging =)
    result_2 = []

    for target in targets:
        first = 0
        last = len(text_2) - 1
        found = False
        new_result = []

        while first <= last and not found:
            mid = (first + last) // 2
            if text_2[mid] == target:
                found = True
                new_result.append(text_2[mid])
            else:
                if target < text_2[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        if found:
            result_2 += new_result
                                        # result_2 does not return a string! It returns a list
    new_result_str = " ".join(result_2) # I tried to convert list to str here :)

    return new_result_str


# Usage
text_2 = ['broccoli', 'spinach', 'tomato', 'cabbage', 'pepper', 'pumpkin']
targets = ['spinach', 'tomato', 'cabbage']   # (?) why it works here with 'broccoli' but not with 'cabbage'?
                                                # only because it's unsorted ?
result_2 = binary_search(text_2, targets)
print(f"Result: {result_2}")


# 3 - 6

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for n in range(size)]

    def __my_hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.size
            return hash_value
        else:
            raise TypeError(f"Unsupported key type: {type(key)}")

    def put(self, key, data):
        hash_value = self.__my_hash(key)
        bucket = self.table[hash_value]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key):
        hash_value = self.__my_hash(key)
        bucket = self.table[hash_value]
        for k, v in bucket:
            if k == key:
                return v                # return the value only, not the key
        return None  # return None if key is not found
# Usage
table = HashTable(10)
table.put('Alice', 25)
table.put('Bob', 32)
table.put('Charlie', 19)
print(table.get('Alice'))
print(table.get('Bob'))
print(table.get('Charlie'))

