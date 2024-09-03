import matplotlib.pyplot as mat
product_price = [10,20,25,30,35,40,50,48,96,78,56,60,89,120,135,150,160,256,260,270,358]
product_range = [0,30,50,100,200,300,400]
mat.hist(product_price,product_range, facecolor='r',rwidth=0.8,histtype='step')
mat.title('Product Details')
mat.xlabel('Product Price')
mat.ylabel('Product Range')
mat.show()