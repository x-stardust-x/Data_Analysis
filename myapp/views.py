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
def plot(request):
    df = pd.read_csv('myapp\\TCT.csv', encoding='Big5')
    df = df.iloc[::-1]
    selected_region = request.GET.get('region')
    if selected_region == '全國各縣市':
        cities =TAIWAN
    elif selected_region == '北部':
        cities = ['台北市','新北市','桃園市','新竹縣','基隆市','宜蘭縣']
    elif selected_region == '中部':
        cities = ['台中市','彰化縣','南投縣','苗栗縣','雲林縣']
    elif selected_region == '南部':
        cities = ['嘉義縣','嘉義市','台南市','高雄市','屏東縣','澎湖縣']
    elif selected_region == '東部':
        cities = ['台東縣','花蓮縣']
    else:
        cities = ['全國']  # 默认情况

    fig = px.line(df, x='年度季別', y=cities, title='房價所得比趨勢圖')
    fig.update_layout(width=1600, height=800 ,yaxis_title='房價所得比')
    # 將圖表轉換為HTML
    plot_html = fig.to_html(full_html=False)

    # 傳遞數據到模板
    context = {
        'plot_html': plot_html,
        'selected_region': selected_region
    }

    return render(request, 'myapp/line.html', context)


def bar(request):
    df = pd.read_csv('myapp\\TCT.csv', encoding='Big5')
    df = df.iloc[::-1]
    selected_region = request.GET.get('region')
    if selected_region == '全國各縣市':
        cities =TAIWAN
    elif selected_region == '北部':
        cities = ['台北市','新北市','桃園市','新竹縣','基隆市','宜蘭縣']
    elif selected_region == '中部':
        cities = ['台中市','彰化縣','南投縣','苗栗縣','雲林縣']
    elif selected_region == '南部':
        cities = ['嘉義縣','嘉義市','台南市','高雄市','屏東縣','澎湖縣']
    elif selected_region == '東部':
        cities = ['台東縣','花蓮縣']
    else:
        cities = ['全國']  # 默认情况
    fig = px.bar(df,
                  x='年度季別',
                  y=cities,
                  color_discrete_sequence=px.colors.qualitative.Alphabet,
                  title='房價所得比長條圖')
    fig.update_layout(width=1600, height=800 ,yaxis_title='房價所得比',barmode='stack', xaxis_tickangle=45)
    plot_html = fig.to_html(full_html=False)
    context = {
        'plot_html': plot_html,
        'selected_region': selected_region
    }
    return render(request, 'myapp/bar.html', context)

def cbar(request):
    df = pd.read_csv('myapp\\TCT.csv', encoding='Big5')
    df = df.iloc[::-1]
    available_quarters = df['年度季別'].unique()
    available_quarters=available_quarters[::-1]
    selected_quarter = request.GET.get('quarter')
    filtered_df = df[df['年度季別'] == selected_quarter] if selected_quarter else df

    # 使用 Plotly Express 繪製長條圖
    fig = px.histogram(filtered_df,x='年度季別', y=['台北市','新北市','桃園市','新竹縣','基隆市','宜蘭縣'], title='地區分佈直方圖')
    fig.update_layout(width=1500, height=800 ,yaxis_title='全國房價所得比',barmode='group', xaxis_tickangle=45)
    # 將圖表轉換為HTML
    plot_html = fig.to_html(full_html=False)
    context = {
        'plot_html': plot_html,
        'quarters': available_quarters,
        'selected_quarter': selected_quarter
    }
    return render(request, 'myapp/compareb.html', context)



def home(request):
    return render(request, 'myapp/home.html')
