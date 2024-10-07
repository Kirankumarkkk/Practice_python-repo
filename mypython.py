print("hello world")
first_name = "kiran"
last_name="kumar"
full_name=first_name+" "+last_name
print("hello "+ full_name)
print(type(full_name))

age=28
age=age+1
print(age)
age*=1
print(age)

message="kiran's pen"
print(message)
message="kiran\'s desk"
print(message)
message="""hello
kiran kumar kkk"""
message='hello world'
print(message)
print(len(message))
print(message[0:2])
print(message[-2:])

print(message[:5])  #starting 0 to 5 th index print
print(message[6:])  #starting 6 to end of the index string print
print(message[3:6]) #start from 3 and stop at 6 index
print(message.lower())  #lower case
print(message.upper())  #upper case
print(message.count('l')) #show count of l letter in the string
print(message.find('world')) #show the index where it start
print(message.find('z')) #this will print -1 since z not present in index
message.replace('hello', 'hi') #replacement isn't happening
print(message)
new_message=message.replace('hello', 'hi')  #assigned new variable hello to hi
print(new_message)
message=message.replace('hi', 'hello') #replacing again hi to hello
print(message)

greeting='hello'
name='kiran'
last_name='kumar'
greeting_name='{}, {} {}.  welcome!'.format(greeting,name,last_name)  #format strings

#instead of greeting_name=greeting+,''+name+ last_name. welcome!
print(greeting_name)

def fun_name1(name, age):
	print(f"hello" + " "+name + " " + {age}")

fun_name1("kiran",28)