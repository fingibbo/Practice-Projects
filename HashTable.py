class HashTable:
    def __init__(self):
        self.collection  = {}

    def hash(self, string_parameter: str) -> int:
        #taking each letter of the string parameter, converting it to the unicode value and adding each value to an element in the string
        hash_list = []
        for char in string_parameter:
            hash_list.append(ord(char))
        # adding each value up to get the sum of the unicode values.
        hash_key = 0
        for item in hash_list:
            hash_key += item
        return hash_key

    def add(self, key: str, value):
        hash_of_key = self.hash(key)
        if hash_of_key in self.collection:
            self.collection[hash_of_key][key] = value
        else:
            self.collection[hash_of_key] = {key: value}

    def remove(self, key):
        hash_of_key = self.hash(key)
        if hash_of_key not in self.collection:
            return
        else:
            if key in self.collection[hash_of_key]:
                del self.collection[hash_of_key][key]
            else:
                return

    def lookup(self, key):
        hash_of_key = self.hash(key)
        if hash_of_key in self.collection:
            if key in self.collection[hash_of_key]:
                return self.collection[hash_of_key][key]
            else:
                return None
        else:
            return None


hash1 = HashTable()
print(hash1.hash("golf"))
hash1.add('dear', 'friend')
hash1.add('read', 'book')
hash1.add('fcc', 'fcc test')
hash1.add('cfc', 'cfc test')
print(hash1.collection)
print(hash1.lookup('read'))
hash1.remove('read')
hash1.remove("cfc")
print(hash1.collection)

