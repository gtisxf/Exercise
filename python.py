cars = ["🚗", "🚗", "0"]

a = 10
def test():
    a =1
    a = a + 1
    print(a)
test()
print(a)


import json
cars_json=json.dumps(cars,indent=2)
print(cars_json)