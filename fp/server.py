from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd


app = Flask(__name__, static_folder="templates")

dfc = pd.read_csv('Labor_force_participation_rate_ female.csv',encoding = 'utf8')
dfc1 =dfc.dropna(axis=0,how='any')

dfe = pd.read_csv('School_enrollment.csv',encoding = 'utf8')
dfe1=dfe.set_index('country')

Canada = list(dfe1.loc["Canada"].values)[0:]
Nepal = list(dfe1.loc["Nepal"].values)[0:]
Brazil = list(dfe1.loc["Brazil"].values)[0:]
Egypt = list(dfe1.loc["Egypt, Arab Rep."].values)[0:]
Cambodia=list(dfe1.loc["Cambodia"].values)[1:]
Rwanda=list(dfe1.loc["Rwanda"].values)[1:]
Madagascar=list(dfe1.loc["Madagascar"].values)[1:]


def bar_base() -> Bar:
    x = [int(x)for x in dfc1.columns.values[1:]]
    c = (
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
    return c


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()(debug=True, port=8000)
