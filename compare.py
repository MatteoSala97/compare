import pandas as pd

rule_1 = pd.read_excel('regola-mio.xlsx')
rule_2 = pd.read_excel('regola-carlo.xlsx')

access_1 = pd.read_excel('access-mio.xlsx')
access_2 = pd.read_excel('access-carlo.xlsx')

#print(rule_1)
#print(rule_2)
#print(rule_1.equals(rule_2))                    #False
#print(access_1.equals(access_2))                #False

def compare_dataframes(df1, df2, name1, name2):
    if df1.equals(df2):
        print(f"I file '{name1}' e '{name2}' sono identici.")
    else:
        print(f"I file '{name1}' e '{name2}' sono diversi.")
        diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
        print("Differenze:")
        print(diff)
        return diff
        
output_df1 = compare_dataframes(rule_1, rule_2, 'regola-mio', 'regola-carlo')
output_df2 = compare_dataframes(access_1, access_2, 'access-mio', 'access-carlo')

output_df1.to_excel("output_rule.xlsx")
output_df2.to_excel("output_access.xlsx")