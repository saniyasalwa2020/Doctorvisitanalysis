import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv(r'/content/DoctorVisits - DA.csv')
print(df.head(15))

df = pd.read_csv(r'/content/DoctorVisits - DA.csv')
df.head(10)

"""**1.Display complete information about the columns of the dataset such as Column name,Count,Data type and overall memory usage**"""

df.info()

"""**2.Find out the total no.of people based on their count of illeness**"""

df["illness"].value_counts()

df["gender"].value_counts()

"""**3.Visualize and analyse the maximum,minimum and medium income**"""

y=list(df.income)
plt.boxplot(y)
plt.show

"""**4.Find out the no of days of reduced activity of male and female seperatly due to illeness**"""

df.groupby(['gender','reduced']).mean()

"""**5.Visualize is there any missing values in the dataset based on a heat map**"""

#missing values
sns.heatmap(df.isnull(),cbar=False,cmap='viridis')

"""**6.Find out the correlation between variables in the given dataset correlation between different variables**"""

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')

"""**7.Analyse how the income of a patient affects the no of visits to the hospital**"""

#relation between income and visits
plt.figure(figsize=(10,10))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('income')
plt.ylabel('visits')

"""**8.Count and visualize the number of males and females ffected by illness**"""

sns.histplot(df.gender,bins=2)

"""**9.Visualize the percentage of people getting govt health insurance due to low income,due to old age and also the percentage of people having private health insurance**"""

# % of people getting govt Insurance due to low income

label=['yes','no']
Y=df[df['freepoor']=='yes']
N = df[df['freepoor']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x, labels=label)
plt.title("% of people getting govt health Insurance due to low income")
plt.show()

# % of people having private Insurance

Y = df[df['private']=='yes']

N=df[df["private"]=='no']
x= [Y.shape[0] , N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("s of people having private health Insurance")
plt.show()

# % of people getting govt Insurance due to old age,disability or vetreran status
Y=df[df["freerepat"]=='yes']
N = df[df["freerepat" ]=='no' ]
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x, labels=label)
plt.title("% of people getting govt health Insuranc due to  old age,disability or vetreran status")
plt.show()

"""**10.Plot a horizontal bar chart to analyze the reduced days of activity due to illenes based on gender**"""

db= df.groupby('gender')['reduced' ].sum().to_frame().reset_index()
#Creating the bar chart
plt.barh(db['gender'], db['reduced'], color = ['cornflowerblue', 'lightseagreen'])
#Adding the aesthetics
plt.title('Bar Chart')
plt.xlabel('gender')
plt.ylabel('reduced activity')
#Show the plot
plt.show()

