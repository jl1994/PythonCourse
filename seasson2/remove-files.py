import os

if os.path.exists("gitlab-ci.yml"):
    print('File gitlab-ci.yml remove')
    os.remove("gitlab-ci.yml")
else:
    print('File gitlab-ci.yml not found')


os.rmdir('delete')  # Delete a dir
