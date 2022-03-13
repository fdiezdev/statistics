import matplotlib.pyplot as plt

n = int(input("Insert number of variables: "))
x_label = str(input("X axis label: "))
y_label = str(input("Y axis label: "))
title = str(input("Graph title: "))

# Var value
    # Name of the variable
    # Value
    # Percent

v = []
total = 0
x = []
y_percent = []
y_total = []

class vector:
    def add(name, value, percent):
        v.append([name, value, percent])


for i in range(n):
    var_name = str(input("Insert variable "+str(i)+" name: "))
    var_value = float(input("Insert variable "+str(i)+" value: "))
    vector.add(var_name, var_value, 0)

    x.append(var_name)
    y_total.append(var_value)

# We add te total values to calculate the percentage
for i in range(len(v)):
    total = total + v[i][1]

for i in range(len(v)):
    per = (v[i][1]/total)*100
    v[i][2] = per
    y_percent.append(per)

y_percent.sort(reverse=True)
y_total.sort(reverse=True)

print("v = ", v)
print("Total: ", total)
print("Vector length: ", len(v))


plt.bar(x, y_percent, color ='blue', width = 0.4)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title + " in %")

fig = plt.figure(figsize = (10, 5))

plt.bar(x, y_total, color ='purple', width = 0.4)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.show()
