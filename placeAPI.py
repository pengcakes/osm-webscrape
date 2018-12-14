"""
https://github.com/slimkrazy/python-google-places

Params:
Key - AIzaSyDNAW7SKoT44fkSUzHhKWVFLcN8xn-g6Jo
Input
Inputtype

key = AIzaSyDNAW7SKoT44fkSUzHhKWVFLcN8xn-g6Jo
https://maps.googleapis.com/maps/api/place/textsearch/xml?query=restaurants+in+Sydney&key=AIzaSyDNAW7SKoT44fkSUzHhKWVFLcN8xn-g6Jo 

test: Gates Public Library
"""
# Python program to get a set of  
# places according to your search  
# query using Google Places API 
  
# importing required modules 
import requests, json, pickle
 
def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def api():
	# url variable store url 
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
	
	  
	# The text string on which to search 
	query = input('Search query: ') 
	  
	# get method of requests module 
	# return response object 
	r = requests.get(url + 'query=' + query +
	                        '&key=' + api_key) 
	  
	# json method of response object convert 
	#  json format data into python format data 
	x = r.json() 
	  
	# now x contains list of nested dictionaries 
	# we know dictionary contain key value pair 
	# store the value of result key in variable y 
	y = x['results'] 
	  
	# keep looping upto lenght of y 
	for i in range(len(y)): 
	      
	    # Print value corresponding to the 
	    # 'name' key at the ith index of y 
	    print(y[i]['name'])


api_key = 'AIzaSyDNAW7SKoT44fkSUzHhKWVFLcN8xn-g6Jo'
api()

# names = load_obj("kodak_names")
# print(names)




