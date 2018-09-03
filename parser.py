import xml.etree.ElementTree as ET

file_name = 'movies.xml'

tree = ET.parse(file_name)

root = tree.getroot()

#iterate through children
# for child in root:
# 	print(child.tag, child.attrib)

# #iterates through all 'elements' (or tags)
# for elem in root.iter():
# 	print(elem.tag)

for x in root.iter("movie"):
	print(x.attrib)

#####PRINT ALL
#print(ET.tostring(root, encoding='utf8').decode('utf8'))



####SELECT

# for movie in root.findall("./genre/decade/movie/[year='1992']"):
#     print(movie.attrib)


# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
#     print(movie.attrib)