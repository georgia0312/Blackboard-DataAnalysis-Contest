# %% 
import pandas as pd

data = pd.read_excel("C:/Users/jhr03/OneDrive/바탕 화면/블랙보드 데이터 분석 공모전/3_블랙보드만족도조사_학생_데이터분석공모전.xlsx")
print(data.shape)
#data.info()

# %% 
data = data.drop(['Timestamp','UniqID','소속','학년','성별'], axis=1)

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# %% 
# 1번 문항
import matplotlib.pyplot as plt
from collections import Counter

q1 = data.iloc[:,0]
q1 = q1.tolist()
q1 = Counter(q1)
print(q1)

q1_data = sorted(list(q1.values()), reverse=True)
labels = ['만족', '매우 만족', '보통', '불만족', '매우 불만족']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 2}

plt.figure(dpi=200)
plt.pie(q1_data, startangle=250, autopct='%.1f%%', pctdistance=1.2, counterclock=False)
plt.title('블랙보드 시스템 만족도', fontsize=10)
plt.legend(labels, fontsize=8)
#plt.show()

# %%
# 21번 문항
import itertools
import numpy as np

data_21 = data.iloc[:,20].apply(lambda x: x.split(';'))
q21 = list(itertools.chain(*data_21))
q21 = Counter(q21)
print(q21)

x = list(q21.keys())
y = list(q21.values())

plt.figure(dpi=200)
plt.title('블랙보드 오류사항', fontsize=15)
plt.barh(x, y, color='orange')
plt.show()

# %%
# 45번 문항
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt

q45 = data['45. 학습관리시스템(LMS) 블랙보드와 관련하여 개선되었으면 하는 사항 및 기타 하고 싶으신 말씀에 대해 작성해주십시오.']
q45 = q45.dropna(axis=0)
q45 = q45.tolist()
q45 = [ i for i in q45 if i != '없음']

'''
# 개선사항 뽑아서 확인해보기
q45 = [ i for i in q45 if i != '없음']
for i in q45[2:10]:
    print(i)
'''

q45_str = ' '.join(s for s in q45)

okt = Okt()
nouns = okt.nouns(q45_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
words = [n for n in words if n!='개선' and n!='기능' and n!='블랙보드' and n!='사용'and n!='활동' and n!='경우']

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 46번 문항
data_46 = data.iloc[:,45].tolist()
q46 = Counter(data_46)
print(q46)

# %%
# 47번 문항
q47 = data['47. 차세대 학습관리시스템(LMS)을 도입을 희망하지 않는 이유에 대해 작성하여 주십시오.']
q47 = q47.dropna(axis=0)
print(q47)

# %%
# 48번 문항
q48 = data['48. 차세대 학습관리시스템(LMS)을 도입을 희망하는 이유에 대해 작성하여 주십시오.']
q48 = q48.dropna(axis=0)
print(q48)

# %%
# 49번 문항
q49 = data.iloc[:,48]
q49 = q49.dropna(axis=0)
q49

# %% 
# 50번 문항
q50 = data.iloc[:,49]
q50 = q50.dropna(axis=0)
q50


# %%
# 12&13번 문항
q12 = data.iloc[:,11].tolist()
q12 = Counter(q12)
print(q12)

q13 = data.iloc[:,12].tolist()
q13 = Counter(q13)
print(q13)

# %%
# 16번 문항
q16 = data.iloc[:,15].tolist()
q16 = Counter(q16)
print(q16)

# %%
# 17번 문항
data_17 = data.iloc[:,16].apply(lambda x: x.split(';'))
q17 = list(itertools.chain(*data_17))
q17 = Counter(q17)
print(q17)

# %%
# 18번 문항
q23 = data.iloc[:,17].tolist()
q23 = Counter(q23)
print(q23)

# %%
# 26번 문항
q45 = data['26. 코스 화면에서 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q45 = q45.dropna(axis=0)
q45 = q45.tolist()
q26_str = ' '.join(s for s in q45)

okt = Okt()
nouns = okt.nouns(q26_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
words = [n for n in words if n!='코스' and n!='화면']

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 7번 문항
q7 = data.iloc[:,6].tolist()

q7 = Counter(q7)
print(q7)


# %%
# 30번 문항
q45 = data['30. 코스 메뉴 공지사항 기능 중 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q45 = q45.dropna(axis=0)
q45 = q45.tolist()
q30_str = ' '.join(s for s in q45)

okt = Okt()
nouns = okt.nouns(q30_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['공지', '사항', '기능', '경우', '개선', '가장', '조금', '나중', '종종']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
q23 = data.iloc[:,21].tolist()
q23 = Counter(q23)
print(q23)

