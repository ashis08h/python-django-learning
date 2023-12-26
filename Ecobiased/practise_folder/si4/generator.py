def create_seq(a_list):
    for i in a_list:
        yield(i)


r= create_seq([1,2,3,4])
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
