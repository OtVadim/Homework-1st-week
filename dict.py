d = {"city": "Москва", "temperature": "20"}
print(d["city"])
print(int(d["temperature"]) - int(5))
print(d)

print(d.get("Country", "Россия"))
d["date"] = "27.05.2019"
print(len(d))