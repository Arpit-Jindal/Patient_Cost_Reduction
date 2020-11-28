import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
import matplotlib.pyplot as plt


monitor=pd.read_csv('out1.csv')
med_db=pd.read_csv('medications.csv')
care_plans=pd.read_csv('careplans.csv')
insurance_provider=pd.read_csv('payers.csv')
insurance_provider=insurance_provider["NAME"]
medicines=np.load('medicine_details.npy',allow_pickle='TRUE').item()
patients=np.load('patient_details.npy',allow_pickle='TRUE').item()
allergies=np.load('allergy_details.npy',allow_pickle='TRUE').item()
conditions=np.load('condition_details.npy',allow_pickle='TRUE').item()
payers=np.load('payer_ids.npy',allow_pickle='TRUE')
med_db=med_db[['MED_DESC','BASE_COST','MED_REASON']]
care_plans=care_plans[['DESCRIPTION','REASONDESCRIPTION']]
ids=monitor['PATIENT']
diet=pd.read_csv('diet.csv')
diets=diet["DIETS"]

#LinearRegression
age_coef=261.83801848327676
obesity_coef=4227.7376009403615 
smoking_coef=23851.06705386572  
medicine_coeff=700.13429
conditions_coeff=5021.21412412
avg_intercept=-4107.42213325581
#For logistic regression
const=-9.126396
bmi_coeff=0.05
sex_male=0.581482
age=0.065454
cigsPerDay=0.019702
totChol=0.002271
sysBP=0.017377
glucose=0.007588
past_disease=0.013
risk_coeff=0.0009
med_coeff=0.0005
cond_coeff=0.0008
amount_coeff=0.00000001

def smoke(X):
    for x in X['SMOKING']:
        status=0
        if(len(x)>2):
            if(x[2]=='N'):
                return 0
            else:
                return 1
def bmi(X):
    s=0
    count=0
    for bm in X['BMI']:
        if(len(bm)>2):
            count+=1
            bm=bm[2:len(bm)-2]
            bm=float(bm)
            s+=bm
            
    if(count!=0):
        return s/count
    else:
        return 22
def agecal(X):
    a=np.array(X['BIRTHDATE'])
    return a[0]
def sex(Y):
    a=np.array(Y['GENDER'])
    if(a[0]=='M'):
        return 1
    else:
        return 0
def heart_rate(X):
    s=0
    count=0
    for bm in X['HEART RATE']:
        if(len(bm)>2):
            count+=1
            bm=bm[2:len(bm)-2]
            bm=float(bm)
            s+=bm
            
    if(count!=0):
        return s/count
    else:
        return 72
def gluc(X):
    s=0
    count=0
    for bm in X['GLUSCOE']:
        if(len(bm)>2):
            count+=1
            bm=bm[2:len(bm)-2]
            bm=float(bm)
            s+=bm
            
    if(count!=0):
        return s/count
    else:
        return 90
def chol_st(X):
    s=0
    count=0
    for bm in X['CHOLESTROL']:
        if(len(bm)>2):
            count+=1
            bm=bm[2:len(bm)-2]
            bm=float(bm)
            s+=bm
            
    if(count!=0):
        return s/count
    else:
        return 170
def sys_st(X):
    s=0
    count=0
    for bm in X['SYSTOLIC']:
        if(len(bm)>2):
            count+=1
            bm=bm[2:len(bm)-2]
            bm=float(bm)
            s+=bm
            
    if(count!=0):
        return s/count
    else:
        return 85
def dias_st(X):
    s=0
    count=0
    for bm in X['DIASTOLIC']:
        if(len(bm)>2):
            count+=1
            bm=bm[2:len(bm)-2]
            bm=float(bm)
            s+=bm
            
    if(count!=0):
        return s/count
    else:
        return 130

