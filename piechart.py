import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rc


#한글 폰트 깨짐
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel("블랙보드만족도조사_학생_데이터분석공모전.xlsx")
data = pd.DataFrame(data)

#Q1
q1 = pd.DataFrame(data.iloc[:,5].value_counts().sort_index())
print(q1)

#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [4, 16, 21, 143, 36] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )
plt.legend(pie[0],labels) ## 범례
plt.title('1. 블랙보드 시스템에 전반적으로 만족하십니까?')
plt.show()

#Q14
q14 = pd.DataFrame(data.iloc[:,18].value_counts().sort_index())
print(q14)
#데이터 준비
labels = ['만족','매우 만족','매우 불만족','보통','불만족','영상 출석콘텐츠 수업 경험 없음']##라벨
frequency = [102, 37, 10, 44, 12, 15] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )
 
plt.legend(pie[0],labels) ## 범례
plt.title('14. 블랙보드 영상 출석콘텐츠 수업 방식에 대해 전반적으로 만족합니까?')
plt.show()


#q16
#q16
q16 = pd.DataFrame(data.iloc[:,20].value_counts().sort_index())
print(q16)

#데이터 준비
labels = ['만족','매우 만족','매우 불만족','보통','불만족','영상 출석콘텐츠 수업 경험 없음']##라벨
frequency = [126, 38, 3, 42, 8, 3] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )

 
plt.legend(pie[0],labels) ## 범례
plt.title('16. 실시간 화상강의(Zoom, Collaborate) 수업 방식에 대해 전반적으로 만족합니까?')
plt.show()

#Q19
q19 = pd.DataFrame(data.iloc[:,23].value_counts().sort_index())
print(q19)
#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [6, 16, 28, 133, 37] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )
 
plt.legend(pie[0],labels) ## 범례
plt.title('19. 블랙보드 기능에 전반적으로 만족하십니까?')
plt.show()

#q20
q20 = pd.DataFrame(data.iloc[:,24].value_counts().sort_index())
print(q20)

#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [4, 13, 27, 115, 610] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       )

#퍼센트가 겹쳐서 계단식으로 
total = np.sum(frequency) ## 빈도수 합
 
threshold = 5
sum_pct = 0 ## 퍼센티지
count_less_5pct = 0 ## 5%보다 작은 라벨의 개수
spacing = 0.1
for i,l in enumerate(labels):
    ang1, ang2 = ax.patches[i].theta1, ax.patches[i].theta2 ## 파이의 시작 각도와 끝 각도
    center, r = ax.patches[i].center, ax.patches[i].r ## 파이의 중심 좌표
    
    ## 비율 상한선보다 작은 것들은 계단형태로 만든다.
    if frequency[i]/total*100 < threshold:
        x = (r/2+spacing*count_less_5pct)*np.cos(np.pi/180*((ang1+ang2)/2)) + center[0] ## 텍스트 x좌표
        y = (r/2+spacing*count_less_5pct)*np.sin(np.pi/180*((ang1+ang2)/2)) + center[1] ## 텍스트 y좌표
        count_less_5pct += 1
    else:
        x = (r/2)*np.cos(np.pi/180*((ang1+ang2)/2)) + center[0] ## 텍스트 x좌표
        y = (r/2)*np.sin(np.pi/180*((ang1+ang2)/2)) + center[1] ## 텍스트 y좌표
    
    ## 퍼센티지 출력
    if i < len(labels) - 1:
        sum_pct += float(f'{frequency[i]/total*100:.2f}')
        ax.text(x,y,f'{frequency[i]/total*100:.2f}%',ha='center',va='center',fontsize=12)
    else: ## 마지막 파이 조각은 퍼센티지의 합이 100이 되도록 비율을 조절
        ax.text(x,y,f'{100-sum_pct:.2f}%',ha='center',va='center',fontsize=12)

 
plt.legend(pie[0],labels) ## 범례
plt.title('20. 블랙보드 기능은 전반적으로 사용하기 쉽습니까?')
plt.show()


#Q22
q22 = pd.DataFrame(data.iloc[:,26].value_counts().sort_index())
print(q22)
#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [5, 18, 50, 114, 33] ##빈도

fig = plt.figure(figsize=(12,12))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )
 
plt.legend(pie[0],labels) ## 범례
plt.title('22. 블랙보드 홈페이지는 LMS를 사용하는데 필요한 정보를 손쉽게 찾고 관련 안내를 신속하게 전달할 수 있도록 구성되었습니다. 이 구성에 만족하십니까? ')
plt.show()

#Q31
q31 = pd.DataFrame(data.iloc[:,35].value_counts().sort_index())
print(q31)
#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [7, 10, 52, 109, 42] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )

plt.legend(pie[0],labels) ## 범례
plt.title('31. 영상 출결 콘텐츠(커먼즈, 유튜브, 구글 드라이브) 기능에 만족하십니까?')
plt.show()

#Q35

q35 = pd.DataFrame(data.iloc[:,39].value_counts().sort_index())
print(q35)
#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [12, 18, 69, 90, 31] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )
 
plt.legend(pie[0],labels) ## 범례
plt.title('35. 그룹활동(토론, 블로그, 저널) 기능에 만족하십니까?')
plt.show()


#Q41
q41 = pd.DataFrame(data.iloc[:,45].value_counts().sort_index())
print(q41)

#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [1, 6, 23, 123, 67] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       )

#퍼센트가 겹쳐서 계단식으로 
total = np.sum(frequency) ## 빈도수 합
 
threshold = 5
sum_pct = 0 ## 퍼센티지
count_less_5pct = 0 ## 5%보다 작은 라벨의 개수
spacing = 0.1
for i,l in enumerate(labels):
    ang1, ang2 = ax.patches[i].theta1, ax.patches[i].theta2 ## 파이의 시작 각도와 끝 각도
    center, r = ax.patches[i].center, ax.patches[i].r ## 파이의 중심 좌표
    
    ## 비율 상한선보다 작은 것들은 계단형태로 만든다.
    if frequency[i]/total*100 < threshold:
        x = (r/2+spacing*count_less_5pct)*np.cos(np.pi/180*((ang1+ang2)/2)) + center[0] ## 텍스트 x좌표
        y = (r/2+spacing*count_less_5pct)*np.sin(np.pi/180*((ang1+ang2)/2)) + center[1] ## 텍스트 y좌표
        count_less_5pct += 1
    else:
        x = (r/2)*np.cos(np.pi/180*((ang1+ang2)/2)) + center[0] ## 텍스트 x좌표
        y = (r/2)*np.sin(np.pi/180*((ang1+ang2)/2)) + center[1] ## 텍스트 y좌표
    
    ## 퍼센티지 출력
    if i < len(labels) - 1:
        sum_pct += float(f'{frequency[i]/total*100:.2f}')
        ax.text(x,y,f'{frequency[i]/total*100:.2f}%',ha='center',va='center',fontsize=12)
    else: ## 마지막 파이 조각은 퍼센티지의 합이 100이 되도록 비율을 조절
        ax.text(x,y,f'{100-sum_pct:.2f}%',ha='center',va='center',fontsize=12)
 
plt.legend(pie[0],labels) ## 범례
plt.title('41. 실시간 강의 도구(ZOOM, Collaborate) 기능에 만족하십니까?')
plt.show()