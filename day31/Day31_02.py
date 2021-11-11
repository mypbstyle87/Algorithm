class Person:
    count = 0
    def __init__(self):
        self.bag = []
        Person.count += 1

    def put_bag(self, stuff):
        self.bag.append(stuff)

    @classmethod
    def print_count(cls):
        print("{0}명 생성되었습니다.".format(cls.count))


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

Person.print_count()