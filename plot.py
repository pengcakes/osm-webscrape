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
import time
import csv
from pprint import pprint
start = time.time()


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

building_dict = load_obj('important_irondequoit')


dpi = 80
im = plt.imread("images/Vis_2017-11-30_13-55-01_08866.ntf.jpg")
height, width, n = im.shape

# figsize = width/float(dpi), height/float(dpi)
# fig = plt.figure(figsize=figsize)
# ax = fig.add_axes([0,0,1,1])
# ax.axis('off')
# ax.imshow(im, interpolation='nearest')
# fig.savefig('test.jpg', dpi=dpi, transparent=True)


plt.imshow(im, extent=[-77.6152, -77.5520, 43.1759, 43.2192])
plt.axis('off')
bcount = 0
for key in building_dict:
	bcount+=1
	print(bcount, '\n\n')
	for x in range(0, len(building_dict[key])):
		plt.scatter(building_dict[key][x][1][0], building_dict[key][x][0][0], c='r', s=1)
		print('plotted: ', building_dict[key][x][1][0], building_dict[key][x][0][0])
		
		# if (43.1759 < building_dict[key][x][0][0] < 43.2192 and -77.6152 < building_dict[key][x][1][0] < -77.5520):
		# 	plt.scattfsdsdfer(building_dict[key][x][1][0], building_dict[key][x][0][0], c='r', s=1)
		# 	print('plotted: ', building_dict[key][x][1][0], building_dict[key][x][0][0])

print(bcount)

plt.savefig('images/important.png')
plt.show()




end = time.time()
print(round(end - start, 5))







