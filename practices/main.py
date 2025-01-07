text = input("Write something: ")
print(text)

set1 = {1, 1, 2, 1, 5, 2, 1, 1, 1, 2, 2}
unique = 0
def return_unique(a_set):
  item = 0
  for i in a_set:
    if i != item:
      item = i
  return item

unique = return_unique(set1)
print("unique: ", unique)