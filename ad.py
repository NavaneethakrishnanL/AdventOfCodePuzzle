import math
import pandas as pd
file = open("adv.txt")
df=pd.DataFrame(columns=['Adv','result'])
df1=pd.DataFrame(columns=['res'])
df2=pd.DataFrame(columns=['new'])
for row in file:
    adv=row
    df=df.append({'Adv':adv}, ignore_index=True)

df=df.replace('\n','',regex=True)
df['Adv'] = pd.to_numeric(df['Adv'], errors='coerce')
df=df.fillna(0)
# print(df)
# print(df.dtypes)
result=0
c=0
# print(df['Adv'])
for i in range (len(df)):
    result=result+df['Adv'][i]
    if (df['Adv'][i]==0):
        i=i+1
        # print('1', result)
        df1=df1.append({'res':result},ignore_index=True)
        result=0
    if i==(len(df)-1):
        # result=result+df['Adv'][i]
        df1=df1.append({'res':result},ignore_index=True)
        # print('l', result)
    
# df1=df1.sort_values(by=['res'], ascending=False)
print(df1['res'].nlargest(3))
# print(df1)
df2['new']=(df1['res'].nlargest(3))
# print(df1.columns.values)
print(df2)
print(df2.sum())
count=0
new=0
# for j in range (len(df2)):
#     result=result+df2['new'][j]
#     print(result)
    # print(df2['new'][j])
    # if (count==2):
    #     print('1', result)
    #     break
        
        # df1=df1.append({'res':result},ignore_index=True)
    # count+=1



        



    

