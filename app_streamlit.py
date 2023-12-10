import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score

import plotly.graph_objects as go

df = pd.read_csv("telco_customer_churn.csv")

orginal_data = pd.read_csv('data.csv', sep=',')
data = orginal_data.copy(deep=True)

st.header("Telco Customer Churn")
# 
st.markdown(
    "First i cleaned my dataset a bit")




st.subheader("Some values")



st.code('''print(df.tenure.mean().round(2))
print(df.tenure.median())
print(df.tenure.std())
''')

st.markdown("17.98")
st.markdown("10.08")
st.markdown("19.531123054519615")
