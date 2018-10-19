"""
Search for:
<way> --> <tag k = "building:height" v = "184">. </way>
k="building:height"
k="building:levels"

BUILDING NAME: [id, height, latlong[]]

also needs to write to .csv file
"""
import xml.etree.ElementTree as ET
import time
import csv
from pprint import pprint
start = time.time()



file_name = 'osm/searsT.osm'

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
	#get building height
	for x in root.findall("way/tag[@k='building:height']"):
		building_heights.append(x.attrib['v'])

	#get building names
	for x in root.findall("way/tag[@k='building:height'].../tag[@k='name']"):
		building_names.append(x.attrib['v'])

	#get building id
	for x in root.findall("way/tag[@k='building:height']..."):
		building_id.append(x.attrib['id'])

	temp = get_latlong()


	#add data to building_dict
	for x in range(len(building_heights)):

		building_dict.update( {building_names[x] : [building_id[x], building_heights[x], temp[x]]} )

	return building_dict


parse()
pprint(building_dict)


filename = 'csv/searsT.csv'
with open(filename, 'w') as file:
	writer = csv.writer(file)
	for key, values in building_dict.items():
		writer.writerow([key, values])
	print('finished writing to: ', filename)


end = time.time()
print(round(end - start, 5))
















##################################################################
# SANDBOX

# ###iterate through children
# for child in root:
# 	print(child.tag, child.attrib)

# ###iterates through all 'elements' (or tags)
# for elem in root.iter():
# 	print(elem.tag)


# ####SHOW ATTRIBs FOR TAG
# ###can exchange for "movie", "description"
# for x in root.iter("way"):
# 	print(x.attrib)

####PRINT ALL
#print(ET.tostring(root, encoding='utf8').decode('utf8'))

####SELECT BASED ON TAG

# for movie in root.findall("./genre/decade/movie/[year='1992']"):
#     print(movie.attrib)

# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
# 	myList.append(movie)
# 	print(movie.attrib, movie.text)

# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
#     print(movie.attrib)


####MODIFYING
# b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
# print(b2tf)

# b2tf.attrib["title"] = "Back to the Future"
# print(b2tf.attrib)

####WRITING CHANGES
###SAVE WITH WRITE
# tree.write("movies.xml")

# for x in root.iter('movie'):
# 	print(x.attrib)

###Fixing Attributes

# for form in root.findall("./genre/decade/movie/format"):
#     print(form.attrib, form.text)

