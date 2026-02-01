import pandas as pd
data={
    "name":["rohit","vishal","simran","vanshika","sahil"],
    "class":[10,9,8,8,10],
    "marks":[85,50,60,85,90]
}
df=pd.DataFrame(data)
print(df)
print(df.groupby("class")["marks"].mean().sort_values(ascending=True))
print(df.loc[df.groupby("class")["marks"].idxmax()])
print(df.groupby("class").filter(lambda x:x["marks"].mean()<70))
print(df.groupby("class").filter(lambda p:p["marks"].mean()>70))
print(df.groupby("name").filter(lambda y:len(y)>=2 and y["marks"].mean()>70))
#groupby().transform()ROW LEVEL COMPARISON USING GROUP LOGIC
#QUESTION WE ARE SOLVING 
#which students scored ABOVE their own class average?
#this is a class data analysis problem
df["class_average"] = df.groupby("class")["marks"].transform("mean")
print(df)
good_classes=df.groupby("class").filter(lambda x:x["marks"].mean()>70)

good_classes["class_average"]=(good_classes.groupby("class")["marks"].transform("mean"))
result=good_classes[good_classes["marks"]>good_classes["class_average"]]
print(result)