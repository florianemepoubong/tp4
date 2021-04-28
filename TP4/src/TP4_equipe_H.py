
#!/usr/bin/env python
# coding: utf-8

# In[250]:

#Importation de librairies

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Lecture de fichier csv et affichage des 5 premièrs lignes du fichier
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')


print(df.columns) # Affichage des différentes entrées/colonnes du fihiers csv
df.head() # Affichage des premières lignes du fihier csv

#convertir la colone 'Date' en Datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
#Compter le nombre d'occurence de chaque date ou les informations ont été transmises aux commercants lors du sondage
df_group_by_date = df.groupby(['Date'])['Date'].count()
print(df_group_by_date)
#Affichage du diagramme sur le nombre d'appels de commercants par date
df_group_by_date.plot()

plt.title('Nombre appels de commerce par date')
plt.xlabel('Date')
plt.ylabel('Nombre appels')
plt.show()


# diagramme représentatif du statut des différents commerces
df_group_by_statut = df.groupby(['Statut du commerce'])['Statut du commerce'].count()
print(df_group_by_statut)

df_group_by_statut.plot.pie()
#plt.title('Nombre d'appels par statut du commerce')
plt.show()


# In[23]:
# Nombre de commerces contactés par phase pour le sondage
df_group_by_phase = df.groupby(['Phase'])['Statut du commerce'].count()
print(df_group_by_phase)

df_group_by_phase.plot.bar()
plt.title('Commerces contactés par phase')
plt.xlabel('phases')
plt.ylabel('Nombre de commerce')
plt.show()


# In[7]:
# Description de données sur la colonne 'Arrondissement / Ville liée'
df_group_by_date = df['Arrondissement / Ville liée'].describe()
print(df_group_by_date)

# In[8]:
# Données agrégées sur le statut de commerce par arrondissement
df['Arrondissement / Ville liée'].value_counts()

# In[9]:
# Données agrégées sur le statut de commerce par ville
df_group_by_date = df.groupby(['Arrondissement / Ville liée','Statut du commerce'])['Statut du commerce'].count()

print(df_group_by_date)

# In[27]:
# Données agrégées sur le statut de commerce par date
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')

df_group_by_date = df.groupby(['Date','Statut du commerce'])['Statut du commerce'].count()
print(df_group_by_date)
#df_group_by_date.plot()


# In[11]:
#Courbe représentative de nombre de commerces ouverts par date
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
df_ouvert = df[df['Statut du commerce'] == "Ouvert"]
df_group_by_date_ouvert = df_ouvert.groupby(['Date'])['Date'].count()
#df_group_by_date_ouvert
df_group_by_date_ouvert.plot()

plt.title('Commerces ouverts par date')
plt.xlabel('Date')
plt.ylabel('Commerces ouverts')
plt.show()


# In[12]:

#Courbe représentative de nombre de commerces fermés par date
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
df_fermes = df[df['Statut du commerce'] == "Fermé"]
df_group_by_date_fermes= df_fermes.groupby(['Date'])['Date'].count()
df_group_by_date_fermes.plot()

plt.title('Commerces fermés par date')
plt.xlabel('Date')
plt.ylabel('Commerces fermés')
plt.show()


# In[70]:
# Statistiques sur l'intéret des commerces pour accompagenement numérique
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
#fig, ax = plt.subplots(figsize=(15,7))
#df_group_by_numerique = df.groupby(['Statut du commerce',"Intérêt pour le programme d'accompagnement pour le virage numérique des entreprises?"])['Statut du commerce'].count().unstack().plot(ax=ax)
#Affichage du diagramme à barre pour mieux visualiser
df_group_by_numerique = df.groupby(["Statut du commerce","Intérêt pour le programme d'accompagnement pour le virage numérique des entreprises?"])["Statut du commerce"].count().unstack(0).plot.barh()
plt.title('Intéret pour accompagenement numérique')
plt.xlabel('Commerces par statut')
plt.ylabel('Interet')
plt.show()

# In[14]:

#Données agrégées sur le statut des commerce et leur canal de vente
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
#fig, ax = plt.subplots(figsize=(15,7))
#df_group_by_agregee = df.groupby(['Statut du commerce',"Intérêt pour le programme d'accompagnement pour le virage numérique des entreprises?"])['Statut du commerce'].count().unstack().plot(ax=ax)
df_group_by_agregee = df.groupby(["Statut du commerce",'Canal de vente en ligne'])['Statut du commerce'].count()
print(df_group_by_agregee)

# In[15]:

#Statistiques de réponses des commerces sur la vente en ligne et leur canal de vente
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
#fig, ax = plt.subplots(figsize=(15,7))
#df_group_by_vente_ligne = df.groupby(['Statut du commerce',"Intérêt pour le programme d'accompagnement pour le virage numérique des entreprises?"])['Statut du commerce'].count().unstack().plot(ax=ax)
df_group_by_vente_ligne = df.groupby(["Faites-vous de la vente en ligne?",'Canal de vente en ligne'])['Faites-vous de la vente en ligne?'].count()
print(df_group_by_vente_ligne)

# In[75]:

# In[17]:

#Statistiques sur les commerces avec enjeux pour le maintien d'opérations, les ressources humaines et la vente en ligne
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
#df_fermes = df[df['Enjeux: Maintien des opérations?'] == "Oui"]
df_group_by_enjeux = df.groupby(['Date'])[['Enjeux: Ressources humaines?', 'Enjeux: Maintien des opérations?', 'Faites-vous de la vente en ligne?']].count()
print(df_group_by_enjeux)
#Calul de corrélation sur les réponses de commerces à ces questions
print(df_group_by_enjeux.corr())
df_group_by_enjeux.plot()
plt.show()


