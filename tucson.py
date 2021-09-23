import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

df = pd.read_csv('t911-50-city-scan-QueryResult.csv')

reasons = df.loc[:,"properties_howreceive"]

print(df)
reason_text =" ".join(reasons)
wordcloud = WordCloud(width=1000, height=1000, margin=0, background_color='white').generate(reason_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
# print(reasons)









