import matplotlib.pyplot as plt

n = int(input("Insert number of variables: "))
x_label = str(input("X axis label: "))
y_label = str(input("Y axis label: "))
title = str(input("Graph title: "))

v = {}
v_percent = [0.0]*n
s = []

for i in range(n):
    var_name = str(input("Insert variable "+str(i)+" name: "))
    var_value = float(input("Insert variable "+str(i)+" value: "))
    v[var_name] = var_value
    s.append(var_value)

print(v)
x = list(v.keys())
y = list(v.values())

total = 0

for i in range(0,len(s)):
    total = total + s[i]

print(total)


for i in range(0, len(v)):
    var_percent = (s[i]/total)*100
    print(var_percent)
    v_percent[i] = var_percent

v_percent.sort(reverse=True)
x.sort(reverse=True)
y.sort(reverse=True)

print(v_percent)

plt.bar(x, v_percent, color ='blue')
plt.xlabel(())

fig = plt.figure(figsize = (10, 5))

plt.bar(x, y, color ='blue', width = 0.4)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.show()