import matplotlib.pyplot as mat
x=[0,1,2,3,4,5,6]
y=[0,1,4,9,16,25,36]
mat.plot(x,y,marker='o',mfc='k',mec='y',ls='dashed',lw=3,c='g')
myfont = {'family':'Arial','size':20,'color':'red'}
myfont1 = {'family':'Arial','size':25,'color':'green'}
mat.title("Line Chart",fontdict=myfont1)
mat.xlabel("X-axis", fontdict=myfont)
mat.ylabel("Y-axis", fontdict=myfont)
mat.grid(axis='both',ls='dotted',lw=1,c='k')
mat.show()
