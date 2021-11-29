import streamlit as st
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

data = pd.read_csv('dataset.csv')

#st.pyplot((data.head(2000)['country'].hist(bins=100)).figure)


def histogrammeVarDiscrete(data,categ):
    return data[categ].value_counts().plot.bar(figsize=(12,6)).figure


def cardinalite(data,categ=None):
    plt.title("Cardinalité")
    plt.xlabel('Variables')
    plt.ylabel('Nombre de catégories uniques')
    if(categ is None):
        return data.nunique().plot.bar(figsize=(12,6)).figure
    else:
        return data[categ].nunique().plot.bar(figsize=(12,6)).figure


# bar plot de variables catégorielles
def barPlot(data,categ): 
    plt.xticks(rotation=0)
    return data[categ].value_counts().plot.bar().figure

#Quantifier les données manquantes
def dataNull(data,moyen):
    plt.xlabel('Variables')
    plt.title('Données manquantes')
    if(moyen == 'somme'):
        plt.ylabel('Somme des valeurs manquantes')
        return data.isnull().sum().plot.bar(figsize=(12,6)).figure
    else:
        plt.ylabel('Moyenne des valeurs manquantes')
        return data.isnull().mean().plot.bar(figsize=(12,6)).figure

#renommer variables rares dans une catégorie

def nomVarDansCat(data,categ):
    return data[categ].unique()

def renameVarInCateg(data,categ,oldVar,newVar):
    data.loc[data.embarked==oldVar,categ] = newVar

def calculValeurCateg(data,categ):
    return data[categ].value_counts()
    
#permet de calculer la frequence pour une catégorie de notre dataset
def frequenceCateg(data,categ):
    retour = data[categ].value_counts() / len(data)
    fig = retour.plot.bar(figsize=(12,6))
    fig.axhline(y=0.10,color='red')
    fig.set_ylabel('Pourcentage de passagers')
    fig.set_xlabel('Variable: '+categ)
    fig.set_title('Identifier les catégories rares')
    return fig.figure



#st.pyplot(cardinalite(data,'country'))
st.write(frequenceCateg(data,'country'))


