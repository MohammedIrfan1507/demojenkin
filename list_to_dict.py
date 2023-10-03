firstNum = int(input("enter first element : \n"))
lastNum = int(input("enter last element : \n"))
newList = [i for i in range(firstNum, lastNum + 1)]
print("\n", newList, "\n")
newList = [num for num in range(firstNum, lastNum + 1) if num % 2 == 0]
print("\nList of even numbers\n", "\n", newList)
print("\nList to Dictionary with key as index and value as element\n")
res_dict = dict(enumerate(newList))
print(res_dict999
