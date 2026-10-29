#program to convert temperature in Celsius to Fahrenheit

def temp_conv(c):
    f=(c*1.8)+32
    return f
temp_list=[150,160,170]
print(list(map(temp_conv,temp_list)))