import pandas as pd
import numpy as np
import statsmodels.api as sm
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
import matplotlib.mlab as mlab
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


heart_df=pd.read_csv("observation1.csv")
heart_df.drop(['education'],axis=1,inplace=True)
heart_df.head()


# In[4]:


heart_df.rename(columns={'male':'Sex_male'},inplace=True)

        


# In[14]:


observation_file=pd.read_csv('csv/out1.csv')
observation_file.head()


# In[56]:


IDS=observation_file['PATIENT'].unique()
PATIENT_REPORTS={}
for id in IDS:
    patient_data=observation_file[observation_file['PATIENT'] == id]
    PATIENT_REPORTS[id]=patient_data


# In[ ]:


for id in IDS:
    data=(PATIENT_REPORTS[id])
    dates=data["DATE"].unique()
    for date in dates:
        D_day=data[data['DATE']==date]
        b_h=D_day[D_day['DESCRIPTION']=="Body Height"]
        b_h=b_h['VALUE']
        a=np.array(b_h)
        b_w=D_day[D_day['DESCRIPTION']=="Body Weight"]
        b_w=b_w['VALUE']
        b=np.array(b_w)
        bmi=D_day[D_day['DESCRIPTION']=="Body Mass Index"]
        bmi=bmi['VALUE']
        c=np.array(bmi)
        d_b_p=D_day[D_day['DESCRIPTION']=="Diastolic Blood Pressure"]
        d_b_p=d_b_p['VALUE']
        d=np.array(d_b_p)
        s_b_p=D_day[D_day['DESCRIPTION']=="Systolic Blood Pressure"]
        s_b_p=s_b_p['VALUE']
        e=np.array(s_b_p)
        h_r=D_day[D_day['DESCRIPTION']=="Heart rate"]
        h_r=h_r['VALUE']
        f=np.array(h_r)
        r=D_day[D_day['DESCRIPTION']=="Respiratory rate"]
        r=r['VALUE']
        r=round(r,2)
        g=np.array(r)
        gl=D_day[D_day['DESCRIPTION']=="Glucose"]
        gl=gl['VALUE']
        h=np.array(gl)
        u_n=D_day[D_day['DESCRIPTION']=="Urea Nitrogen"]
        u_n=u_n['VALUE']
        i=np.array(u_n)
        cr=D_day[D_day['DESCRIPTION']=="Creatinine"]
        cr=cr['VALUE']
        j=np.array(cr)
        smoke=D_day[D_day['DESCRIPTION']=="Tobacco smoking status NHIS"]
        smoke=smoke['VALUE']
        k=np.array(smoke)
        haemo=D_day[D_day['DESCRIPTION']=="Hemoglobin A1c/Hemoglobin.total in Blood"]
        haemo=haemo['VALUE']
        l=np.array(haemo)       
        chol=D_day[D_day['DESCRIPTION']=="Total Cholesterol"]
        chol=chol['VALUE']
        m=np.array(chol)   
        new_row={'PATIENT':id,'BODY HEIGHT':a,'BODY WEIGHT':b,'BMI':c,'DIASTOLIC':d,'SYSTOLIC':e,'HEART RATE':f,'RESPIRATORY':g,'GLUSCOE':h,'UREA':i,'CREATININE':j,'SMOKING':k,'HAEMOGLOBIN':l,'CHOLESTROL':m}
        new_frame =new_frame.append(new_row,ignore_index=True)


# ### <font color=CornflowerBlue>Missing values<font>

# In[15]:


heart_df.isnull().sum()


# In[16]:


count=0
for i in heart_df.isnull().sum(axis=1):
    if i>0:
        count=count+1
print('Total number of rows with missing values is ', count)
print('since it is only',round((count/len(heart_df.index))*100), 'percent of the entire dataset the rows with missing values are excluded.')


# In[17]:


heart_df.dropna(axis=0,inplace=True)


# ## <font color=RoyalBlue>Exploratory Analysis<font>

# In[18]:


def draw_histograms(dataframe, features, rows, cols):
    fig=plt.figure(figsize=(20,20))
    for i, feature in enumerate(features):
        ax=fig.add_subplot(rows,cols,i+1)
        dataframe[feature].hist(bins=20,ax=ax,facecolor='midnightblue')
        ax.set_title(feature+" Distribution",color='DarkRed')
        
    fig.tight_layout()  
    plt.show()
draw_histograms(heart_df,heart_df.columns,6,3)


# In[19]:


heart_df.TenYearCHD.value_counts()


# In[20]:


sn.countplot(x='TenYearCHD',data=heart_df)


# There are 3179 patents with no heart disease and 572 patients with risk of heart disease.

# In[21]:


sn.pairplot(data=heart_df)


# In[22]:


heart_df.describe()


# In[23]:


from statsmodels.tools import add_constant as add_constant
heart_df_constant = add_constant(heart_df)
heart_df_constant.head()


# In[24]:


st.chisqprob = lambda chisq, df: st.chi2.sf(chisq, df)
cols=heart_df_constant.columns[:-1]
model=sm.Logit(heart_df.TenYearCHD,heart_df_constant[cols])
result=model.fit()
result.summary()


# In[43]:


