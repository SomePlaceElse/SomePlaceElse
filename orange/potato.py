import Orange, json
from Orange.testing.unit.tests.test_table import native

SUPPORT = 0.4
ranked_recommendations = {}
# Load data from the text file: data.basket
data = Orange.data.Table("data.basket")

# Identify association rules with supports at least 0.4
# Since our basket is sparse.
rules = Orange.associate.AssociationRulesSparseInducer(data, support=SUPPORT)


# print out rules
# print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
# for rule in rules[:]:
#     print "%4.1f %4.1f  %s" % (rule.support, rule.confidence, rule)

print
print
with open('number_of_rules.txt', 'a') as a:
    a.write(json.dumps((SUPPORT, len(rules))) + ',')       # Records the support and number of rules created
print
print
print 'RECOMMENDATIONS'

data_instance = data[len(data)-1]   # The last item in the bucket is the one of userinput!
print 'User data',data_instance
for rule in rules:
    if rule.applies_left(data_instance) and not rule.applies_right(data_instance):
        rec_list = rule.right.get_metas(str).keys()
        for item in rec_list:
            if ranked_recommendations.has_key(item):
                ranked_recommendations[item] += 1
            else:
                ranked_recommendations[item] = 1
print ranked_recommendations

        # print "%4.1f %4.1f  %s" % (rule.support, rule.confidence, rule)

        # Now set a minimum threshold on confidence. i.e. 0.5 50% of the time the rule is correct
        # We can also optimize it y considering only those set of rules where user is concerned
        # set a minRules and maxRules so that if the # of rules returned = maxRules, it means the support is too low.
        # vice versa for minRules

        # Calculate the rules after new data_instance of XYZ is added
        # for rule in rules:
        #   if rule.applies_left(data_instance):
        #         recommendationList.append(rule.right) // rule.right in the form of Orange.data.Instance
        #