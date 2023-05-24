from django.shortcuts import render
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

TAIWAN=['全國','新北市','台北市','桃園市','台中市',
        '台南市','高雄市','宜蘭縣','新竹縣','苗栗縣',
        '彰化縣','南投縣','雲林縣','嘉義縣','屏東縣',
        '台東縣','花蓮縣','澎湖縣','基隆市','新竹市','嘉義市']

def parse_quarter(quarter):
    year, quarter = quarter.split('Q')
    return int(year) * 4 + int(quarter)

def plot(request):
    df = pd.read_csv('myapp\\TCT.csv', encoding='Big5')
    df = df.iloc[::-1]
    available_quarters = df['年度季別'].unique()
    available_quarters = available_quarters[::-1]

    selected_region = request.GET.get('region')
    selected_start_quarter = request.GET.get('quarterstart')
    selected_end_quarter = request.GET.get('quarterend')

    if selected_start_quarter and selected_end_quarter:
        start_date = parse_quarter(selected_start_quarter)
        end_date = parse_quarter(selected_end_quarter)

        # 自动修正时间段的顺序
        if start_date > end_date:
            selected_start_quarter, selected_end_quarter = selected_end_quarter, selected_start_quarter
            start_date, end_date = end_date, start_date

        df = df[(df['年度季別'].apply(parse_quarter) >= start_date) & (df['年度季別'].apply(parse_quarter) <= end_date)]

    if selected_region == '全國各縣市':
        cities = TAIWAN
    elif selected_region == '北部':
        cities = ['台北市', '新北市', '桃園市', '新竹縣', '基隆市', '宜蘭縣']
    elif selected_region == '中部':
        cities = ['台中市', '彰化縣', '南投縣', '苗栗縣', '雲林縣']
    elif selected_region == '南部':
        cities = ['嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '澎湖縣']
    elif selected_region == '東部':
        cities = ['台東縣', '花蓮縣']
    else:
        cities = ['全國']  # 預設值

    fig = px.line(df, x='年度季別', y=cities, title='房價所得比趨勢圖')

    average_line = df[cities].mean(axis=1)  # 平均值数据
    fig.add_scatter(x=df['年度季別'], y=average_line, mode='lines', name='平均值',line=dict(color='red',width=5,dash='dot'))

    fig.update_layout(
        width=1600,
        height=800,
        yaxis_title='房價所得比'
    )

    plot_html = fig.to_html(full_html=False)

    context = {
        'selected_region' : selected_region,
        'plot_html': plot_html,
        'quarters': available_quarters,
        'selected_start_quarter': selected_start_quarter,
        'selected_end_quarter': selected_end_quarter
    }

    return render(request, 'myapp/line.html', context)

def bar(request):
    df = pd.read_csv('myapp\\TCT.csv', encoding='Big5')
    df = df.iloc[::-1]
    available_quarters = df['年度季別'].unique()
    available_quarters = available_quarters[::-1]

    selected_region = request.GET.get('region')
    selected_start_quarter = request.GET.get('quarterstart')
    selected_end_quarter = request.GET.get('quarterend')
    selected_mode = request.GET.get('mode')

    if selected_start_quarter and selected_end_quarter:
        start_date = parse_quarter(selected_start_quarter)
        end_date = parse_quarter(selected_end_quarter)

        # 自动修正时间段的顺序
        if start_date > end_date:
            selected_start_quarter, selected_end_quarter = selected_end_quarter, selected_start_quarter
            start_date, end_date = end_date, start_date

        df = df[(df['年度季別'].apply(parse_quarter) >= start_date) & (df['年度季別'].apply(parse_quarter) <= end_date)]

    if selected_region == '全國各縣市':
        cities = TAIWAN
    elif selected_region == '北部':
        cities = ['台北市', '新北市', '桃園市', '新竹縣', '基隆市', '宜蘭縣']
    elif selected_region == '中部':
        cities = ['台中市', '彰化縣', '南投縣', '苗栗縣', '雲林縣']
    elif selected_region == '南部':
        cities = ['嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '澎湖縣']
    elif selected_region == '東部':
        cities = ['台東縣', '花蓮縣']
    else:
        cities = ['全國']  # 預設值

    # 计算每个季度各个城市的房价收入比平均值
    avg_values = df.groupby('年度季別')[cities].mean().reset_index()

    fig = go.Figure()

    # 添加每个城市的柱状图
    for city in cities:
        fig.add_trace(go.Bar(
            x=avg_values['年度季別'],
            y=avg_values[city],
            name=city
        ))

    # 添加平均值的折线图
    fig.add_trace(go.Scatter(
        x=avg_values['年度季別'],
        y=avg_values[cities].mean(axis=1),
        mode='lines',
        name='平均值',
	line=dict(color='red',width=5,dash='dot')
    ))

    fig.update_layout(
        width=1600,
        height=800,
        yaxis_title='房價所得比',
        barmode=selected_mode
    )

    plot_html = fig.to_html(full_html=False)

    context = {
        'selected_mode': selected_mode,
        'selected_region': selected_region,
        'plot_html': plot_html,
        'quarters': available_quarters,
        'selected_start_quarter': selected_start_quarter,
        'selected_end_quarter': selected_end_quarter
    }
    return render(request, 'myapp/bar.html', context)


def rader(request):
    df = pd.read_csv('myapp\\TCT.csv', encoding='Big5')
    df = df.iloc[::-1]
    available_years = df['年度季別'].str[:3].unique()
    available_years = available_years[::-1]
    line_colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'pink', 'cyan', 'magenta', 'teal', 'lime', 'brown', 'gray', 'olive', 'navy', 'salmon', 'gold', 'indigo', 'coral', 'orchid', 'turquoise']
    # 取得選擇的地區和年份
    selected_region = request.GET.get('region')
    selected_year = request.GET.get('year')

    # 根據選擇的地區篩選資料
    if selected_region == '全國各縣市':
        cities = TAIWAN
    elif selected_region == '北部':
        cities = ['台北市', '新北市', '桃園市', '新竹縣', '基隆市', '宜蘭縣']
    elif selected_region == '中部':
        cities = ['台中市', '彰化縣', '南投縣', '苗栗縣', '雲林縣']
    elif selected_region == '南部':
        cities = ['嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '澎湖縣']
    elif selected_region == '東部':
        cities = ['台東縣', '花蓮縣']
    else:
        cities = ['全國']  # 預設值
    # 根據選擇的年份篩選資料
    filtered_df = df[df['年度季別'].str[:3] == selected_year] if selected_year else df
    filled_df = filtered_df.copy()
    filled_df = filled_df.append(filtered_df.iloc[0])

    # 使用 Plotly Express 繪製長條圖
    fig = px.histogram(filtered_df, x='年度季別', y=cities, title='地區分佈直方圖')
    fig.update_layout(width=1500, height=800, yaxis_title='全國房價所得比', barmode='group', xaxis_tickangle=45)

    # 將長條圖轉換為雷達圖
    radar_fig = go.Figure()

    for city, color in zip(cities, line_colors):
        radar_fig.add_trace(go.Scatterpolar(
        r=filled_df[city],
        theta=filled_df['年度季別'],
        name=city,
        mode='lines',
        line=dict(color=color, width=3),
        fill='none',
        hovertemplate='%{r:.2f}',
    ))

    radar_fig.update_layout(
        polar=dict(
            angularaxis=dict(
                tickmode='array',
                tickvals=[0, 1, 2, 3, 4],
                ticktext=['第一季', '第二季', '第三季', '第四季', '第一季'],  # 添加第一季以形成封閉區域
                tickangle=45,
                direction='clockwise',
                rotation=45
            ),
            radialaxis=dict(
                visible=True,
                range=[0, filled_df[cities].max().max()]  # 根據資料範圍設定適當的範圍
            )
        ),
        showlegend=True,
        title='地區分佈雷達圖',
        width=800,
        height=800
    )

    # 將雷達圖轉換為HTML
    radar_html = radar_fig.to_html(full_html=False)

    context = {
        'selected_region': selected_region,
        'plot_html': radar_html,
        'years': available_years,
        'selected_year': selected_year
    }
    return render(request, 'myapp/rader.html', context)



def home(request):
    return render(request, 'myapp/home.html')
