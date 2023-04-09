import pandas as pd
from matplotlib import rc
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
#한글 폰트 깨짐
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv("/Users/sehyunjun/Desktop/blackboard/revised_dataset.csv")
data = pd.DataFrame(data)

#Q6-9만족도 레이더 차트
#해당 문항 데이터 추출
list1=[11,12,13,14]
data1=data.iloc[:,list1]
data1=np.exp(data1)     #지수 함수 적용
data1=data1.mean()      #평균값 추출
print(data1)

#항목 키워드
categories1=['메인화면 구성/디자인', '코스 메뉴', '정보 분류', '글자 크기']
categories1 = [*categories1,categories1[0]]
data1_values=data1.values
data1_values = [*data1_values, data1_values[0]]

#레이더 차트 그리기
label_loc1 = np.linspace(start=0, stop=2*np.pi, num=len(data1_values))
fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')
ax = fig.add_subplot(polar=True)
#plt.title('', size=20, color=  , x=-0.2, y=1,2, ha='left) 타이틀 지정
plt.xticks(label_loc1, labels=categories1, fontsize=12, color='black')
ax.set_rlabel_position(30)
plt.yticks([20,40,60,80,100], ['20','40','60','80','100'], color="grey", size=11)
plt.ylim(0,100)
ax.plot(label_loc1,data1_values,linestyle='solid',color='lightgreen')
ax.fill(label_loc1,data1_values,color='lightgreen',alpha=0.4)
plt.show()

#Q25,27,29만족도 레이더 차트

#해당 문항 데이터 추출
list1_1=[30,32,34]
data1_1=data.iloc[:,list1_1]
data1_1=np.exp(data1_1)     #지수 함수 적용
data1_1=data1_1.mean()      #평균값 추출
print(data1_1)

#항목 키워드
categories1_1=['코스 화면 구성', '코스 메뉴 구성', '코스 메뉴 공지사항']
categories1_1 = [*categories1_1,categories1_1[0]]
data1_1_values = data1_1.values
data1_1_values = [*data1_1_values, data1_1_values[0]]

#레이더 차트 그리기
label_loc1_1 = np.linspace(start=0, stop=2*np.pi, num=len(data1_1_values))
fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')
ax = fig.add_subplot(polar=True)
#plt.title('', size=20, color=  , x=-0.2, y=1,2, ha='left) 타이틀 지정
plt.xticks(label_loc1_1, labels=categories1_1, fontsize=12, color='black')
ax.set_rlabel_position(30)
plt.yticks([20,40,60,80,100], ['20','40','60','80','100'], color="grey", size=11)
plt.ylim(0,100)
ax.plot(label_loc1_1,data1_1_values,linestyle='solid',color='lightgreen')
ax.fill(label_loc1_1,data1_1_values,color='lightgreen',alpha=0.4)
plt.show()

#[4, 37, 33, 39, 43] 레이더 차트
list2=[9,42,38,44,48]
data2=data.iloc[:,list2]
data2=np.exp(data2)
data2=data2.mean()

categories2=['신속한 사이트 접속', '영상 출석 현황 기능', '과제 제출/피드백 기능', '시험/락다운 기능', '성적/기능']
categories2 = [*categories2,categories2[0]]
data2_values=data2.values
data2_values = [*data2_values, data2_values[0]]

label_loc2 = np.linspace(start=0, stop=2*np.pi, num=len(data2_values))
fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')
ax = fig.add_subplot(polar=True)
#plt.title('', size=20, color=  , x=-0.2, y=1,2, ha='left) 타이틀 지정
plt.xticks(label_loc2, labels=categories2, fontsize=12, color='black')
ax.set_rlabel_position(30)
plt.yticks([20,40,60,80,100], ['20','40','60','80','100'], color="grey", size=11)
plt.ylim(0,100)
ax.plot(label_loc2,data2_values,linestyle='solid',color='lightgreen')
ax.fill(label_loc2,data2_values,color='lightgreen',alpha=0.4)
plt.show()


#[37,14,16,35,33,39,43,,23] 만족도 레이더 차트 (8각형)
list3 = [42,19,21,40,38,44,48,28]
data3 = data.iloc[:,list3]
data3 = np.exp(data3)
data3 = data3.mean()
print(data3)

categories3=['출석 현황 기능', '영상 출석콘텐츠 수업 방식 ', '실시간 화상강의 수업 방식', '그룹활동 기능 ', '과제 제출 / 피드백 기능','시험/락다운 브라우저 기능', '성적 기능','모바일 앱']
categories3 = [*categories3,categories3[0]]
data3_values=data3.values
data3_values = [*data3_values, data3_values[0]]

label_loc3 = np.linspace(start=0, stop=2*np.pi, num=len(data3_values))
fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')
ax = fig.add_subplot(polar=True)
#plt.title('', size=20, color=  , x=-0.2, y=1,2, ha='left) 타이틀 지정
plt.xticks(label_loc3, labels=categories3, fontsize=11, color='black')
ax.set_rlabel_position(30)
plt.yticks([20,40,60,80,100], ['20','40','60','80','100'], color="grey", size=10)
plt.ylim(0,100)
ax.plot(label_loc3,data3_values,linestyle='solid',color='lightgreen')
ax.fill(label_loc3,data3_values,color='lightgreen',alpha=0.4)
plt.show()