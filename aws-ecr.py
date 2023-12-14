import docker
import subprocess
import re

# Log in to the ECR registry
client = docker.from_env()
client.login(username="username", password=password, registry=registry)