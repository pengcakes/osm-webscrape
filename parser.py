import xml.etree.ElementTree as ET

file_name = 'searsT.osm'

tree = ET.parse(file_name)

root = tree.getroot()

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
#     print(movie.attrib, movie.text)

# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
#     print(movie.attrib)

####################################RETURN ALL BUILDING HEIGHTS
for x in root.findall("./way/tag/[building:height]"):
	print(x.attrib)

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

