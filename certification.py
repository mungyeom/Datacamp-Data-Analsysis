import pandas as pd
import numpy as np
import sys
from numpy import nan as NA
import matplotlib.pyplot as plt
import seaborn as sb
import copy




#call the data
data = pd.read_csv('/Desktop/Python workspace/Practice/travel_insurance.csv')
type(data)
print(data)
#check whether the data contain null
data.isnull()
#collect the rows and columns which have data
data.dropna()
#check the dulpiocated data and drop them
data.duplicated()
data.drop_duplicates()

#Devide customers and non-customers
Customers = data[data['TravelInsurance']==1]
print(Customers)
Non_Customers = data[data['TravelInsurance']==0]
print(Non_Customers.count())

#ages bins(Customers)
age_bins = [20,25,30,35,40,45,50,55,60,100]
cats = pd.cut(Customers['Age'],age_bins)
cats
pd.value_counts(cats)


#Employment Type(Customers)
c_non_g = Customers['Employment Type'] == 'Private Sector/Self Employed'
pd.value_counts(c_non_g)
570/(570+140)*100
#Graduation
c_graduate = Customers['GraduateOrNot'] == 'Yes'
pd.value_counts(c_graduate)
611/(611+99)*100
#AnnualIncome
c_income = round(Customers['AnnualIncome'].mean())
print(c_income)


#FamilyMembers
f_numbers_bins = [1,2,3,4,5,6,7,8]
c_f_numbers= pd.cut(Customers['FamilyMembers'],f_numbers_bins)
pd.value_counts(c_f_numbers)
sb.distplot(Customers['FamilyMembers'], bins=[1,2,3,4,5,6,7,8], color='green',rug =True)
plt.title('The number of Family members')
plt.show()
#ChronicDiseases
c_chronic = Customers['ChronicDiseases'] == 1
pd.value_counts(c_chronic)
205/(505+205)*100

#FrequentFlyer
c_fly = Customers['FrequentFlyer'] == 'Yes'
pd.value_counts(c_fly)

239/(471+239)*100

#EverTravelledAbroad
c_abroad = Customers['EverTravelledAbroad'] == 'Yes'
pd.value_counts(c_abroad)
298/(412+298)*100
################################################
#Number of Non-customers
Non_Customers = data[data['TravelInsurance']==0]
print(Non_Customers.count())
#ages bins(Non-Customers)
cats_non = pd.cut(Non_Customers['Age'],age_bins)
pd.value_counts(cats_non)


##Employment Type(Non-Customers)
non_g = Non_Customers['Employment Type'] == 'Private Sector/Self Employed'
pd.value_counts(non_g)

# age between 20 and 25 and the job is private sector
Etype_p20 = Non_Customers[(Non_Customers['Employment Type']=='Private Sector/Self Employed')&
        (Non_Customers['Age']<=25)&(Non_Customers['Age']>=20)]
print(Etype_p20)
Etype_p20.count()

# age between 30 and 35 and the job is private sector
Etype_p30 = Non_Customers[(Non_Customers['Employment Type']=='Private Sector/Self Employed')&
        (Non_Customers['Age']<=35)&(Non_Customers['Age']>=30)]
print(Etype_p30)
Etype_p30.count()

# age between 20 and 25 and the job is Government
Etype_g20 = Non_Customers[(Non_Customers['Employment Type']!='Private Sector/Self Employed')&
        (Non_Customers['Age']<=25)&(Non_Customers['Age']>=20)]
print(Etype_g20)
Etype_g20.count()

# age between 30 and 35 and the job is Government
Etype_g30 = Non_Customers[(Non_Customers['Employment Type']!='Private Sector/Self Employed')&
        (Non_Customers['Age']<=35)&(Non_Customers['Age']>=30)]
print(Etype_g30)
Etype_g30.count()

#Graduation(Non-Customers)
non_graduate = Non_Customers['GraduateOrNot'] == 'Yes'
pd.value_counts(non_graduate)

#Graduate & Private
N_gp = Non_Customers[(Non_Customers['GraduateOrNot']=='Yes')&
        (Non_Customers['Employment Type'] == 'Private Sector/Self Employed')]
print(N_gp)
N_gp.count()

#Graduate & Government
N_gg = Non_Customers[(Non_Customers['GraduateOrNot']=='Yes')&
        (Non_Customers['Employment Type'] != 'Private Sector/Self Employed')]
print(N_gg)
N_gg.count()

