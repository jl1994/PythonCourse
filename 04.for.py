devops = ['johan', 'jarminson', 'edgar', 'natalia']
password = "123456"

for i in devops:
    print(i)

for i in password:
    print(i)

# For Range
for i in range(0, 101, 50):
    print(i)

# Doble for para iterar devops + password
for i in devops:
    for j in password:
        print(i, j)
