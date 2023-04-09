# 가로 막대 그래프 
# %%
import numpy as np
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import seaborn as sns 

data = pd.read_excel("C:/Users/jhr03/OneDrive/바탕 화면/블랙보드 데이터 분석 공모전/3_블랙보드만족도조사_학생_데이터분석공모전.xlsx")
data = data.drop(['Timestamp','UniqID','소속','학년','성별'], axis=1)

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# %%
# 10번
q10 = data.iloc[:,9]
q10 = Counter(q10)
print(q10)

x = list(q10.keys())
y = list(q10.values())

plt.figure(dpi=200)
plt.barh(x, y, color='orange')
plt.title('10. 블랙보드 내에서 가장 선호하는 온라인수업(비대면) 운영 방식은 무엇입니까?', fontsize=10)
plt.show()

# %%
# 11번
q11 = data.iloc[:,10]
q11 = Counter(q11)
print(q11)

x = list(q11.keys())
y = list(q11.values())

plt.figure(dpi=200)
plt.barh(x, y, color='orange')
plt.title('11. 귀하가 생각하는 가장 효과적인 블랙보드 내 학습활동은 무엇입니까?', fontsize=10)
plt.show()

# %%
# 12번
q12 = data.iloc[:,11]
q12 = Counter(q12)
print(q12)

x = list(q12.keys())
y = list(q12.values())

plt.figure(dpi=200)
plt.barh(x, y, color='orange')
plt.title('12. 블랙보드 내 학습의 한계는 무엇이라고 생각하십니까?', fontsize=10)
plt.show()

# %%
# 13번
q13 = data.iloc[:,12]
q13 = Counter(q13)
print(q13)

x = list(q13.keys())
y = list(q13.values())

plt.figure(dpi=200)
plt.barh(x, y, color='orange')
plt.title('13. 블랙보드 내 수강 환경의 한계는 무엇이라고 생각하십니까?', fontsize=10)
plt.show()

# %%
# 15번
import seaborn as sns 

data_15 = data.iloc[:,14].apply(lambda x: x.split(';'))
q15 = list(itertools.chain(*data_15))
q15 = Counter(q15)
#q15 = sorted(q15.items(), key = lambda item: item[1], reverse = True)
print(q15)

x = list(q15.keys())
y = list(q15.values())

colors = sns.color_palette('hls',len(x)) 

plt.figure(dpi=200)
plt.title('15. 블랙보드 영상 출석콘텐츠 수업 방식의 한계는 무엇이라고 생각하십니까?', fontsize=10)
plt.barh(x, y, color=colors)
plt.show()

# %%
# 17번
data_17 = data.iloc[:,16].apply(lambda x: x.split(';'))
q17 = list(itertools.chain(*data_17))
q17 = Counter(q17)
#q15 = sorted(q15.items(), key = lambda item: item[1], reverse = True)
print(q17)

x = list(q17.keys())
y = list(q17.values())

colors = sns.color_palette('hls',len(x)) 

plt.figure(dpi=200)
plt.title('17. 실시간 화상강의(Zoom, Collaborate)를 활용한 온라인수업의 한계는 무엇이라고 생각하십니까?', fontsize=10)
plt.barh(x, y, color=colors)
plt.show()

# %%
# 18번 
q18 = data.iloc[:,17]
q18 = Counter(q18)
print(q18)

x = list(q18.keys())
y = list(q18.values())

plt.figure(dpi=200)
plt.barh(x, y, color='orange')
plt.title('18. 블랙보드 내에서 가장 선호하는 소통 방식을 선택하여 주십시오.', fontsize=10)
plt.show()


# %%
# 21번 문항
data_21 = data.iloc[:,20].apply(lambda x: x.split(';'))
q21 = list(itertools.chain(*data_21))
q21 = [i for i in q21 if i != '없음']
q21 = Counter(q21)
print(q21)

x = list(q21.keys())
y = list(q21.values())

plt.figure(dpi=200)
plt.title('블랙보드 오류사항', fontsize=15)
plt.barh(x, y, color='orange')
plt.show()

# %%
# 23번
q23 = data.iloc[:,22]
q23 = Counter(q23)
print(q23)

x = list(q23.keys())
y = list(q23.values())

plt.figure(dpi=200)
plt.title('모바일 앱 만족도', fontsize=15)
plt.bar(x, y, color='orange', width=0.6)
plt.xticks(fontsize=13)
plt.show()

# %%
# 46번 문항
q46 = data.iloc[:,45]
q46 = Counter(q46)
print(q46)

x = list(q46.keys())
y = list(q46.values())

plt.figure(dpi=200)
plt.barh(x, y, color='orange')
plt.title('46. 차세대 학습관리시스템(LMS)를 도입하는 것에 대해 어떻게 생각하십니까?', fontsize=10)
plt.show()