"""
Search for:
<way> --> <tag k = "building:height" v = "184">. </way>
k="building:height"
k="building:levels"

id: latlong[]

For Irondequoit, the lat and lon range is : 43.1759   43.2192  -77.6152  -77.5520

For elmgroove, the lat and lon range is : 43.1342   43.1763  -77.7752  -77.7133


"""
import xml.etree.ElementTree as ET
import time
import csv
from pprint import pprint
start = time.time()



file_name = 'osm/irondequoit.osm'

tree = ET.parse(file_name)
root = tree.getroot()

building_dict = {}

building_id = []
building_heights = []
building_names = []


def printArr(array):
	for x in array:
		print(x, '\n')


#not optimized even a little, spaget but it works
#used in get_latlong()
#try using .clear() function maybe?
def nd_parse():

	node_dictionary = []

	for i in building_id:

		temp_list = [] #makes new temp w/ each run

		for x in root.findall("way[@id='{buidling_id}']/nd".format(buidling_id=i)):
			temp_list.append(x.attrib['ref'])
		
		node_dictionary.append(temp_list)

	return node_dictionary

#holy big o^3
#used in parse()
def get_latlong():
	node_dictionary = nd_parse()

	# test_dict = []
	# test_dict.append(node_dictionary[0])
	# test_dict.append(node_dictionary[1])
	# test_dict.append(node_dictionary[2])

	building_locations = []
	
	for node in node_dictionary:
		temp=[]
		for data in node:
			latitude=[]
			longitude=[]
			for location in root.findall("node[@id='{z}']".format(z = data)):
				latitude.append((location.attrib['lat']))
				longitude.append((location.attrib['lon']))
			combined = [latitude, longitude]
			temp.append(combined)

		building_locations.append(temp)	


	return building_locations

def parse():
	#get building id
	for x in root.findall("way/tag[@k='building']..."):
		building_id.append(x.attrib['id'])

	temp = get_latlong()


	#add data to building_dict
	for x in range(len(building_id)):

		building_dict.update( {building_id[x] :  temp[x]} )

	return building_dict


parse()
pprint(building_dict)


filename = 'csv/irondequoit.csv'
with open(filename, 'w') as file:
	writer = csv.writer(file)
	for key, values in building_dict.items():
		writer.writerow([key, values])
	print('finished writing to: ', filename)


end = time.time()
print(round(end - start, 5))

