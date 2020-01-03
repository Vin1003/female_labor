from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Line

df1 = pd.read_csv("School_enrollment.csv", encoding='gbk')
df2 = pd.read_csv("Labor_force_participation_rate_ female.csv", encoding='gbk')
df3 = pd.read_csv("Employment_to_population_ratio.csv", encoding='gbk')

app = Flask(__name__)

# 准备工作
regions_available_female_school = list(df1.country.dropna().unique())
regions_available_female_labor = list(df2.country.dropna().unique())
regions_available_labor = list(df3.country.dropna().unique())


# cf.set_config_file(offline=True, theme="ggplot")
# py.offline.init_notebook_mode()

@app.route('/', methods=['GET'])
def female_school():
    data_str = df1.to_html()
    return render_template('results1.html',
                           the_res=data_str,
                           the_select_region=regions_available_female_school)


@app.route('/', methods=['GET'])
def female_labor():
    data_str = df2.to_html()
    return render_template('results2.html',
                           the_res=data_str,
                           the_select_region=regions_available_female_labor)

@app.route('/', methods=['GET'])
def labor():
    data_str = df3.to_html()
    return render_template('results3.html',
                           the_res=data_str,
                           the_select_region=regions_available_labor)


@app.route('/hurun', methods=['POST'])
def female_school_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df1.query("country=='{}'".format(the_region))
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
    return render_template('results1.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=regions_available_female_school,
                           )


@app.route('/hurun', methods=['POST'])
def female_labor_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df1.query("country=='{}'".format(the_region))
    #     df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
    #     print(df_summary.head(5)) # 在后台检查描述性统计
    #     ## user select
    # print(dfs)
    #     # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example2.html", auto_open=False)
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
                           the_select_region=regions_available_female_labor,
                           )

@app.route('/hurun', methods=['POST'])
def labor_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df1.query("country=='{}'".format(the_region))
    #     df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
    #     print(df_summary.head(5)) # 在后台检查描述性统计
    #     ## user select
    # print(dfs)
    #     # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example3.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    #     # plotly.offline.plot(data, filename='file.html')

    #     with open("render.html", encoding="utf8", mode="r") as f:
    #         plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results3.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=regions_available_labor,
                           )


if __name__ == '__main__':
    app.run(debug=True, port=8000)