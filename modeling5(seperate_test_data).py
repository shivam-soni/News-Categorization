
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

y_test2=[]
x_pos,x_neg,y_pos,y_neg=[],[],[],[]
tempa,tempb,x_train,x_test,y_train,y_test=[],[],[],[],[],[]
y2,y3=[],[]


def train_test_creation(fp,n):
    temp1,temp2=[],[]
    data=fp.readlines()
    for i in data:
        if i!='\n':
            temp1.append(i)
            temp2.append(n)
          
            
    temp1a,temp1b,temp2a,temp2b=train_test_split(temp1,temp2,test_size=0.20,random_state=42)
    x_train.extend(temp1a)
    x_test.extend(temp1b)
    y_train.extend(temp2a)
    y_test.extend(temp2b)
   
    
        
fp=open('NewMurder_news.txt','r')
train_test_creation(fp,1)
fp.close()

fp=open('NewCyberCrime.txt','r')
train_test_creation(fp,2)
fp.close()

fp=open('NewDowryData.txt','r')
train_test_creation(fp,3)

fp=open('NewAcidData.txt','r')
train_test_creation(fp,4)
fp.close()

fp=open('NewNobelPrize.txt','r')
train_test_creation(fp,5)
fp.close()

fp=open('NewEducationNews.txt','r')
train_test_creation(fp,6)
fp.close()

fp=open('NewMedicalNews.txt','r')
train_test_creation(fp,7)
fp.close()

fp=open('NewSocialService.txt','r')
train_test_creation(fp,8)
fp.close()

combo=[]
for i in range(0,len(x_train)):
    combo.append([x_train[i],y_train[i]]) 
    
 
random.shuffle(combo)
x_train,y_train=[],[]

for i in combo:
    x_train.append(i[0])
    y_train.append(i[1])

x_train.extend(x_test)   #we lost the original x_train here
vec = CountVectorizer()
vec.fit_transform(x_train)
x_matrix = vec.transform(x_train)

x_train_matrix=x_matrix[0:len(x_train)-len(x_test),:]
x_test_matrix=x_matrix[len(x_train)-len(x_test):len(x_train),:]

#x_train,x_test,y_train,y_test=train_test_split(x_train_matrix,y1,test_size=0.12,random_state=42)

#y_train=numpy.array(y_train)

rd=ensemble.RandomForestClassifier()
rd.fit(x_train_matrix,y_train)
pred1=rd.predict(x_test_matrix)

'''model=svm.SVC(C=1.0, kernel='rbf', degree=3, gamma=0.18, coef0=0.0, shrinking=True, probability=False,tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=900, random_state=None)
model.fit(x_train_matrix, y_train)
model.score(x_train_matrix, y_train)
pred1= model.predict(x_test_matrix)'''
 
    
    


pos,neg=0,0

for i in range(0,len(pred1)):
    if pred1[i] == y_test[i]:
        pos+=1
    else:
        neg+=1
        
print 'accuracy ',(float(pos)/len(pred1))*100

mett=metrics.classification_report(y_test,pred1)
print mett




