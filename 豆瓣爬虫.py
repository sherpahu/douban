import requests
from bs4 import BeautifulSoup
import re

request=requests.get('https://movie.douban.com/cinema/nowplaying/beijing/')
html_data=request
def get_HTML(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''
def parserHTML(html):
    soup=BeautifulSoup(html,'html.parser')
    comments_list=soup.find_all('div',class_='comment')
    eachComment=list()
    for com in comments_list:
        if com.find_all('p')[0].string is not None:
            eachComment.append(com.find_all('p')[0].string)
    return eachComment
def operate(list):
    comment=''
    for x in range(len(list)):
        comment+=(str(list[x])).strip()
        #去除首尾换行符
    pattern=re.compile(r'[\u4e00-\u9fa5]+')
    comments=re.sub(pattern,'',comment)
    return comments
def cnt(comments):
    import jieba
    import pandas as pd
    segment=jieba.lcut(comments)
    words_df=pd.DataFrame({'segment':segment})
    stopwords=pd.read_csv("chineseStopWords.txt",\
                          index_col=False,quoting=3,\
                          sep="\t",names=['stopword'], \
                          encoding='utf-8')#quoting=3全不引用
    words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
    import numpy    #numpy计算包
    words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
    words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)
    return words_df


def show(words_stat):
    import matplotlib.pyplot as plt
    #%matplotlib inline

    import matplotlib
    matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
    from wordcloud import WordCloud#词云包

    wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80) #指定字体类型、字体大小和字体颜色
    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}
    word_frequence_list = []
    for key in word_frequence:
        temp = (key,word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud=wordcloud.fit_words(word_frequence_list)
    plt.im
    show(wordcloud)
def main():
    url='https://movie.douban.com/subject/26861685/?from=playing_poster'
    html=get_HTML(url)
    li=parserHTML(html)
    com=operate(li)
    word=cnt(com)
    show(word)

main()
