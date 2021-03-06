

print("UNEMPLOYMENT REPORT...")

import os
import json
from alphavantage_api import pull
import requests
import kaleido


data = pull()


#
# DATA AND CHARTING
#

from pandas import DataFrame
from plotly.express import bar

yax = range(0,10)
df = DataFrame(data)
#df1 = df["value"].copy()
#sdf = df1.sort_index(0,ascending = False, inplace = False)
#print(sdf.head())
#print(df1.head())
#df = df.values.sort_values(0,0,ascending=True)
#print(df.head())

fig = bar(df, x="date", y="value", title="Unemployment Rates", range_y=(0,10))
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html

# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_yaxes
# https://plotly.com/python/reference/layout/yaxis/
# https://plotly.com/python/reference/layout/yaxis/#layout-yaxis-ticksuffix

fig.update_yaxes(
    #tickprefix="$",
    ticksuffix="%",
    showgrid=True
)

fig.update_layout(autotypenumbers='convert types')

fig.show()

#breakpoint()

print("CSV EXPORT...")
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.csv")
df.to_csv(csv_filepath, index=False)


print("DATAVIZ EXPORT...")
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_image
# fig.to_image(format="png")

# https://plotly.com/python/static-image-export/
# Image export using the "kaleido" engine requires the kaleido package,
#which can be installed using pip:
#    $ pip install -U kaleido
img_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.png")
fig.write_image(img_filepath)

exit()
