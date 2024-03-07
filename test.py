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

#array
#equal to
#list
color = ["white", "red", "black", "blue"]
number = [1,1,4,2,3]
print(color)
print(number)
#add
color.append("pink")
print(color)

#travel the list
# for(i=0;color.len;i++)
#   let temp = color[i];
#   console.log(temp)
for i in color:
    print(i)
for i in number:
    print(i)

print(color[0])

#dictionary
me={
    "first name": "Fernanda",
    "last name": "Ugalde",
    "age": 20
}
print(me["first name"])

me["age"] = 99
me["color"]="blue"
print(me)