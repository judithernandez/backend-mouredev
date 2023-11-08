### Type Hints ###

my_string_variable = "My String Variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# Python es de tipado dinámico

my_tiped_variable: int = "My typed String Variable" # esto es un tipado débil, no obliga a que sea un int
print(my_tiped_variable)
print(type(my_tiped_variable))

my_tiped_variable = 5
print(my_tiped_variable)
print(type(my_tiped_variable))