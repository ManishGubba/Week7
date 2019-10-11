#pushbike
import pandas as pd

lst = ["I", "got", "a", "brand", "new", "pushbike"]

print(lst)

df = pd.DataFrame(lst, index = ['a','b','c','d','e','f'], columns = ["Words"])

#print(df)

lst2 = [11, 22, 33, 44, 55, 66]

df2 = pd.DataFrame([lst,lst2])
#print (df2)

df3 = pd.DataFrame(list(zip(lst,lst2)), columns = ["Words", "Values"])

print (df3)