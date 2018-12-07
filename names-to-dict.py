import pickle
import pprint
import csv


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


d = load_obj('irondequoit')
important = load_obj('important_irondequoit')
building_names = load_obj('names_irondequoit')

# pprint.pprint(important)
# pprint.pprint(building_names)

x = len(building_names)
count = 0

for key,val in building_names.items():
    if key in d:
    	d[key] = [val, d[key]]

#writes key to each row
savefile = 'csv/all_irondequoit.csv'
with open(savefile, 'w') as file:
	writer = csv.writer(file)
	for key, values in d.items():
		writer.writerow([key, values])
	print('finished writing to: ', savefile)