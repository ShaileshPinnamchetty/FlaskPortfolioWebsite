import os
print(os.path.abspath(os.path.dirname(__file__)))
print(os.getcwd())
os.chdir("../../")
print(os.getcwd())