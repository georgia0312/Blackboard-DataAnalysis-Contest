# 워드 클라우드
# %%
import matplotlib.pyplot as plt
from konlpy.tag import Okt
import pandas as pd
from collections import Counter
from wordcloud import WordCloud

data = pd.read_excel("C:/Users/jhr03/OneDrive/바탕 화면/블랙보드 데이터 분석 공모전/3_블랙보드만족도조사_학생_데이터분석공모전.xlsx")
data = data.drop(['Timestamp','UniqID','소속','학년','성별'], axis=1)

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# %%
# 24번 문항 
q24 = data['24. 모바일 APP 이용 시 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q24 = q24.dropna(axis=0)
q24 = q24.tolist()
q24_str = ' '.join(map(str, q24))

okt = Okt()
nouns = okt.nouns(q24_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['모바일','기능', '경우', '개선', '사용', '자꾸']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 26번 문항
q26 = data['26. 코스 화면에서 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q26 = q26.dropna(axis=0)
q26 = q26.tolist()
q26_str = ' '.join(s for s in q26)

okt = Okt()
nouns = okt.nouns(q26_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
words = [n for n in words if n!='코스' and n!='화면' and n!='별로']

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)

# %%
# 28번 문항
q28 = data['28. 코스 메뉴 구성에서 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q28 = q28.dropna(axis=0)
q28 = q28.tolist()
q28_str = ' '.join(s for s in q28)

okt = Okt()
nouns = okt.nouns(q28_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['코스', '메뉴', '기능', '경우', '개선', '구성', '필요','사용']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 30번 문항
q30 = data['30. 코스 메뉴 공지사항 기능 중 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q30 = q30.dropna(axis=0)
q30 = q30.tolist()
q30_str = ' '.join(s for s in q30)

okt = Okt()
nouns = okt.nouns(q30_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['공지', '사항', '기능', '경우', '개선', '가장', '조금', '나중', '종종','사용','매우']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 32번
q32 = data['32. 영상 출결 콘텐츠(커먼즈, 유튜브, 구글 드라이브) 기능 중 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q32 = q32.dropna(axis=0)
q32 = q32.tolist()
q32 = [ i for i in q32 if i != '없음']

q32_str = ' '.join(s for s in q32)

okt = Okt()
nouns = okt.nouns(q32_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['개선','기능','가끔','출결','영상','경우','사용','제대로','바로']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 34번
q34 = data['34. 과제 제출 및 피드백 기능에서 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q34 = q34.dropna(axis=0)
q34 = q34.tolist()
q34 = [ i for i in q34 if i != '없음']

q34_str = ' '.join(s for s in q34)

okt = Okt()
nouns = okt.nouns(q34_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['기능', '경우', '개선', '과제', '제출', '사용', '대한','피드백']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 36번
q36 = data['36. 그룹활동(토론, 블로그, 저널) 기능에서 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q36 = q36.dropna(axis=0)
q36 = q36.tolist()
q36 = [ i for i in q36 if i != '없음']

q36_str = ' '.join(s for s in q36)

okt = Okt()
nouns = okt.nouns(q36_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['기능', '경우', '개선', '과제','사용', '이용', '거의','대한','활용']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 38번
q38 = data['38. 녹화영상 출석 현황에서 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q38 = q38.dropna(axis=0)
q38 = q38.tolist()
q38 = [i for i in q38 if i != '없음']

q38_str = ' '.join(s for s in q38)

okt = Okt()
nouns = okt.nouns(q38_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['기능', '경우', '개선', '종종','사용', '이용', '출석', '영상']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 40번 
q40 = data['40. 시험/락다운브라우저 기능 중 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q40 = q40.dropna(axis=0)
q40 = q40.tolist()
q40 = [i for i in q40 if i != '없음']

q40_str = ' '.join(s for s in q40)

okt = Okt()
nouns = okt.nouns(q40_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['기능', '경우', '개선', '종종','사용', '이용', '출석', '영상','락다운','브라우저','시험']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()
# %%
# 42번
q42 = data['42. 실시간 강의 도구(ZOOM, Collaborate) 기능에서 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q42 = q42.dropna(axis=0)
q42 = q42.tolist()
q42 = [i for i in q42 if i != '없음']

q42_str = ' '.join(s for s in q42)

okt = Okt()
nouns = okt.nouns(q42_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['기능', '경우', '개선', '종종','사용', '이용', '출석', '영상','콜라보']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 44번
q44 = data['44. 성적 기능에서 개선되었으면 하는 점을 자유롭게 작성하여 주십시오.']
q44 = q44.dropna(axis=0)
q44 = q44.tolist()
q44 = [i for i in q44 if i != '없음']

q44_str = ' '.join(s for s in q44)

okt = Okt()
nouns = okt.nouns(q44_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['기능', '경우', '개선', '성적', '강의']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()

# %%
# 45번
q45 = data['45. 학습관리시스템(LMS) 블랙보드와 관련하여 개선되었으면 하는 사항 및 기타 하고 싶으신 말씀에 대해 작성해주십시오.']
q45 = q45.dropna(axis=0)
q45 = q45.tolist()
q45 = [i for i in q45 if i != '없음']

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
# 47번 문항 
q48 = data['47. 차세대 학습관리시스템(LMS)을 도입을 희망하지 않는 이유에 대해 작성하여 주십시오.']
q48 = q48.dropna(axis=0)
q48 = q48.tolist()
q48_str = ' '.join(s for s in q48)

okt = Okt()
nouns = okt.nouns(q48_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['시스템', '기능', '경우', '개선', '사용','때문','블랙보드']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()
# %%
# 48번 문항 
q48 = data['48. 차세대 학습관리시스템(LMS)을 도입을 희망하는 이유에 대해 작성하여 주십시오.']
q48 = q48.dropna(axis=0)
q48 = q48.tolist()
q48_str = ' '.join(s for s in q48)

okt = Okt()
nouns = okt.nouns(q48_str) # 명사만 추출

words = [n for n in nouns if len(n) > 1]
no_words = ['시스템', '기능', '경우', '개선', '생각','블랙보드','입장','때문']
words = [n for n in words if n not in no_words]

c = Counter(words)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, scale=2.0, max_font_size=200, background_color='white')
gen = wc.generate_from_frequencies(c)
plt.figure(figsize=(10, 8), dpi=200)
plt.axis('off')
plt.imshow(gen)
plt.show()
# %%
