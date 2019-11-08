
#import gensim
import numpy
import random
from nltk.tokenize import RegexpTokenizer
#from gensim import corpora,models
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn import ensemble
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn import tree
import warnings
warnings.filterwarnings("ignore")

y_test2=[]
x_pos,x_neg,y_pos,y_neg=[],[],[],[]
tempa,tempb,x_train,x_test,y_train,y_test=[],[],[],[],[],[]
y2,y3=[],[]


def train_test_creation(fp,n,m,flag):
    temp1,temp2=[],[]
    data=fp.readlines()
    for i in data:
        if i!='\n':
            temp1.append(i)
            temp2.append(m)
            if flag=='neg':
                x_neg.append(i)
                y_neg.append(n)
            else:
                x_pos.append(i)
                y_pos.append(n)
            
    temp1a,temp1b,temp2a,temp2b=train_test_split(temp1,temp2,test_size=0.20,random_state=42)
    x_train.extend(temp1a)
    x_test.extend(temp1b)
    y_train.extend(temp2a)
    y_test.extend(temp2b)
    #print len(temp1b)
    for i in range(0,len(temp2b)):
        y_test2.append(n)
    
        
fp=open('Data/NewMurder_news.txt','r')
train_test_creation(fp,1,0,'neg')
fp.close()

fp=open('Data/NewCyberCrime.txt','r')
train_test_creation(fp,2,0,'neg')
fp.close()

fp=open('Data/NewDowryData.txt','r')
train_test_creation(fp,3,0,'neg')

fp=open('Data/NewTerroristData.txt','r')
train_test_creation(fp,4,0,'neg')
fp.close()


fp=open('Data/NewSmugglingNews.txt','r')
train_test_creation(fp,5,0,'neg')
fp.close()


fp=open('Data/NewNobelPrize.txt','r')
train_test_creation(fp,6,1,'pos')
fp.close()

fp=open('Data/NewAwardsNews.txt','r')
train_test_creation(fp,7,1,'pos')
fp.close()

fp=open('Data/NewMedical.txt','r')
train_test_creation(fp,8,1,'pos')
fp.close()

fp=open('Data/NewSocialService.txt','r')
train_test_creation(fp,9,1,'pos')
fp.close()

fp=open('Data/NewScienceNews.txt','r')
train_test_creation(fp,10,1,'pos')
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
print ("MODEL 1")
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
        
print ('accuracy ',(float(pos)/len(pred1))*100)

mett=metrics.classification_report(y_test,pred1)
print (mett)



'''MODEL 2'''
m2_x_test=[]
m2_y_test=[]
for i in range(0,y_test2.index(6)):
    if pred1[i]==0:
        m2_x_test.append(x_test[i])
        m2_y_test.append(y_test2[i])
        
        
x_neg.extend(m2_x_test)    
vec = CountVectorizer()
vec.fit_transform(x_neg)
x_matrix2= vec.transform(x_neg)            
    
x_train_matrix2=x_matrix2[0:len(x_neg)-len(m2_x_test),:]
x_test_matrix2=x_matrix2[len(x_neg)-len(m2_x_test):len(x_neg),:]   

print ("MODEL 2")
rd=ensemble.RandomForestClassifier()
rd.fit(x_train_matrix2,y_neg)
pred2=rd.predict(x_test_matrix2)

'''model=svm.SVC(C=1.0, kernel='rbf', degree=3, gamma=0.18, coef0=0.0, shrinking=True, probability=False,tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=900, random_state=None)
model.fit(x_train_matrix2, y_neg)
model.score(x_train_matrix2, y_neg)
pred2= model.predict(x_test_matrix2)'''
 



pos,neg=0,0

for i in range(0,len(pred2)):
    if pred2[i] == m2_y_test[i]:
        pos+=1
    else:
        neg+=1
        
print ('accuracy ',(float(pos)/len(pred2))*100)

mett=metrics.classification_report(m2_y_test,pred2)
print (mett)

'''MODEL 3'''
m3_x_test=[]
m3_y_test=[]

for i in range(y_test2.index(6),len(y_test2)):
    if pred1[i]==1:
        m3_x_test.append(x_test[i])
        m3_y_test.append(y_test2[i])
        
x_pos.extend(m3_x_test)    
vec = CountVectorizer()
vec.fit_transform(x_pos)
x_matrix3= vec.transform(x_pos)         
        
x_train_matrix3=x_matrix3[0:len(x_pos)-len(m3_x_test),:]
x_test_matrix3=x_matrix3[len(x_pos)-len(m3_x_test):len(x_pos),:]   
        
print ("MODEL 3")
'''tree_model = tree.DecisionTreeClassifier()
tree_model.fit(x_train_matrix3,y_pos)
pred3= tree_model.predict(x_test_matrix3)

rd=ensemble.RandomForestClassifier()
rd.fit(x_train_matrix3,y_pos)
pred3=rd.predict(x_test_matrix3)
model=svm.SVC(C=1.0, kernel='rbf', degree=3, gamma=0.18, coef0=0.0, shrinking=True, probability=False,tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=900, random_state=None)
model.fit(x_train_matrix3, y_pos)
model.score(x_train_matrix3, y_pos)
pred3= model.predict(x_test_matrix3)'''
knn = neighbors.KNeighborsClassifier()
knn.fit(x_train_matrix3,y_pos)
pred3 = knn.predict(x_test_matrix3)
        
pos,neg=0,0

for i in range(0,len(pred3)):
    if pred3[i] == m3_y_test[i]:
        pos+=1
    else:
        neg+=1
        
print ('accuracy ',(float(pos)/len(pred3))*100)

mett=metrics.classification_report(m3_y_test,pred3)
print (mett)
        
