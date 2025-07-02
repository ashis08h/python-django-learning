def generate_iter(a_list):
    for item in a_list:
        yield item


seq = generate_iter([1, 2, 3, 4])
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
# print(seq.__next__())


def add_symbol(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper


@add_symbol
def hello_text():
    return "Ashish Kumar"


print(hello_text())


tabl1 -
id 1, 2, 3, 4, 5, 6
date 29-04-2025, 30-04-2025, 01-05-2025, 02-05-2025, 03-05-2025, 04-05-2025
count 6, 102, 135, 110, 90, 101

select
id, date, count from table1
order by date desc offset 2 limt 1

Employee
id 1, 2, 3
name 'as', 'as', 'yz'

delect from Employee where rank > 2
select id, name from Employee
having count() > 1
dense rank() as rank


WITH CTE AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY name, email, department
               ORDER BY id
           ) AS rn
    FROM Employee
)
DELETE FROM CTE
WHERE rn > 1;


with CTE AS (
SELECT *, ROW_NUMBER() OVER( PARTITIONED BY name ORDER BY id) as rn from Employee
)
DELETE FROM CTE WHERE RN > 1;






