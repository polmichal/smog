# -*- coding: ISO-8859-2 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def rysuj_wykres(plik):
    column_names = ['CZAS','PM10','PM2.5']
    path = plik
    df = pd.read_csv(path,delimiter=';',header=None)     
    df2 = df.drop(df.index[[0,-1,-2,-3]])
    df2.columns=column_names    
    df3 = df2.convert_objects(convert_numeric=True)    
    df4 = df3.dropna()    
    czas = df4.iloc[:,0]    
    pm10 = df4.iloc[:,1]
    pm2 = df4.iloc[:,2]    
    fig = plt.figure(facecolor=("#F1F8E9")) # B0BEC5#DCEDC8 #B2EBF2 #81D4FA 
    plt.title('Poziom zanieczyszczenia powietrza w Olsztynie\nczujnik ul.Puszkina',fontsize=14)
    plt.xlabel('Czas', fontsize=13)    
    plt.xticks(np.arange(len(czas)),rotation=50)    
    plt.ylabel('Poziom pyłów',fontsize=14)    
    ax = plt.axes()
    ax.plot(czas,pm10)
    ax.plot(czas, pm2)    
    ax.grid()
    ax.axhline(y=50, xmin=0,color='r', linestyle = '--', label='poziom dopuszczalny')
    ax.legend(['Pył PM10', 'Pył PM2.5', 'Poziom dopuszczalny'], loc='upper left')
    ax.set_facecolor(color='peachpuff')    
    plt.show()    
    
rysuj_wykres('dane-pomiarowe_2018-12-22_17-23-54.csv')
