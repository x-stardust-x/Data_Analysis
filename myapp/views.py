from django.shortcuts import render
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

TAIWAN=['全國','新北市','台北市','桃園市','台中市',
        '台南市','高雄市','宜蘭縣','新竹縣','苗栗縣',
        '彰化縣','南投縣','雲林縣','嘉義縣','屏東縣',
        '台東縣','花蓮縣','澎湖縣','基隆市','新竹市','嘉義市']
def plot(request , parameter):
    df = pd.read_csv('myapp\\TCT.csv', encoding='Big5')
    df = df.iloc[::-1]
    
    if parameter == 'All':
        cities = TAIWAN
    elif parameter == 'North':
        cities = ['台北市','新北市','桃園市','新竹縣','基隆市','宜蘭縣']
    elif parameter == 'Center':
        cities = ['台中市','彰化縣','南投縣','苗栗縣','雲林縣']
    elif parameter == 'South':
        cities = ['嘉義縣','嘉義市','台南市','高雄市','屏東縣','澎湖縣']
    elif parameter == 'East':
        cities = ['台東縣','花蓮縣']
    elif parameter == 'Total':
        cities = ['全國']  # 默?情?

    fig = px.line(df,
                  x='年度季別',
                  y=cities,
                  color_discrete_sequence=px.colors.qualitative.Alphabet, 
                  title='房價所得比趨勢圖')
    fig.update_layout(width=1600, height=800 ,yaxis_title='全國房價所得比')
    plot_html = fig.to_html(full_html=False)
    return render(request, 'myapp/line.html', {'plot_html': plot_html})

def bar(request , parameter ):
    df = pd.read_csv('myapp\\TCT.csv', encoding='Big5')
    df = df.iloc[::-1]

    if parameter == 'All':
        cities = TAIWAN
    elif parameter == 'North':
        cities = ['台北市','新北市','桃園市','新竹縣','基隆市','宜蘭縣']
    elif parameter == 'Center':
        cities = ['台中市','彰化縣','南投縣','苗栗縣','雲林縣']
    elif parameter == 'South':
        cities = ['嘉義縣','嘉義市','台南市','高雄市','屏東縣','澎湖縣']
    elif parameter == 'East':
        cities = ['台東縣','花蓮縣']
    elif parameter == 'Total':
        cities = ['全國']  # 默?情?

    fig = px.bar(df,
                  x='年度季別',
                  y=cities,
                  color_discrete_sequence=px.colors.qualitative.Alphabet, 
                  title='房價所得比長條圖')
    fig.update_layout(width=1600, height=800 ,yaxis_title='全國房價所得比',barmode='stack', xaxis_tickangle=45)
    plot_html = fig.to_html(full_html=False)
    return render(request, 'myapp/bar.html', {'plot_html': plot_html})

def home(request):
    return render(request, 'myapp/home.html')
    