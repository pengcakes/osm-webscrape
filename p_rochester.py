"""
Search for:
<way> --> <tag k = "building:height" v = "184">. </way>
k="building:height"
k="building:levels"

DATASET:

BUILDING NAME: [id, height, lat[], long[]]

FIND WAY TO MATH ND REFS TO BUILDING ID


For Irondequoit, the lat and lon range is : 43.1759   43.2192  -77.6152  -77.5520

For elmgroove, the lat and lon range is : 43.1342   43.1763  -77.7752  -77.7133


"""
import xml.etree.ElementTree as ET
import time
start = time.time()

file_name = 'osm/irontest.osm'
#file_name = 'osm/movies.xml'

tree = ET.parse(file_name)
root = tree.getroot()

building_dict = {}
building_data = []
building_id = []

#returns nodes
#not optimized even a little, spaget but it works
#try using .clear() function maybe?
def nd_parse():

	node_ref = []
	count = 0
	for i in building_id:
		if(count>0):
			node_ref.append(temp_list)
		count+=1
		temp_list = []
		for x in root.findall("way[@id='{buidling_id}']/nd".format(buidling_id=i)):
			temp_list.append(x.attrib['ref'])
	
	return node_ref


#uses nodes to find lat long
#holy big o^3
def get_latlong():
	var = nd_parse()
	latitude = []
	longitude = []
	count = 0
	for i in var:
		for x in i:
			for j in root.findall("node[@id='{z}']".format(z = x)):
				latitude.append((j.attrib['lat']))
				longitude.append((j.attrib['lon']))
	
	return latitude, longitude

def parse():
	#get building id
	for x in root.findall("way/tag[@k='building']..."):
		building_id.append(x.attrib['id'])

	temp = get_latlong()

	print(temp)

	#add lat arr and long arr to building_dict
	for x in range(0, len(building_id)):
		building_dict[building_id[x]] = [x]

	return building_dict


parse()
for x in building_dict:
	print(x, building_dict[x])

# my_dict = {1: 'apple', 2: 'ball'}
# my_dict[3] = ["pie", 5]
# for x in my_dict:
# 	print(x, my_dict[x])


end = time.time()
print(round(end - start, 5))

# var = nd_parse()

# test = var[0][0]

# print(len(var))

# for x in root.findall("node[@id='{z}']".format(z = test)):
# 	print(x.attrib['lat'])
# 	print(x.attrib['lon'])


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

