
# coding: utf-8

# ## 1) Write a python program which creates a class named Cone and write a function calculate_area which calculates the area of the Cone.

# In[1]:


import math
class Cone:
    def __init__(self, r,h):
        self.r = r
        self.h=h
        self.area = 0
        self.pi=3.14
    def Area(self):
        self.l = math.sqrt(self.r * self.r + self.h * self.h)
 
    # Calculate the Surface Area
        self.area = self.pi * self.r * (self.r + self.l)
        
        return self.area

def main():
    r = float(input("Please enter the radius of the cone:"))
    h = float(input(" Please enter the height of the cone:"))
    s=Cone(r,h)
    s.Area()
    print('Area of a cone with radius:{} and height:{} is: '.format(r,h),s.Area())

if __name__ == '__main__':
    
    main()


# ## 2) Define a class MathOperation which implements pow(x,n) without using python's in-built pow() method

# In[4]:


def power(a,b):
    res = 1
    if b==0:
        return 1
    if b>0:
        for i in range(b):
            res *= a
        return res
    else:
        return 1./float(power(a,-b))


print(power(-2,5))


# In[17]:


class MathOp:
    def __init__(self):
        pass
        
    def power(self,x,y):
        self.x = x
        self.y= y
        if(self.y == 0):
            return 1
        self.temp = power(self.x, int(self.y / 2))
        
        if (self.y % 2 == 0):
            return self.temp * self.temp
        else:
            if(self.y > 0):
                return self.x * self.temp * self.temp
            else:
                return (self.temp * self.temp) / self.x
        
M=MathOp()
print(M.power(2, 3))
print(M.power(5, -3))
print(M.power(-2, 5)) 
print(M.power(-5, -3))
print(M.power(20000,0)) 


# ## 3) Write a python program that creates a class Base and Derived. Use inbuilt function issubclass and isinstance which gives boolean results.(True or False)
# 

# In[44]:


class Base:
    pass 
 
class Derived(Base):
    pass  
 
print(' Derived class is a subclass of Base class which will return ',issubclass(Derived, Base))
print(' Base class is a subclass of Derived class which will return ',issubclass(Base, Derived))
 
d = Derived()
b = Base()
print('Base class is an  instance of Derived class which will return',isinstance(b, Derived))
print('Derived class is an instance of Base class which will return ',isinstance(d, Base))


# ## 4) Write a python program that creates base class Person which has two methods    def __init__(self, first, last)    def __str__(self)
#     Also create a derived class named Employee which uses the base class method “def __str__(self)” using “super()” to concatenate first name wit h last name

# In[43]:


class Person:
    def __init__(self,first,last): 
        self.first=first
        self.last=last
           
    def __str__(self):
        return self.first+ self.last
class Employee(Person):
    
    def __init__(self,first,last):
        super().__init__(first,last)
                
dev_1=Employee('JeevaNandam ','B')

dev_1.__str__()

