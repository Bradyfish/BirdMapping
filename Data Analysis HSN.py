import pandas
import matplotlib.pyplot as plt
import os
directory = 'C:\\Users\\logan\\Desktop\\python_work\\Data'


for filename in os.listdir(directory):
	if filename.endswith(".csv"):
		os.chdir('C:\\Users\\logan\\Desktop\\python_work\\Data')
		data = pandas.read_csv(filename)
		x = []
		for i in data['Year']:
			x.append(i-1997)
		
		y = []
		for i in data['Nesting Success Rate']:
			y.append(i)
		if x==[]:
			name = f"{filename.replace('.csv','')}_empty"
		else:
			name = filename.replace('.csv','')
		fig, ax=plt.subplots()
		ax.plot(x,y)
		plt.xlabel('Years since 1997')
		plt.ylabel('Success Rate as a Percent')
		plt.title(f'Success of {name}')
		os.chdir('C:\\Users\\logan\\Desktop\\python_work\\Plots')
		fig.savefig(f'{name} Plot.png')
		plt.close(fig)
		'''
		plt.plot(x,y)
		plt.xlabel('Years since 1997')
		plt.ylabel('Success Rate as a Percent')
		
		plt.title(f'Success of {name}')
		os.chdir('C:\\Users\\logan\\Desktop\\python_work\\Plots')
		plt.savefig(f'{name} Plot.png')
		'''
		
	
'''		

data = pandas.read_csv('AK_Eastern Bluebird.csv')
x = []
for i in data['Year']:
	x.append(i-1997)
	
y = []
for i in data['Nesting Success Rate']:
	y.append(i)
print(x)
print(y)
plt.plot(x,y,'g')
plt.xlabel('Years since 1997')
plt.ylabel('Success Rate as a Percent')
plt.title('Success of AK Eastern Bluebird')
os.chdir('C:\\Users\\logan\\Desktop\\python_work\\Plots')
plt.savefig('AK_Eastern Bluebird Plot.png')

'''
