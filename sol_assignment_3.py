#  1. Write a python script to convert a number into str type.

a=10
b=str(a)
print(b)
print(type(b))


#   2. Write a python script to print Unicode of the character ‘m’

print(ord("m"))

#   3. Write a python script to print character representation of a given unicode 100.


x=100
print(chr(x))


#  4. Write a python script to print any number and its binary equivalent

a=9
print(bin(a))

#   5. Write a python script to print any number and its octal equivalent.

a=9
print(oct(a))

#   6. Write a python script to print any number and its hexadecimal equivalent.

a=987
print(hex(a))

#   7. Write a python script to store binary number 1100101 in a variable and print it in
#      decimal format.

x=0b1100101
print(int(x))

#   8. Write a python script to store a hexadecimal number 2F in a variable and print it in
#      octal format.

x=0x2F
print(oct(x))

#     9. Write a python script to store an octal number 125 in a variable and print it in binary
#        format.

x=0o125
print(bin(x))

#    10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
#        display the result in binary format.


a=0o25
b=0x39
print(bin(a+b))
