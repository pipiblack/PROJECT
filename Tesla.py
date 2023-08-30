import pandas as pd
import json
from bs4 import BeautifulSoup
import requests
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_graphs(stock_data,revenue_data,stock):
    fig = make_subplots(rows=2,cols=1,shared_axes=True,subplots_title=("Historical_share_price","Historical_revenue"),vertical_spacing=.3)
    stock_data_specific = stock_data[stock.Date <='2021--06-14']
    revenue_data_specific = stock_data[stock.Date <= "2021-04-30"]
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.tail(20))

# scrap and visualize the data

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

table = soup.find("table",{"table":"wikitable"})
if table is not None:
    table_rows = table.find_all('tr')

    data = []
    for row in table_rows[1:]:
        columns = row.find_all('td')
        date = columns[0].text.strip()
        revenue = columns[1].text.strip()
        data.append([date, revenue])

    netflix_revenue = pd.DataFrame(data, columns=["Date", "Revenue"])

    print(netflix_revenue)
else:
    print("Table not found.")
