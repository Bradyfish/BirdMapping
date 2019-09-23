
import pandas
data=pandas.read_csv('newdata.csv')
states = pandas.read_csv('states.csv')
symbols = states['Code']

speciesData = data['Species']
species = set()
for thing in speciesData:
	species.add(thing)

for item in species:
	newdata = data[data['Species']==item]
	for symbol in symbols:
		newdata[newdata['Location']==symbol].to_csv(f"{symbol}_{item.replace('/',' ')}.csv")
