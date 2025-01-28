# Array
fruits = ["apple", "orange", "banana"]
in_banana = "banana" in fruits
print(f"Is banana include? : {in_banana}")
print("Is banana include? : {}".format("banana" in fruits))

# Tuple
x, _, _, *y = (1, -1, 0, 2, 5, )
print(f"Unpacking from Tuple, x: {x}, y: {y}")
x, y = y, x
print(f"Swap, x: {x}, y: {y}")

# Dictionary
dic = {"seoul" : 10, "swon" : True}
del dic["swon"]
print("Get swon : {}".format(dic.get("swon", "알수없음")))

# Set
fruits_1 = {"apple", "orange", "banana"}
fruits_2 = {"apple", "grapse", "pitch"}
print(fruits_1 | fruits_2)
print(fruits_1 & fruits_2)
print(fruits_1 - fruits_2)