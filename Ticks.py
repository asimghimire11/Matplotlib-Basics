import matplotlib.pyplot as mat
x=[0,10,20,30,40,50]
y=[i*10 for i in x]
mat.plot(x,y,color='k')
mat.title('Product-Sales Details')
mat.xlabel('Product')
mat.ylabel('Sales')
# mat.xticks(x,['A','B','C','D','E','F'])
# mat.yticks(y,['0','1','2','3','4','5'])
mat.xlim(0,60)
mat.ylim(0,600)
mat.show()