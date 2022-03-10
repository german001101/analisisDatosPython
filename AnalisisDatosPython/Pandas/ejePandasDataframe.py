#!/usr/bin/env python3
 
import pandas as pd

dataframe = pd.read_csv(r'/home/gburgos/Documents/AnalisisDatosPython/Pandas/dataFrame.csv')

print(dataframe)

#print(dataframe.Pais)

#print(dataframe[['Edad','Automovil']])
#Contar valores repetidos
#print(dataframe.Automovil.value_counts())
#Ordenando valores
#print(dataframe.Pais.value_counts(ascending=True))#dropna=False valores nulos
#print(dataframe.Pais.sort_values())
#print(dataframe.Pais.sort_values(by=['Nombre y apellido','Edad']))

#Filtrar información de python

