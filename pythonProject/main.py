import json
with open("pythonProject/OOP", "r") as fileobject:
    data = json.load(fileobject)



print(data[0]["tags"])
print(data[0]["address"])
print(data[0]["friends"][0]["id"])
print(data[0]["friends"][0]["name"])
print(data[0]["friends"][1]["id"])
print(data[0]["friends"][1]["name"])
print(data[0]["friends"][2]["id"])
print(data[0]["friends"][2]["name"])



print(data[1]["tags"])
print(data[1]["address"])
print(data[1]["friends"][0]["id"])
print(data[1]["friends"][0]["name"])
print(data[1]["friends"][1]["id"])
print(data[1]["friends"][1]["name"])
print(data[1]["friends"][2]["id"])
print(data[1]["friends"][2]["name"])


print(data[2]["tags"])
print(data[2]["address"])
print(data[2]["friends"][0]["id"])
print(data[2]["friends"][0]["name"])
print(data[2]["friends"][1]["id"])
print(data[2]["friends"][1]["name"])
print(data[2]["friends"][2]["id"])
print(data[2]["friends"][2]["name"])