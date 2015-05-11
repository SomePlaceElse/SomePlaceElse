__author__ = 'samarthshah'
from project import Project
import json
ok_now = Project('chefPriyanka')
ok_now.shoot_eager()


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
#     w.write(json.dumps(writeit))
#
#
# foodSet=set()
# with open('Food/american.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/british.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/chinese.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/french.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/indian.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/irish.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/italian.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/japanese.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/korean.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/mexican.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/spanish.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# with open('Food/thai.txt', 'r') as r:
#     for line in r.readlines():
#         text = line[:-1]
#         words = text.strip().split(' ')
#         if len(words)<4:
#             foodSet.add(text)
#
# foodList = list(foodSet)
# for f in foodList:
#     print f
# print len(foodList)
# query = '" OR "'.join(foodList)
# print query
# print len(query)
# print type(query)
#
# i = 0
# list_of_queries = []
# while i<len(query):
#     list_of_queries.append(query[i:min(len(query), i+460)])
#     i+=460
#
# for ls in list_of_queries:
#     print ls
#     print len(ls)
#
# with open('Files/queries.txt', 'w') as w:
#     for ls in list_of_queries:
#         w.write(ls + '\n')
#


