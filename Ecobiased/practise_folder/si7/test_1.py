# class Employee(models.Model):
#     """
#     Class to store employee details
#     """
#     emp_id = models.IntegerField()
#     name = models.CharField(max_length=100)
#     image_path = models.ImageField(upload_to='path')
#
#
# class SerializerClass(serializer.ModelSerialzer):
#     model = 'Employee'
#
#
# class Employees():
#
#     def get(self, request):
#         employees = Employee.objects.filter(Q(name__startswith='a') and image_path='')
#         employee_ser_data = SerializerClass(employees)
#         return employee_ser_data
#
#     def post(self, request):
#         name = request.POST.get('name')
#         image_path = request.POST.get('image_path')
#         emp_obj = Employee()
#         emp_obj.name = name
#         emp_obj.image_path = image_path
#         emp_obj.save()
#         return HttpResponse("created")
#
#
#
# url_patterns = [
#     path('get_employee_list', Employees.as_view(), 'get_employee_list')
# ]
#
# Input : s1 = "listen"
#         s2 = "silent"
# Output : The strings are anagrams.

def is_anagrams(s1, s2):
    count = 0
    if len(s1) != len(s2):
        return "not"
    for char in s1:
        if char in s1:
            if s1.count(char) != s2.count(char):
                continue
            count += 1
    if count == len(s2):
        return "yes"
    else:
        return "not"

print(is_anagrams("dad", "bad"))