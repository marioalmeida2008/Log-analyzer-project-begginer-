file = open("auth.log")

for line in file:
   if "Failed password" in line:
    print(line)