'''
#Type checking
a = 10
b = 5.6
c = "Tom"
d = [1,2]
e = (9,1,2,3)
f = {1,2,3,4}
g = {"name": "Tom"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,list))
print(isinstance(e,tuple))
print(isinstance(f,set))
print(isinstance(g,dict))
'''

#Duck Typing
class Duck:
    def quack(self):
        print("Quack, quack!")
class Person:
    def quack(self):
        print("I'm quacking like a duck!")
def in_the_forest(duck):
    duck.quack()
d = Duck()
p = Person()
in_the_forest(d)  
in_the_forest(p)  