#Non-graduate & Private
NN_gp = Non_Customers[(Non_Customers['GraduateOrNot']!='Yes')&
        (Non_Customers['Employment Type'] == 'Private Sector/Self Employed') &
        Non_Customers['FrequentFlyer']=='Yes' & Non_Customers['EverTravelledAbroad']=='Yes']
print(NN_gp)
NN_gp.count()

#Non-graduate & Government
NN_gg = Non_Customers[(Non_Customers['GraduateOrNot']!='Yes')&
        (Non_Customers['Employment Type'] != 'Private Sector/Self Employed')]
print(NN_gg)
NN_gg.count()



#AnnualIncome
round(data['AnnualIncome'].mean())
non_income = data[(data['AnnualIncome'] > 932763) & (data['Employment Type']=='Private Sector/Self Employed')]
pd.value_counts(non_income)
print(non_income)

#FamilyMembers
f_numbers_bins = [1,2,3,4,5,6,7,8]
Non_f_numbers= pd.cut(Non_Customers['FamilyMembers'],f_numbers_bins)
pd.value_counts(Non_f_numbers)

#ChronicDiseases
Non_chronic = Non_Customers['ChronicDiseases'] == 1
pd.value_counts(Non_chronic)
347/(930+347)*100
#FrequentFlyer
Non_fly = Non_Customers['FrequentFlyer'] == 'Yes'
pd.value_counts(Non_fly)

178/(1099+178)*100

#EverTravelledAbroad
Non_abroad = Non_Customers['EverTravelledAbroad'] == 'Yes'
pd.value_counts(Non_abroad)
82/(1195+82)*100
    
### Travel habits difference
lt.rcParams["figure.figsize"] = (20,10)
plt.rcParams['axes.grid'] = True 


def bar_chart(feature):
    c = data[data['TravelInsurance']==1][feature].value_counts()
    nc = data[data['TravelInsurance']==0][feature].value_counts()
    df = pd.DataFrame([c,nc])
    df.index = ['Customers','Non-Customers']
    df.plot(kind='bar',stacked=True,rot=0)


# Show graphic
bar_chart('FrequentFlyer')
plt.title('The number of people who frequently take flights')
plt.show()

data.loc[(data['Age']>=20)&(data['Age']<25), 'Age'] = 1
data.loc[(data['Age']>=25)&(data['Age']<30), 'Age'] = 2
data.loc[(data['Age']>=30)&(data['Age']<35), 'Age'] = 3
data.loc[data['Age']>=35, 'Age']= 4

data.loc[(data['AnnualIncome']<932763), 'AnnualIncome'] = 0
data.loc[(data['AnnualIncome']>=932763), 'AnnualIncome'] = 1
bar_chart('AnnualIncome')
plt.title('The number of people whose income is over the average income')
plt.show()

bar_chart('Age')
plt.title('Age Group')
plt.legend(['25~29','30~34','35~'])
plt.show()


data.loc[(data['FamilyMembers']>=1)&(data['FamilyMembers']<3), 'FamilyMembers'] = 1
data.loc[(data['FamilyMembers']>=3)&(data['FamilyMembers']<5), 'FamilyMembers'] = 2
data.loc[(data['FamilyMembers']>=5), 'FamilyMembers'] = 3
bar_chart('FamilyMembers')
plt.title('Family members')
plt.legend(['~5','3~4','1~2'])
plt.show()

bar_chart('ChronicDiseases')
plt.title('Whether they have chronic diseases')
plt.show()

bar_chart('Employment Type')
plt.title('Employment Type')
plt.show()


bar_chart('GraduateOrNot')
plt.title('Whether they graduate or not')
plt.show()

bar_chart('EverTravelledAbroad')
plt.title("The number of people who have ever tripped to overseas countries")
plt.show()

#heatmap
heatmap_data = copy.copy(data)
print(heatmap_data)
heatmap_data['Employment Type'] = heatmap_data['Employment Type'].map({'Government Sector':0,'Private Sector/Self Employed':1})
heatmap_data['GraduateOrNot'] = heatmap_data['GraduateOrNot'].map({'Yes':1,'No':0})
heatmap_data['FrequentFlyer'] = heatmap_data['FrequentFlyer'].map({'Yes':1,'No':0})
heatmap_data['EverTravelledAbroad']=heatmap_data['EverTravelledAbroad'].map({'Yes':1,'No':0})
print(heatmap_data)
heatmap_data.corr(method='pearson')

plt.rcParams["figure.figsize"] = (9,9)
sb.heatmap(data.corr(),
           annot = True, 
           cmap = 'Greens', 
           vmin = -1, vmax=1)   
plt.show()     

round(data['AnnualIncome'].mean())

