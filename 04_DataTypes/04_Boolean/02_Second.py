# Empty string will be treated as False boolean data type in condirional case
name = ""

if(name):
    print(name)
else:
    print("name is required")
# here else will execute because name has empty string and empty string will be evaluated as False
# Result --> name is required