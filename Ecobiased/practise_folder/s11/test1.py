given_number = 21
result_list = list(filter(lambda x:x<given_number, [12, 33, 10, 20, 25]))
print(result_list)



test_list = ['How', 'to', 'use', 'recursive', 'method', 'in', 'Python']
N=3



def get_sentence2(input_list, n):
    input_list = list(map(lambda x: x+" ", input_list))
    new_sen = "".join(input_list[0:n])
    print(new_sen)
    input_list = input_list[n:]
    if len(input_list) > 0:
        get_sentence2(input_list, n)

get_sentence2(test_list, N)
