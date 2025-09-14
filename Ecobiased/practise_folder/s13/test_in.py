# from copy import copy, deepcopy
#
# input_list = [1, 2, [3, 4], 12]
#
# # example of shallow copy
#
# copied_list = input_list.copy()
#
# copied_list[2][0] = 99
#
# print("copied_list", copied_list)
# print("input_list", input_list)
#
# # example of deep copy
# input_list1 = [1, 2, [3, 4], 12]
# copied_list1 = deepcopy(input_list)
#
# copied_list1[2][0] = 99
#
# print("copied_list1", copied_list1)
# print("input_list1", input_list1)

ips= [1,2,3,3,4,5,6,1,2,1,2,3,4,5,6]
longest = []
current = [ips[0]]
print("starting current", current)

for i in range(1, len(ips)):
    if ips[i] == ips[i - 1] + 1:
        current.append(ips[i])
        print("come in if", i)
        print("current", current)
    else:
        print("come in else", i)
        if len(current) > len(longest):
            longest = current
        current = [ips[i]]
        print("current", current)

# Final check at the end
if len(current) > len(longest):
    longest = current

print("Longest continuous +1 sequence:", longest)
print("Length:", len(longest))




#
# Employee- emp_id, emp_name, dept_id, joining_date
# Salary- emp_id, emp_name, salary
# Second highest salary of employee in each dept
#
# select top(1) e.department, s.salary from Employee e inner join salary s
# on e.emp_id = s.emp_id
# group by e.department order by s.salary desc offset 1
#
# select emp_id, salary from(
# select e.emp_id as emp_id, s.salary as salary, DENSE_RANK(over partition by e.department order by s.salary desc) as rank from Employee e
# inner join salary s on e.emp_id = s.emp_id) where rank = 2;
#
# def fun1():
#     print(1)
# def fun2():
#     print(2)
#
# @fun2
# @fun1
# def fun():
#     print("xyz")
#
# fun()
