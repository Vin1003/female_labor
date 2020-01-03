from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Grid,Scatter 
import pandas as pd 
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Tab, Pie, Line
from pyecharts.components import Table

app = Flask(__name__, static_folder="templates")

dfa = pd.read_csv('Employment_to_population_ratio.csv',encoding = 'utf8')
dfa1 =dfa.dropna(axis=0,how='any')

dfb = pd.read_csv('Labor_force_participation_rate_male.csv',encoding = 'utf8')
dfb1 =dfb.dropna(axis=0,how='any')

dfc = pd.read_csv('Labor_force_participation_rate_ female.csv',encoding = 'utf8')
dfc1 =dfc.dropna(axis=0,how='any')

def timeline_map_a() -> Timeline:
    tl = Timeline()
    for i in range(2009,2020):
        map0 = (
            Map()
            .add(
                "总就业人口比率", (list(zip(list(dfa1.country),list(dfa1["{}".format(i)])))), "world",is_map_symbol_show = False
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="".format(i),subtitle="",
                                         subtitle_textstyle_opts=opts.TextStyleOpts(color="red",font_size=16,font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=0, max_=100,series_index=0),
            
            )
        )
        tl.add(map0, "{}".format(i))
    return tl

def timeline_map_b() -> Timeline:
    tl = Timeline()
    for i in range(2009,2020):
        map0 = (
            Map()
            .add(
                "男性劳动力参与率", (list(zip(list(dfb1.country),list(dfb1["{}".format(i)])))), "world",is_map_symbol_show = False
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="".format(i),subtitle="",
                                         subtitle_textstyle_opts=opts.TextStyleOpts(color="blue",font_size=16,font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=0, max_=100,series_index=0),
            
            )
        )
        tl.add(map0, "{}".format(i))
    return tl

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
    return tl


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    tl = bar_base()
    return ti.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()(debug=True, port=8000)
