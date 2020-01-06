from flask import Flask, render_template, request
from pyecharts import options as opts
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Grid,Scatter
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Tab, Pie, Line
from pyecharts.components import Table
import csv
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

dfa = pd.read_csv('Employment_to_population_ratio.csv',encoding = 'utf8')
dfa1 =dfa.dropna(axis=0,how='any')
x轴 = [int(x)for x in dfa1.columns.values[-11:]]
dfa2=print(list(dfa1.country))
总就业人口比率= list(zip(list(dfa1.country)))
dfb = pd.read_csv('Labor_force_participation_rate_male.csv',encoding = 'utf8')
dfb1 =dfb.dropna(axis=0,how='any')
dfb2=print(list(dfb1.country))
男性劳动力参与率 = list(zip(list(dfb1.country)))
dfc = pd.read_csv('Labor_force_participation_rate_ female.csv',encoding = 'utf8')
dfc1 =dfc.dropna(axis=0,how='any')
女性劳动力参与率 = list(zip(list(dfc1.country)))
dfc2=dfc1.set_index('country')
Canada = list(dfc2.loc["Canada"].values)[1:]
United_Arab_Emirates=list(dfc2.loc["United Arab Emirates"].values)[1:]
Nepal=list(dfc2.loc["Nepal"].values)[1:]
Brazil=list(dfc2.loc["Brazil"].values)[1:]
Egypt=list(dfc2.loc["Egypt, Arab Rep."].values)[1:]
Cambodia=list(dfc2.loc["Cambodia"].values)[1:]
Rwanda=list(dfc2.loc["Rwanda"].values)[1:]
Madagascar=list(dfc2.loc["Madagascar"].values)[1:]
x = [int(x)for x in dfc1.columns.values[1:]]
dfe = pd.read_csv('School_enrollment.csv',encoding = 'utf8')
dfe1=dfe.set_index('country')
Canada = list(dfe1.loc["Canada"].values)[0:]
Nepal = list(dfe1.loc["Nepal"].values)[0:]
Brazil = list(dfe1.loc["Brazil"].values)[0:]
Egypt = list(dfe1.loc["Egypt, Arab Rep."].values)[0:]
Cambodia=list(dfe1.loc["Cambodia"].values)[1:]
Rwanda=list(dfe1.loc["Rwanda"].values)[1:]
Madagascar=list(dfe1.loc["Madagascar"].values)[1:]
# type = dfa1['country'].tolist()


def timeline_map_c() -> Timeline:
    tl = Timeline()
    for i in range(2009,2020):
        map0 = (
            Map()
            .add(
                "女性劳动力参与率", (list(zip(list(dfc1.country),list(dfc1["{}".format(i)])))), "world",is_map_symbol_show = False
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="".format(i),subtitle="",
                                         subtitle_textstyle_opts=opts.TextStyleOpts(color="blue",font_size=16,font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=0, max_=100,series_index=0),
            
            )
        )
        tl.add(map0, "{}".format(i))
    return tl.render_embed()


def bar_base() -> Bar:
    x =  [int(x)for x in dfc1.columns.values[1:]]
    d = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("加拿大", Canada)
        .add_yaxis("阿拉伯",United_Arab_Emirates)
        .add_yaxis("尼泊尔", Nepal)
        .add_yaxis("巴西", Brazil)
        .add_yaxis("埃及", Egypt)
        .add_yaxis("柬埔寨", Cambodia)
        .add_yaxis("卢旺达", Rwanda)
        .add_yaxis("马达加斯加", Madagascar)
        .set_global_opts(title_opts=opts.TitleOpts(title="女性劳动力劳动参与率", subtitle="2009-2019"))
    )
    return d.render_embed()


def line_base() -> Line:
    e = (
        Line()
        .add_xaxis(['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])
        .add_yaxis("加拿大", Canada)
        .add_yaxis("阿拉伯",United_Arab_Emirates)
        .add_yaxis("尼泊尔", Nepal)
        .add_yaxis("巴西", Brazil)
        .add_yaxis("埃及", Egypt)
        .add_yaxis("柬埔寨", Cambodia)
        .add_yaxis("卢旺达", Rwanda)
        .add_yaxis("马达加斯加", Madagascar)
        .set_global_opts(title_opts=opts.TitleOpts(title="女性劳动力劳动参与率"))
    )
    return e.render_embed()

def bar_base() -> Bar:
    x = [int(x)for x in dfc1.columns.values[1:]]
    f = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("加拿大", Canada)
        .add_yaxis("尼泊尔", Nepal)
        .add_yaxis("巴西", Brazil)
        .add_yaxis("埃及", Egypt)
        .add_yaxis("柬埔寨", Cambodia)
        .add_yaxis("卢旺达", Rwanda)
        .add_yaxis("马达加斯加", Madagascar)
        .set_global_opts(title_opts=opts.TitleOpts(title="高等学校女性入学比例", subtitle="2009-2019"))
    )
    return f.render_embed()


# regions_available = list(dfa.country.dropna().unique())
#regions_available = list(dfb.country.dropna().unique())
#regions_available = list(dfc.country.dropna().unique())
#regions_available = list(dfe.country.dropna().unique())
regions_available = list(dfa1.country.dropna().unique())

# cf.set_config_file(offline=True, theme="ggplot")


@app.route('/', methods=['GET'])
def female_labor():
    data_str = dfc1.to_html()
    return render_template('results2.html',
                           the_res=data_str,
                           the_select_region=regions_available)


@app.route('/hurun', methods=['POST'])
def hurun() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = dfc1.query("country=='{}'".format(the_region))
    #     df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
    #     print(df_summary.head(5)) # 在后台检查描述性统计
    #     ## user select
    # print(dfs)
    #     # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    #     # plotly.offline.plot(data, filename='file.html')

    #     with open("render.html", encoding="utf8", mode="r") as f:
    #         plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=regions_available,
                           )

@app.route('/map',methods=['GET'])
def timeline_map() -> Timeline:
        return render_template('female_render.html')
#链接地图html页面

@app.route('/worldhhh',methods=['POST'])
def world_exports():
    data_world = dfb.to_html()
    return render_template('exports_data2.html',
                           the_res = data_world,)

@app.route('/uncn',methods=['POST'])
def uncn():
    return render_template('fsl.html',
                           the_plot_all=bar_base())


@app.route('/worldppp',methods=['POST'])
def worldphoto():
    return render_template('female_labor.html')



if __name__ == '__main__':
    app.run(debug=True)




