#2.1.1- Scope Rules
def update(n,x):
    n=2
    x.append(4)
    print('update: ',n,x)

def main():
    n=1
    x=[0,1,2,3]
    print('main: ',n,x)
    update(n,x)
    print('main: ',n,x)

main()


#2.1.2- Classes and OOP
class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))

#Question 1
class NewList(list):
    def remove_max(self):
        self.remove(max(self))
    def append_sum(self):
        self.append(sum(self))

x = NewList([1,2,3])
while max(x) < 10:
    x.remove_max()
    x.append_sum()

print(x)


#2.2.2: Slicing NumPy Arrays
import numpy as np
x=np.array([1,2,3])
y=np.array([2,4,6])
X=np.array([[1,2,3],[4,5,6]])
Y=np.array([[2,4,6],[8,10,12]])
