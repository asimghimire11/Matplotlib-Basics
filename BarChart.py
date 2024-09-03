import matplotlib.pyplot as mat
x = [2019,2020,2021,2022,2023]
y = [4000,2200,3000,3500,4200]
mat.xlabel('Year')
mat.ylabel('Sales')
mat.title('Sales Detail(5 years)')
mycolor=['red','green','blue','black','yellow']
mat.bar(x,y,width=0.6,color=mycolor)
# mat.barh(x,y,height=0.6,color=mycolor)
mat.show()
