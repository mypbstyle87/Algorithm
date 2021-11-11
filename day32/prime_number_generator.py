def prime_number_generator(start_num, stop_num):
    curr = 10
    prime_list = [2, 3, 5, 7]
    while curr < 1000:
        for i in prime_list:
            if curr % i == 0:
                break
        else:
            prime_list.append(curr)
        curr += 1

    cut_list = list(filter(lambda x: start_num < x < stop_num, prime_list))
    yield from cut_list


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
