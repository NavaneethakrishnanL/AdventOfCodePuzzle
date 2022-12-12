import math
import pandas as pd
file = open("advCodePuzzleDay2part2.txt")
df=pd.DataFrame(columns=['Opp','Me'])
df1=pd.DataFrame(columns=['res'])
df2=pd.DataFrame(columns=['new'])
for row in file:
    adv=row
    df=df.append({'Opp':adv, }, ignore_index=True)

df=df.replace('\n','',regex=True)
df[['Opp','Me']] = df["Opp"].str.split(" ", 1, expand=True)
df["Me"] = df["Me"].str.strip(" ")
a=0
for i in range (len(df)):
    u = (df['Opp'][i])
    m = (df['Me'][i])
    if u=="A" and m=='Y':
        a= a+1+3
    elif u=='B' and m=='Y':
        a=a+2+3
    elif u=='C' and m== 'Y':
        a=a+3+3
    elif u=="A" and m=='X':
        a=a+3
    elif u=='B' and m=='X':
        a=a+1
    elif u=='C' and m=='X':
        a=a+2
    elif u=='A' and m=='Z':
        a=a+2+6
    elif u=='B' and m=='Z':
        a=a+6+3
    elif u=='C' and m=='Z':
        a=a+1+6

print(a)