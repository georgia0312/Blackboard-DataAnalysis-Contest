import pandas as pd
from matplotlib import rc
import matplotlib.pyplot as plt

#한글 폰트 깨짐
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel("/Users/sehyunjun/Desktop/3_블랙보드만족도조사_학생_데이터분석공모전.xlsx")
data = pd.DataFrame(data)

#uiux관련 만족도 Q6-9
uiux = pd.DataFrame() 
for i in range(10,14):
    uiux[data.columns[i]]= pd.DataFrame(data.iloc[:,i].value_counts().sort_index())
print(uiux)

uiux.plot.bar(fontsize=7,color = ['red', 'orange', 'yellow', 'green'],alpha=0.5,width=0.5)
plt.legend(loc='upper left',fontsize=6)
plt.show()

#코스 관련 만족도 Q27,29
course = pd.DataFrame()
for i in [31,33]:
    course[data.columns[i]]= pd.DataFrame(data.iloc[:,i].value_counts().sort_index())
course.plot.bar(fontsize=7,color = ['red', 'orange'],alpha=0.5,width=0.5)
plt.legend(loc='upper left',fontsize=6)
plt.show()

#모바일 블랙보드 APP 만족도 Q23
app = pd.DataFrame(data.iloc[:,27].value_counts().sort_index())
app.plot.bar(fontsize=7,color = 'orange',alpha=0.5,width=0.5)
plt.legend(loc='upper left',fontsize=5)
plt.show()


#df3.apply(pd.value_counts).fillna(0.0) NaN채우기

