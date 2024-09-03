import matplotlib.pyplot as mat
x=[0,1,2,3,4,5]
y=[i**2 for i in x]
x1=[i**3 for i in x]
y1=[i**4 for i in x]
# mat.subplot(1,2,1)
mat.subplot(2,1,1)
mat.plot(x,y,marker='*',mfc='k',mec='y',ms=10,ls='dashed',lw=3,c='g')
# mat.subplot(1,2,2)
mat.subplot(2,1,2)
mat.plot(x1,y1,marker='p',mfc='k',mec='y',ms=10,ls='dashed',lw=3,c='g')
myfont = {'family':'Arial','size':20,'color':'red'}
myfont1 = {'family':'Arial','size':25,'color':'green'}
mat.show()