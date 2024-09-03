import matplotlib.pyplot as mat
x=[0,1,2,3,4,5]
y=[0,1,4,9,16,25]
mat.plot(x,y, marker='h', mfc='y',mec='k',ms=10,ls='dashed',lw=2,c='k')
myfont = {'family':'Arial','size':20,'color':'red'}
myfont1 = {'family':'Arial','size':25,'color':'green'}
mat.title("Line Chart",fontdict=myfont1)
mat.xlabel("X-axis", fontdict=myfont)
mat.ylabel("Y-axis", fontdict=myfont)
mat.show()

