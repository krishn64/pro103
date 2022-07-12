import pandas as pd
import plotly.express as px

df = pd.read_csv("C103 PROJECT.csv")
fig = px.scatter(df,x="date",y="cases",color="country")
fig.show()








