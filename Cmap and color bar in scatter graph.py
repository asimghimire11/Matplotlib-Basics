import matplotlib.pyplot as mat
x=[1,2,3,4,5,6]
y=[i*2 for i in x]
y1=[i**3 for i in x]
# mycolor=['red','yellow','green','cyan','blue','black']
mycolor=[10,20,30,40,50,60]
mysize=[10,20,30,40,50,60]
mat.scatter(x,y,c=mycolor,cmap='Greys',s=mysize)
mat.colorbar()
mat.scatter(x,y1,color='orange',s=80)
mat.show()