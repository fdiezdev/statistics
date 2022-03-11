import matplotlib.pyplot as plt

n = int(input("Insert number of variables: "))
x_label = str(input("X axis label: "))
y_label = str(input("Y axis label: "))
title = str(input("Graph title: "))

v = {}
for i in range(n):
    var_name = str(input("Insert variable "+str(i)+" name: "))
    var_value = float(input("Insert variable "+str(i)+" value: "))
    v[var_name] = var_value

print(v)
x = list(v.keys())
y = list(v.values())

plt.bar(x, y, color ='blue')
plt.xlabel(())

fig = plt.figure(figsize = (10, 5))

plt.bar(x, y, color ='blue', width = 0.4)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.show()