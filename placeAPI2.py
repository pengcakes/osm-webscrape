"""
Kodack Park
43.1342   43.1763
-77.7752  -77.7133

Home
43.127374, -77.641362
"""

from googleplaces import GooglePlaces, types, lang

api_key = 'AIzaSyDNAW7SKoT44fkSUzHhKWVFLcN8xn-g6Jo'
google_places = GooglePlaces(api_key)

query_result = google_places.nearby_search(
        lat_lng={'lat': 43.127374, 'lng': -77.641362}, 
        radius=1000,
        types=[types.TYPE_RESTAURANT] or [types.TYPE_CAFE] or [types.TYPE_LIBRARY])

for place in query_result.places:
     place.get_details()
     print('%s %s %s %s %s %s %s \n\n' % (place.name, place.geo_location, place.types, place.get_details, place.local_phone_number, place.website, place.url))
