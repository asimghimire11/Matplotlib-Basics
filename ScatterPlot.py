import matplotlib.pyplot as mat
x=[1,2,3,4,5,6]
y=[i*2 for i in x]
x1=[i*3 for i in x]
y1=[i**2 for i in x]
mat.scatter(x,y,marker='s',label='Product',s=10,linewidth=2,color='red',alpha=0.75)
mat.scatter(x1,y1,marker='o',label='Sales',s=10,linewidth=2,color='green',alpha=0.75)
mat.legend()
mat.show()