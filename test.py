print("Hello world!")

# let variable = 21; 
name = "Fernanda"
last_name = "Ugalde"
total = 12.99
age = 20
found = True

# if / else statement
# if(var1==var2){
# logic
# }
if age < 100:
    print("dont worry youre not that old")
elif age == 100:
    print("congratz your'e a century")
else: 
    print("sorry, seems that your'e old!")

#function
# function say_hello(){}
    
def say_hello():
    print("hello there")
def say_goodbye(name):
    print("goodbye "+ name)

#call a function
say_hello()
say_goodbye(name)

#concatenate
print("Hello my name is "+name+"and i have "+str(age)+" years old")