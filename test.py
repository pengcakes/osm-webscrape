from pprint import pprint
import collections



dict = collections.defaultdict(list)

dict['123'] = 123
dict['456'] = 456

dict['123'].append('test')

pprint(dict)