import gensim
import numpy
import random
from nltk.tokenize import RegexpTokenizer
from gensim import corpora,models
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn import ensemble
from sklearn import metrics
from sklearn.cross_validation import train_test_split

tokenizer = RegexpTokenizer(r'\w+')

x,x_pos=[],[]
y=[]
y2=[]
fp=open('NewMurder_news.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(0)

fp=open('NewCyberCrime.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(0)
        
fp=open('NewDowryData.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(0)

fp=open('NewTerroristData.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(0)

fp=open('NewSmugglingNews.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(0)
        
fp=open('NewNobelPrize.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(1)
        y2.append(6)
        x_pos.append(i)

fp=open('NewAwardsNews.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(1)
        y2.append(7)
        x_pos.append(i)

fp=open('NewMedicalNews.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(1)
        y2.append(8)  
        x_pos.append(i)
'''fp=open('NewSocialService.txt','r')
data=fp.readlines()

for i in data:
    if i!='\n':
        x.append(i)
        y.append(1)'''

fp=open('NewSocialService.txt','r')
test_data=fp.readlines()

for i in test_data:
    if i!='\n':
        x.append(i)
        y.append(1)
        y2.append(9)
        x_pos.append(i)

fp=open('NewScienceNews.txt','r')
test_data=fp.readlines()

temp1,temp2,temp3=[],[],[]
for i in test_data:
    if i!='\n':
        temp1.append(i)
        temp2.append(1)
        temp3.append(10)
temp_x,x_test,temp_y,y_test,temp_y2,y_test_m2=train_test_split(temp1,temp2,temp3,test_size=0.20,random_state=42)     
x.extend(temp_x)
y.extend(temp_y)
combo=[]
for i in range(0,len(x)):
    combo.append([x[i],y[i]]) 
 
random.shuffle(combo)

x1,y1=[],[]
for i in combo:
    x1.append(i[0])
    y1.append(i[1])
    
x1.extend(x_test)
    
vec = CountVectorizer()
vec.fit_transform(x1)
x_matrix = vec.transform(x1)

x_train_matrix=x_matrix[0:len(x1)-len(x_test),:]
x_test_matrix=x_matrix[len(x1)-len(x_test):len(x1),:]

rd=ensemble.RandomForestClassifier()
rd.fit(x_train_matrix,y1)
pred1=rd.predict(x_test_matrix)

'''model=svm.SVC(C=1.0, kernel='rbf', degree=3, gamma=0.18, coef0=0.0, shrinking=True, probability=False,tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=900, random_state=None)
model.fit(x_train, y1)
model.score(x_train, y1)
pred1= model.predict(x_test)'''
 
pos,neg=0,0

for i in range(0,len(pred1)):
    if pred1[i] == y_test[i]:
        pos+=1
    else:
        neg+=1
        
print 'accuracy ',(float(pos)/len(pred1))*100
y_test=numpy.array(y_test)
mett=metrics.classification_report(y_test,pred1)
print mett


#MODEL 2

m2_x_test,m2_y_test=[],[]
if (pos>neg):
    for i in pred1:
        if i==1:
            m2_x_test.append(x_test[i])
            m2_y_test.append(y_test_m2[i])

    x_pos.extend(temp_x)
    y2.extend(temp_y2)
    combo=[]
    for i in range(0,len(x_pos)):
        combo.append([x_pos[i],y2[i]]) 
     
    random.shuffle(combo)
    
    x2,y2_m2=[],[]
    for i in combo:
        x2.append(i[0])
        y2_m2.append(i[1])
        
    x2.extend(m2_x_test)
    
    vec = CountVectorizer()
    vec.fit_transform(x2)
    x_matrix2 = vec.transform(x2)
    
    x_train_matrix2=x_matrix2[0:len(x2)-len(m2_x_test),:]
    x_test_matrix2=x_matrix2[len(x2)-len(m2_x_test):len(x2),:]
    
    rd=ensemble.RandomForestClassifier()
    rd.fit(x_train_matrix2,y2_m2)
    pred2=rd.predict(x_test_matrix2)
    
    pos,neg=0,0
    for i in range(0,len(pred2)):
        if pred2[i] == m2_y_test[i]:
            pos+=1
        else:
            neg+=1
    print "MODEL 2"        
    print 'accuracy ',(float(pos)/len(pred2))*100
    
    m2_y_test=numpy.array(m2_y_test)
    mett=metrics.classification_report(m2_y_test,pred2)
    print mett

    
    




    