def med_count(X):
    un=X['MED_DESC'].unique() 
    X=X[['MED_DESC','TOTALCOST']]
    cost=0
    for x in un:
        record=X[X['MED_DESC'] == x]
        if(len(record)==0):
            continue
        c=np.array(record['TOTALCOST'])
        cost+=c[0]
    if(cost==0 and len(un) is not 0):
        cost=145.23
    return [un,cost]
def condition_count(X):
    X=X['condition_description'].unique()
    return X
def get_medicines(conditions,medicines):
    l=(len(medicines))
    x=len(conditions)
    suggestions={}
    v=random.choice(payers)
    for condition in conditions:
        record=med_db[med_db['MED_REASON'] == condition].sort_values('BASE_COST')
        if(len(record)==0):
            continue
        suggestions[condition]=[]
        record=record['MED_DESC'].unique()
        for r in record:
            suggestions[condition].append(r)
    reduce=0
    random.seed(l+2)
    if(l is not 0):
        reduce= random.randrange(1,10)
        reduce=float(reduce)
        h=(random.randint(1,100))/100
        reduce+=h
    return [suggestions,reduce,v]
def careplan(conditions):
    suggestions=[]
    for condition in conditions:
        record=care_plans[care_plans['REASONDESCRIPTION'] == condition]
        if(len(record)==0):
            continue
        record=record['DESCRIPTION'].unique()
        for s in record:
            suggestions.append(s)
    return suggestions
def getname(X):
    first_name=np.array(X['FIRST'])
    first_name=first_name[0]
    first_name = ''.join(i for i in first_name if not i.isdigit())
    last_name=np.array(X['LAST'])
    last_name=last_name[0]
    last_name = ''.join(i for i in last_name if not i.isdigit())
    name=str(first_name)+" "+str(last_name)
    return name
def plot_hr(H):
    random.seed(1)
    X=np.random.normal(H, random.randint(1,5), size=200)
    Y=np.random.normal(72.0, 1, size=200)
    Z={"Patient":X,"Normal":Y}
    return Z
def plot_sys(H):
    random.seed(1)
    X=np.random.normal(H, random.randint(1,6), size=200)
    Y=np.random.normal(120, 1, size=200)
    Z={"Patient":X,"Normal":Y}
    return Z
def plot_dias(H):
    random.seed(1)
    X=np.random.normal(H, random.randint(1,6), size=200)
    Y=np.random.normal(80, 1, size=200)
    Z={"Patient":X,"Normal":Y}
    return Z
def plot_chol(H):
    random.seed(1)
    X=np.random.normal(H, random.randint(1,6), size=200)
    Y=np.random.normal(90, 1, size=200)
    Z={"Patient":X,"Normal":Y}
    return Z
def plot_bmi(H):
    random.seed(1)
    X=np.random.normal(H, random.randint(1,6), size=200)
    Y=np.random.normal(24, 1, size=200)
    Z={"Patient":X,"Normal":Y}
    return Z
def plot_gluc(H):
    random.seed(1)
    X=np.random.normal(H, random.randint(1,6), size=200)
    Y=np.random.normal(90, 1, size=200)
    Z={"Patient":X,"Normal":Y}
    return Z
def admission(risk,med_c,conditions,amount):
    ad=[] 
    random.seed(5)
    if(risk<85 and risk >10):
        adm1=risk+random.randint(1,10)+(random.randint(1,conditions)/100)
        adm2=risk-random.randint(1,10)+(random.randint(1,conditions)/100)
        ad.append(adm1)
        ad.append(adm2)
        return random.choice(ad)
    if(risk>85):
        adm1=risk+random.randint(1,5)+(random.randint(1,conditions)/100)
        adm2=risk-random.randint(1,5)+(random.randint(1,conditions)/100) 
        ad.append(adm1)
        ad.append(adm2)
        return random.choice(ad)
    if(risk>90):
        adm1=risk-random.randint(1,5)+(random.randint(1,conditions)/100)
        return adm1
    if(risk<10):
        adm1=risk+random.randint(1,4)+(random.randint(1,conditions)/100)
        return adm1
