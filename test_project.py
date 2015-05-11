__author__ = 'samarthshah'
from project import Project
import json
ok_now = Project('testspe')
ok_now.shoot_lazy()

# restaurantList = []
# with open('Files/restaurants_list.txt', 'r') as r:
#     for line in r.readlines():
#         restaurantList = json.loads(line)
#         print 'Res list = ',restaurantList
#
# for i in range(len(restaurantList)):
#     print restaurantList[i]
# restaurant_list, title_case = [], []
# with open('Files/restaurants.txt', 'r') as r:
#     for line in r.readlines():
#         for item in line.split(','):
#             if len(item)>4:
#                 restaurant_list.append(item.strip())
#
# print 'list', restaurant_list
# for word in restaurant_list:
#     title_case.append(word.title())
#
# print title_case
# with open('Files/restaurants_list.txt', 'w') as w:
#     w.write(json.dumps(title_case))
