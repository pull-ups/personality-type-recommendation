#!/usr/bin/env python
# coding: utf-8

# In[241]:


import numpy as np
from pyecharts.charts import Radar, Bar
from pyecharts import options as opts

def radar_chart(labels):
    
    labels = [int(i) for i in list((np.array(labels) - 1) / 6 *100)]
    data = [[labels[0], labels[7], labels[5], labels[3], labels[1], labels[6], labels[4], labels[2]]]

    chart = (Radar(init_opts=opts.InitOpts(theme='dark'))
            .add_schema(schema=[opts.RadarIndicatorItem(name="E", min_=-10, max_=110),
                                opts.RadarIndicatorItem(name="J", min_=-10, max_=110),
                                opts.RadarIndicatorItem(name="T", min_=-10, max_=110),
                                opts.RadarIndicatorItem(name="N", min_=-10, max_=110),
                                opts.RadarIndicatorItem(name="I", min_=-10, max_=110),
                                opts.RadarIndicatorItem(name="P", min_=-10, max_=110),
                                opts.RadarIndicatorItem(name="F", min_=-10, max_=110),
                                opts.RadarIndicatorItem(name="S", min_=-10, max_=110)],
                                textstyle_opts=opts.TextStyleOpts(font_size=20))
            .add('성격유형', data, label_opts=opts.LabelOpts(is_show=False),
                areastyle_opts=opts.AreaStyleOpts(opacity=0.7), color='pink',
                linestyle_opts=opts.LineStyleOpts(width=2, color="white"),
                tooltip_opts=opts.TooltipOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title='당신의 성격유형은', pos_left='center'),
                            legend_opts=opts.LegendOpts(is_show=False))
            )
    
    return chart.render()

