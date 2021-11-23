import streamlit as st
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

data = pd.read_csv('dataset.csv')

st.pyplot((data.head(2000)['country'].hist(bins=100)).figure)


def histogrammeVarDiscrete(data,var):
    return data[var].hist(bins=50).figure
