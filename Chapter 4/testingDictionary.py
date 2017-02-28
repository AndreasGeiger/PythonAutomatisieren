items = {"First": 22, "Second": "What?", "Test": "Yeah", 323: "Test2"}

for k, v in items.items():
    print(str(k) + " " + str(v))

for v in items.values():
    print(str(v))

for k in items.keys():
    print(str(k))
