import math
import pandas as pd
file = open("advCodePuzzleDay2.txt")
df=pd.DataFrame(columns=['Opp','Me'])
df1=pd.DataFrame(columns=['res'])
df2=pd.DataFrame(columns=['new'])
for row in file:
    adv=row
    df=df.append({'Opp':adv, }, ignore_index=True)

df=df.replace('\n','',regex=True)
df[['Opp','Me']] = df["Opp"].str.split(" ", 1, expand=True)
df["Me"] = df["Me"].str.strip(" ")
# df['Adv'] = pd.to_numeric(df['Adv'], errors='coerce')
# print(df)
a=0
for i in range (len(df)):
    u = (df['Opp'][i])
    m = (df['Me'][i])
    if u=='A' and m =='X':
        a=1+3+a
    elif u=='B' and m=='Y':
        a=2+3+a
    elif u=='C' and m=='Z':
        a=3+3+a
    elif u=='A' and m=='Y':
        a=2+6+a
    elif u=='B' and m=='Z':
        a=3+6+a
    elif u=='C' and m=='X':
        a=1+6+a
    elif u=='A' and m=='Z':
        a=3+a
    elif u=='B' and m=='X':
        a=1+a
    elif u=='C' and m=='Y':
        a=2+a
print(a)