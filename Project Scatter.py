import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\vedan\Desktop\Data Visualization\Data-visualization-master\Teacher refrence\data.csv")
fig = px.scatter(df, x="Country", y="Population")
fig.show()
