"""
Search for:
<way> --> <tag k = "building:height" v = "184">. </way>
k="building:height"
k="building:levels"
"""
import xml.etree.ElementTree as ET

file_name = 'searsT.osm'
#file_name = 'movies.xml'

tree = ET.parse(file_name)
root = tree.getroot()

building_heights = []
building_names = []
building_dict = {}

#find building height
for child in root.findall("way/tag[@k='building:height']"):
	building_heights.append(child.attrib['v'])

#get building names
for child in root.findall("way/tag[@k='building:height'].../tag[@k='name']"):
	building_names.append(child.attrib['v'])



for i in range(len(building_heights)):
	building_dict[building_names[i]] = building_heights[i]

for x in building_dict:
	print(x, building_dict[x])


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