def rec_diet(cond,diet):
    z=len(cond)
    z+=random.randint(1,4)
    random.seed(2)
    random.shuffle(diet)
    return diet[:z]
def provider(l,prov):
    random.seed(l)
    random.shuffle(prov)
    return prov[:3]
        
def calculate_insurance(age,obesity,smoking,med,cond):
    y=(age_coef*age)+(obesity_coef*obesity)+(smoking_coef*smoking)+avg_intercept+medicine_coeff*med+conditions_coeff*cond
    return y

def calculate_risk(sex,age_val,cig,choles,sysB,gl,bmi,cond):
    s=const+sex_male*sex+age*age_val+cigsPerDay*cig+totChol*choles+sysBP*sysB+glucose*gl+bmi_coeff*bmi+past_disease*cond
    e=np.exp(s)
    return (e/(1+e))*100



def final_output(p_id):
    diet=np.array(diets)
    ins_prov=np.array(insurance_provider)
    ins_prov=ins_prov[:len(ins_prov)-2]
    X=monitor[monitor['PATIENT'] == p_id]
    Y=patients[p_id]
    a=agecal(Y)
    b=bmi(X)
    c=smoke(X)
    d=sex(Y)
    e=gluc(X)
    f=chol_st(X)
    g=int(sys_st(X))
    h=0
    [i,cost]=med_count(medicines[p_id])
    cost=round(cost,2)
    j=condition_count(conditions[p_id])
    l=int(dias_st(X))
    m=heart_rate(X)
    m=round(m,0)
    name=getname(Y)
    c_p=careplan(j)
    if(c is not 0):
        h=random.randint(1,20)
    insurance=calculate_insurance(a,b,c,len(i),len(j))
    insurance=round(insurance,3)
    r=calculate_risk(d,a,h,f,g,e,b,len(j))
    r=round(r,2)
    [suggestions,reduce,v]=get_medicines(j,i)
    out={}
    z="Female"
    if(d==1):
        z="Male"
    AL=[]
    for al in allergies[p_id]:
        if(al!='AL_DESCRIPTION'):
            AL.append(al)
    if(r<10):
        insurance=40000+(random.randint(1,100)/100)
    if(r>90):
        insurance+=250000
    insurance=round(insurance,2)
    reduce_cost=cost-(reduce*cost)/100
    reduce_cost=round(reduce_cost,2)
    diet_plan=rec_diet(j,diet)
    h_plot=plot_hr(m)
    s_plot=plot_sys(g)
    d_plot=plot_dias(l)
    g_plot=plot_gluc(e)
    c_plot=plot_chol(f)
    b_plot=plot_bmi(b)
    reduce = round(reduce,2)
    adm=admission(r,len(i),len(j),insurance)
    adm=round(adm,2)
    prov=provider(len(j),ins_prov)
    out["Name"]=name
    out["Sex"]=z
    out["Age"]=a
    out["Blood_Pressure"]=str(g)+'/'+str(l)
    out["Insurance"]=insurance
    out["Risk"]=r
    out["Heart_Rate"]=m
    out["Medicine_Cost"]=cost
    out["Current_Medications"]=i
    out["Current_Conditions"]=j
    out["Reduced_cost"]=reduce_cost
    out["Suggestions"]=suggestions
    out["Reduce_amount"]=reduce
    out["Vendor"]=v
    out["Allergies"]=AL
    out["Care_plan"]=c_p
    out["Heart_Plot"]=h_plot
    out["Systolic_Plot"]=s_plot
    out["Diastolic_Plot"]=d_plot
    out["Cholestrol_Plot"]=c_plot
    out["Glucose_Plot"]=g_plot
    out["BMI_Plot"]=b_plot
    out["Admission"]=adm
    out["Diet_Plan"]=diet_plan
    out["Health Insurance Providers"]=prov
    
    return out

# p_id='5b891358-1bb3-4bbf-b8a6-a73fbe58efe7'

# X=final_output(p_id)
