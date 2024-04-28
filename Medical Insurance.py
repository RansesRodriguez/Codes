#Medical Insurance

import pandas as pd

df = pd.read_csv('Insurance.csv')

# People with and without children from the nort and south region:

no_children_in_southeast = df.loc[(df['children'] == 0) & (df['region'] == "southeast")]
#print(no_children_in_southeast.head(10))

no_children_in_northeast = df.loc[(df['children'] == 0) & (df['region'] == "northeast")]
#print(no_children_in_northeast.head(10))

have_children_in_southeast = df.loc[(df['children'] > 1) & (df['region'] == "southeast")]
#print(have_children_in_southeast.head(10))

have_children_in_northeast = df.loc[(df['children'] > 1) & (df['region'] == "northeast")]
#print(have_children_in_northeast.head(10))

# Average Insurance in the north and south region without children:

acncs = round(no_children_in_southeast['charges'].mean(), 2)
acncn = round(no_children_in_northeast['charges'].mean(), 2)

# Average Insurance in the north and south region with children: 

accs = round(have_children_in_southeast['charges'].mean(),2)
accn = round(have_children_in_northeast['charges'].mean(),2)

#print("This is the average charges for Medical Insurance in the southeast region without children: ${}".format(acncs))
#print("This is the average charges for Medical Insurance in the northeast region without children: ${}".format(acncn))
#print("This is the average charges for Medical Insurance in the southeast region with children: ${}".format(accs))
#print("This is the average charges for Medical Insurance in the northeast region with children: ${}".format(accn))

# Smokers over 40 yo from the southeast region:

smokers_over_40_south = df.loc[(df['age'] > 39) & (df['smoker'] == "yes") & (df['region'] == 'southeast')]
#print(smokers_over_40_south.head(10))

# Average Insurance charges for smokers over 40 yo in the southeast region:
average_charges_south = round(smokers_over_40_south['charges'].mean(), 2)
#print("This is the average Medical Insurance cost for smokers over 40 years old in the southeast region: ${}".format(average_charges_south))

# Smokers over 40 yo from the northeast region:

smokers_over_40_north = df.loc[(df['age'] > 39) & (df['smoker'] == "yes") & (df['region'] == "northeast")]
#print(smokers_over_40_north.head(10))

# Average Insurance charges for smokers over 40 yo in the northeast region:

average_charges_north = round(smokers_over_40_north['charges'].mean(),2)
#print("This is the average Medical Insurance charges for smokers over 40 years old in the northeast region: ${}".format(average_charges_north))

# With this analisys we can find that the southeast region has higher charges than the northeast region.