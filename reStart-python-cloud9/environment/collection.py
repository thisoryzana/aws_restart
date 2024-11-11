import array as arr

myArr = arr.array('i', [1,2,3])
print(type(myArr))

myCharArr = arr.array('u', ['a', 'b','c'])
print(myCharArr)
print(type(myCharArr))

# list
print('List buah :')
myBuahList = ["apple", "banana", "cherry"]
print(myBuahList)
print(type(myBuahList))

print(myBuahList[0])

group = [
    ["oryza", "nazwa", "ero"],
    ["gyu", "beom", "tae"]
    ]
     
print(group[1])     
print(group[1][2])

# Tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Dictionary
print("\nDictionary")
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

# Set
print("\nSet")
mySet = {1,2,3,4}
print(mySet)