# In[ ]:
# In[18]:
#df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
#df_fermes = df[df['Enjeux: Maintien des opérations?'] == "Oui"]
df_group_by_enjeux= df.groupby(['Date'])[['Enjeux: Ressources humaines?', 'Faites-vous de la vente en ligne?']].count()
print(df_group_by_enjeux.corr())
df_group_by_enjeux.plot()
plt.show()
# In[59]:

#statistiques sur les commerces ayant un intérêt pour le programme d'aide d'urgence,pour le programme d'accompagnement pour le virage vers le numérique, et sur utilité de information transmise
#df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
df_oui = df[df["Intérêt pour le programme d'aide d'urgence?"] == "Oui"]
df_oui = df[df['Intérêt pour le programme d\'accompagnement pour le virage numérique des entreprises?'] == "Oui"]
df_oui = df[df['Est-ce que l\'information que nous vous avons donnée vous a été utile?'] == "Oui"]
#Affichage de statistique de commerce ayant répondu oui aux trois questions
print(df_oui)
df_group_by_interet = df.groupby(['Date'])[['Intérêt pour le programme d\'aide d\'urgence?', 'Intérêt pour le programme d\'accompagnement pour le virage numérique des entreprises?', 'Est-ce que l\'information que nous vous avons donnée vous a été utile?']].count()
#df_group_by_interet = df.groupby(['Date'])[["Intérêt pour le programme d'aide d'urgence?", 'Intérêt pour le programme d\'accompagnement pour le virage numérique des entreprises?', 'Est-ce que l\'information que nous vous avons donnée vous a été utile?']].count()

#print(df_group_by_interet)
#Calcul de corrélation
print(df_group_by_interet.corr())
# Affichage de courbe pour visualiser la correlation
df_group_by_interet.plot()
plt.show()


#statistiques sur les commerces ayant un intérêt pour le programme d'aide d'urgence,pour le programme d'accompagnement pour le virage vers le numérique, et sur utilité de information transmise
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
df_oui = df[df["Intérêt pour le programme d'aide d'urgence?"] == "Oui"]
df_oui = df[df['Intérêt pour le programme d\'accompagnement pour le virage numérique des entreprises?'] == "Oui"]
df_oui = df[df['Est-ce que l\'information que nous vous avons donnée vous a été utile?'] == "Oui"]
#Affichage de statistique de commerce ayant répondu oui aux trois questions

df_group_by_interet = df.groupby(['Date'])[['Intérêt pour le programme d\'aide d\'urgence?', 'Intérêt pour le programme d\'accompagnement pour le virage numérique des entreprises?', 'Est-ce que l\'information que nous vous avons donnée vous a été utile?']].count()
#df_group_by_interet = df.groupby(['Date'])[["Intérêt pour le programme d'aide d'urgence?", 'Intérêt pour le programme d\'accompagnement pour le virage numérique des entreprises?', 'Est-ce que l\'information que nous vous avons donnée vous a été utile?']].count()

#Calcul de corrélation
print(df_group_by_interet.corr())
# Affichage de courbe pour visualiser la correlation
df_group_by_interet.plot()
plt.show()

# In[49]:
#df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
#fig, ax = plt.subplots(figsize=(15,7))
#df_group_by_aide_urgence = df.groupby(['Statut du commerce',"Intérêt pour le programme d'accompagnement pour le virage numérique des entreprises?"])['Statut du commerce'].count().unstack().plot(ax=ax)
df_group_by_aide_urgence = df.groupby(['Intérêt pour le programme d\'aide d\'urgence?','Statut du commerce'])['Intérêt pour le programme d\'aide d\'urgence?'].count().unstack(0).plot.barh()
plt.show()


# In[63]:
# Statistique sur les enjeux de soutien financier par statut du commerce
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
#fig, ax = plt.subplots(figsize=(15,7))
#df_group_by_soutien_financier = df.groupby(['Statut du commerce',"Intérêt pour le programme d'accompagnement pour le virage numérique des entreprises?"])['Statut du commerce'].count().unstack().plot(ax=ax)
df_group_by_soutien_financier = df.groupby(['Enjeux: Soutien financier?','Statut du commerce'])['Enjeux: Soutien financier?'].count().unstack(0).plot.barh()
plt.title('Soutien financier par statut du commerce')
plt.ylabel('Statut du commerce')
plt.show()

# In[74]:

# Statistique sur réponses des commerces avec enjeux de santé, sécurité
df = pd.read_csv('../data/j_informe_les_commercants.csv', sep = ',')
#fig, ax = plt.subplots(figsize=(15,7))
#df_group_by_accompagnement = df.groupby(['Statut du commerce',"Intérêt pour le programme d'accompagnement pour le virage numérique des entreprises?"])['Statut du commerce'].count().unstack().plot(ax=ax)
df_group_by_accompagnement = df.groupby(['Enjeux: Santé et sécurité?','Statut du commerce'])['Enjeux: Soutien financier?'].count().unstack(0).plot.barh()
print(df_group_by_accompagnement)
plt.show()


#Statistique de l'utilité des enjeux
df_group_by_utilite = df.groupby(['Date'])[['Enjeux: Santé et sécurité?',"Enjeux: Recherche d'équipement sanitaire?", 'Enjeux: Soutien financier?','Est-ce que l\'information que nous vous avons donnée vous a été utile?']].count()
#Calcul de corrélation sur les commerces qui ont trouvé de l'utilité aux informations transmises et les enjeux sanitaire rencontrés par ces commerces
print(df_group_by_utilite.corr())
# Affichage de courbe pour visualiser la correlation
df_group_by_utilite.plot()

plt.title('Observation des enjeux')
plt.show()

