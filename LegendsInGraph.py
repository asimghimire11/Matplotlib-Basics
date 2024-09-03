import matplotlib.pyplot as mat
x=[0,1,2,3,4,5,6]
y=[i**2 for i in x]
y1=[i**3 for i in x]
mat.plot(x,y,label='Product', marker='o',mfc='k',mec='y',ls='solid',lw=2,c='r')
mat.plot(x,y1, label='Sales', marker='*',mfc='k',mec='y',ls='solid',lw=2,c='b')
myfont = {'family':'Arial','size':20,'color':'red'}
myfont1 = {'family':'Arial','size':25,'color':'green'}
mat.title("Line Chart",fontdict=myfont1)
mat.xlabel("X-axis", fontdict=myfont)
mat.ylabel("Y-axis", fontdict=myfont)
mat.grid(axis='both',ls='dotted',lw=1,c='k')
mat.legend(facecolor='cyan',edgecolor='k',loc=2,shadow=True,framealpha=0.25)
mat.show()