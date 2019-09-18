# single variable
var_string = "Hello World"
var_integer = 10
var_float = 3.14
var_boolean = True
VAR_TETAP = 30

print (var_string)
print (var_integer)
print (var_float)
print (var_boolean)


# multiple variable
a, b, c = 2, 25, 'abc'
print (a,b,c)


print ("\n")

print ("Data Type:")
print ("variable var_string adalah: ", type(var_string))
print ("variable var_integer adalah: ", type(var_integer))
print ("variable var_float adalah: ", type(var_float))
print ("variable var_boolean adalah: ", type(var_boolean))

print ("\n")
print ("Menghapus Variable")
a = 10
print (a)
try:
    del a
    print (a)
except NameError: # handle error
    print("Variable a belum terdeklarasi")

