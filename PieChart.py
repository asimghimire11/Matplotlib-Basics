import matplotlib.pyplot as mat
stu_result = ['I Division','II Division','III Division','Supplementary','Fail']
stu_values = [100, 234, 189, 34, 12]
mat.figure(figsize=(8,6))
mat.pie(stu_values, labels=stu_result, startangle=25, explode=[0.1,0.1,0.1,0.1,0.1], colors=['red','green','blue','yellow','cyan'],shadow=True,autopct="%2.1f%%")
mat.legend(loc='upper left')
mat.title('Student Result')
mat.show()
