cicd = open(".gitlab-ci.yml", 'r')  # This is a function
# print(cicd.read())
print(cicd.readline())

for i in cicd:
    print(i)

# print(cicd.readline())
# print(cicd.readline())

cicd.close()
