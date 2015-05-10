
# coding: utf-8

# In[1]:

import Orange


with open('itemSet.txt'):
    print 'cds'


raw_data = ["Burger, Pizza, Tandoori Chicken",
        "Pizza, noodles, Tacos",
        "Burger, Pasta", 
        "Burger, Pizza, noodles",
        "Burger, Tandoori Chicken, Pasta",
        "Pizza, Tandoori Chicken"]



# write data to the text file: data.basket
f = open('food.basket', 'w')
for item in raw_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("food.basket")


# Identify association rules with supports at least 0.3
rules = Orange.associate.AssociationRulesSparseInducer(data, support=0.2)


# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

rule = rules[0]
for index, d in enumerate(data):
    print '\nUser {0}: {1}'.format(index, raw_data[idx])
    for r in rules:
        if r.applies_left(d) and not r.applies_right(d):
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

