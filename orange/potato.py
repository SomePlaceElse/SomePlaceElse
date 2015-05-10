import Orange

# Load data from the text file: data.basket
data = Orange.data.Table("data.basket")

# Identify association rules with supports at least 0.3
# Since our basket is sparse.
rules = Orange.associate.AssociationRulesSparseInducer(data, support=0.3)


# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

print 'Rules ', rules
print 'Rules[0] ', rules[0]
rule = rules[0]
for index, d in enumerate(data):
    # print '\nUser {0}: {1}'.format(index, raw_data[idx])
    for r in rules:
        if r.applies_left(d) and not r.applies_right(d):
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

# Now set a minimum threshold on confidence. i.e. 0.5 50% of the time the rule is correct
# We can also optimize it y considering only those set of rules where user is concerned
# set a minRules and maxRules so that if the # of rules returned = maxRules, it means the support is too low.
# vice versa for minRules
