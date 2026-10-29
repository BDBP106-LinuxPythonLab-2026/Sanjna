#program to convert celsius to fahrenheit using lambda expression

temp_list=[150,160,170]
print(list(map(lambda c: (c*1.8)+32, temp_list)))