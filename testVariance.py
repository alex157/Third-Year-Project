import statistics

integer_list = [4,6,2,8,7]

a = statistics.mean(integer_list)
b = statistics.variance(integer_list)

print("Items on list: " + str(integer_list[0:5]))
for s in range(len(integer_list)):
    c = (a - integer_list[s])*(a - integer_list[s])
    print ("Similar artist with ID " + str(integer_list[s]) + " has variance of " + str(c))
lower = a - b
upper = a + b
print ("Min boundary: " + str(lower))
print("Mean: " + str(a))
print ("Max boundary: " + str(upper))
print("Overall variance: " + str(b))
