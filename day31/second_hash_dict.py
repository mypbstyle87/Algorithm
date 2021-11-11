hash_table = [0 for i in range(10)]


def hash_func(key):
    return key % 5


def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

storage_data('Andy', '01032130231')
storage_data('Dave', '01231232222')
storage_data('Trump', '0332323222')

print(get_data('Andy'))



