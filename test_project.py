__author__ = 'samarthshah'
from project import Project
import json
ok_now = Project('testspe')
ok_now.shoot_lazy()
#

# foodList=[]
# with open('Food/american.txt', 'r') as r:
#     for line in r.readlines():
#         foodList = line.split(' and ')
#

# restaurantList = []
# with open('Files/restaurants_list.txt', 'r') as r:
#     for line in r.readlines():
#         restaurantList = json.loads(line)
#         print 'Res list = ',restaurantList
#
# for i in range(len(restaurantList)):
#     print restaurantList[i]
#
# restaurant_set = set()
# title_case = []
# with open('Files/restaurants.txt', 'r') as r:
#     for line in r.readlines():
#         for item in line.split(','):
#             print item.split(' '), len(item.split(' '))<4
#             if len(item)>4 and len(item.split(' '))<4:
#                 print 'true'
#                 restaurant_set.add(item.strip())
#
# print 'set', restaurant_set
# for word in restaurant_set:
#     title_case.append(word.title())
#
# writeit = sorted(title_case, key=len)
# with open('Files/restaurants_list.txt', 'w') as w:
#     for n in writeit:
#         w.write(n + '\n')