def back_feature_elem (data_frame,dep_var,col_list):
    """ Takes in the dataframe, the dependent variable and a list of column names, runs the regression repeatedly eleminating feature with the highest
    P-value above alpha one at a time and returns the regression summary with all p-values below alpha"""

    while len(col_list)>0 :
        model=sm.Logit(dep_var,data_frame[col_list])
        result=model.fit(disp=0)
        largest_pvalue=round(result.pvalues,3).nlargest(1)
        if largest_pvalue[0]<(0.05):
            return result
            break
        else:
            col_list=col_list.drop(largest_pvalue.index)

result=back_feature_elem(heart_df_constant,heart_df.TenYearCHD,cols)


# In[44]:


result.summary()


# ## <font color=RoyalBlue>Interpreting the results: Odds Ratio, Confidence Intervals and Pvalues<font>

# In[45]:


params = np.exp(result.params)
conf = np.exp(result.conf_int())
conf['OR'] = params
pvalue=round(result.pvalues,3)
conf['pvalue']=pvalue
conf.columns = ['CI 95%(2.5%)', 'CI 95%(97.5%)', 'Odds Ratio','pvalue']
print ((conf))


# ### <font color=CornflowerBlue>Splitting data to train and test split<font>

# In[46]:


import sklearn
new_features=heart_df[['age','Sex_male','cigsPerDay','totChol','sysBP','glucose','TenYearCHD']]
x=new_features.iloc[:,:-1]
y=new_features.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20,random_state=5)


# In[47]:


from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
y_pred=logreg.predict(x_test)


# ## <font color=RoyalBlue>Model Evaluation<font>
# 
# ### <font color=CornflowerBlue>Model accuracy<font>

# In[48]:


sklearn.metrics.accuracy_score(y_test,y_pred)


# ####  <font color=DarkBlue>Accuracy of the model is 0.88<font>

# ### <font color=CornflowerBlue>Confusion matrix<font>

# In[49]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
conf_matrix=pd.DataFrame(data=cm,columns=['Predicted:0','Predicted:1'],index=['Actual:0','Actual:1'])
plt.figure(figsize = (8,5))
sn.heatmap(conf_matrix, annot=True,fmt='d',cmap="YlGnBu")


# The confusion matrix shows 658+4 = 662 correct predictions and 88+1= 89 incorrect ones.
# 
# **<font color=DarkBlue>True Positives:**  4<font>
# 
# **<font color=DarkBlue>True Negatives:**  658<font>
# 
# **<font color=DarkBlue>False Positives:** 1 (*Type I error*)<font>
# 
# **<font color=DarkBlue>False Negatives:** 88 ( *Type II error*)<font>

# In[50]:


TN=cm[0,0]
TP=cm[1,1]
FN=cm[1,0]
FP=cm[0,1]
sensitivity=TP/float(TP+FN)
specificity=TN/float(TN+FP)


# ### <font color=CornflowerBlue>Model Evaluation - Statistics<font>

# In[51]:


print('The acuuracy of the model = TP+TN/(TP+TN+FP+FN) = ',(TP+TN)/float(TP+TN+FP+FN),'\n',

'The Missclassification = 1-Accuracy = ',1-((TP+TN)/float(TP+TN+FP+FN)),'\n',

'Sensitivity or True Positive Rate = TP/(TP+FN) = ',TP/float(TP+FN),'\n',

'Specificity or True Negative Rate = TN/(TN+FP) = ',TN/float(TN+FP),'\n',

'Positive Predictive value = TP/(TP+FP) = ',TP/float(TP+FP),'\n',

'Negative predictive Value = TN/(TN+FN) = ',TN/float(TN+FN),'\n',

'Positive Likelihood Ratio = Sensitivity/(1-Specificity) = ',sensitivity/(1-specificity),'\n',

'Negative likelihood Ratio = (1-Sensitivity)/Specificity = ',(1-sensitivity)/specificity)


# **From the above statistics it is clear that the model is highly specific than sensitive. The negative values are predicted more accurately than the positives.**

# In[52]:


y_pred_prob=logreg.predict_proba(x_test)[:,:]
y_pred_prob_df=pd.DataFrame(data=y_pred_prob, columns=['Safe','Risk'])
y_pred_prob_df.head()


# In[53]:


from sklearn.preprocessing import binarize
for i in range(1,5):
    cm2=0
    y_pred_prob_yes=logreg.predict_proba(x_test)
    y_pred2=binarize(y_pred_prob_yes,i/10)[:,1]
    cm2=confusion_matrix(y_test,y_pred2)
    print ('With',i/10,'threshold the Confusion Matrix is ','\n',cm2,'\n',
            'with',cm2[0,0]+cm2[1,1],'correct predictions and',cm2[1,0],'Type II errors( False Negatives)','\n\n',
          'Sensitivity: ',cm2[1,1]/(float(cm2[1,1]+cm2[1,0])),'Specificity: ',cm2[0,0]/(float(cm2[0,0]+cm2[0,1])),'\n\n\n')
    


# In[59]:


fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob_yes[:,1])
plt.plot(fpr,tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.title('Disease classifier')
plt.xlabel('False positive rate (1-Specificity)')
plt.ylabel('True positive rate (Sensitivity)')
plt.grid(True)


# In[ ]:




