"""
Image is 8000 x 8000
For Irondequoit, the lat and lon range is : 43.1759   43.2192  -77.6152  -77.5520
MODIFY CSV FILE or CHANGE AXIS FOR MAP

SAVE IMAGE AT REAL RESOLUTION
DRAW LINES B/W POINTS AND FILL IN
DIFF COLORS FOR MAJOR BUILDINGS AND SAVE INTERESTING INFO IN ANOTHER FILE
"""
import matplotlib.pyplot as plt
import pickle
import csv
from pprint import pprint

# with open('csv/test.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for x in readCSV:
#     	building_dict = x    	

# print(type(building_dict))

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

building_dict = load_obj('irondequoit')




image_name = "Vis_2017-11-30_13-55-01_08866.ntf.jpg"

im = plt.imread(image_name)


#extent=[longitude_top_left,longitude_top_right,latitude_bottom_left,latitude_top_left]
plt.imshow(im, extent=[-77.6152, -77.5520, 43.1759, 43.2192])
plt.title('Irondequoit')

count = 0

for key in building_dict:
	#print(building_dict[key][0][0][0])
	for x in range(0, len(building_dict[key])):
		if (43.1759 < building_dict[key][x][0][0] < 43.2192 and -77.6152 < building_dict[key][x][1][0] < -77.5520):
			#plt.scatter(building_dict[key][x][1][0], building_dict[key][x][0][0], c='r', s=1)
			print('plotted: ', building_dict[key][x][1][0], building_dict[key][x][0][0])


plt.show()










