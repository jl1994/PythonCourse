cicd = open(".gitlab-ci.yml", "w")

cicd.write(f"\nAuthor: Johan Luna \nMail: johanluna777@gmail.com")

for i in cicd:
    print(i)
    
cicd.close()

# # cicd = open(".gitlab-ci.yml", "r")
# cicd = open(".gitlab-ci.yml", "a")

# cicd.write(f"\nAuthor: Johan Luna \nMail: johanluna777@gmail.com")


# cicd.close()

# cicd = open(".gitlab-ci.yml", 'r')  # This is a function
# # print(cicd.read())
# print(cicd.readline())

# for i in cicd:
#     print(i)

# # print(cicd.readline())
# # print(cicd.readline())

# cicd.close()
