# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:24:51 2021

@author: nicol
"""

import numpy as np
import pandas as pd
import evaluate as ev

fra_excel = True
#%% Nes
if not fra_excel:
    # Laster inn csv-filer
    nes_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_pred_ar5_endring.csv", low_memory=False)
    nes_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_ruter_med_tresatt_myr.csv")
    
    nes_results = ev.evaluate_predictions(nes_df, 100, nes_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score.xlsx")
    nes_results_for = ev.evaluate_artype_for(nes_df, nes_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_for.xlsx")
    nes_results_etter = ev.evaluate_artype_etter(nes_df, nes_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_etter.xlsx")

#%% Nes laste inn fra excel
if fra_excel:
    nes_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score.xlsx")
    nes_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_for.xlsx", None)
    nes_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_etter.xlsx", None)

#%% Nes plotting
ev.artype_barplot(nes_results_for, nes_results, 30, "MCC", title="Nes kommune før endringer")
ev.artype_barplot(nes_results_etter, nes_results, 30, "MCC", title="Nes kommune etter endringer")

#%% Nord-Aurdal
if not fra_excel:
    # Laster inn csv-filer
    nordaurdal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_pred_ar5_endring.csv", low_memory=False)
    nordaurdal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_ruter_med_tresatt_myr.csv")
    
    nordaurdal_results = ev.evaluate_predictions(nordaurdal_df, 100, nordaurdal_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score.xlsx")
    print("Ferdig med resultater totalt")
    nordaurdal_results_for = ev.evaluate_artype_for(nordaurdal_df, nordaurdal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_for.xlsx")
    print("Ferdig med resultater før")
    nordaurdal_results_etter = ev.evaluate_artype_etter(nordaurdal_df, nordaurdal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_etter.xlsx")
    print("Ferdig med totale resultater etter")

#%% Nord-Aurdal laste inn fra excel
if fra_excel:
    nordaurdal_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score.xlsx")
    nordaurdal_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_for.xlsx", None)
    nordaurdal_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_etter.xlsx", None)

#%% Nord-Aurdal plotting
ev.artype_barplot(nordaurdal_results_for, nordaurdal_results, 50, "MCC", title="Nord-Aurdal kommune før endringer")
ev.artype_barplot(nordaurdal_results_etter, nordaurdal_results, 50, "MCC", title="Nord-Aurdal kommune etter endringer")

#%% Ullensaker
if not fra_excel:
    # Laster inn csv-filer
    ullensaker_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_pred_ar5_endring.csv", low_memory=False)
    ullensaker_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_ruter_med_tresatt_myr.csv")
    
    ullensaker_results = ev.evaluate_predictions(ullensaker_df, 100, ullensaker_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score.xlsx")
    print("Ferdig med resultater totalt")
    ullensaker_results_for = ev.evaluate_artype_for(ullensaker_df, ullensaker_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_for.xlsx")
    print("Ferdig med resultater før")
    ullensaker_results_etter = ev.evaluate_artype_etter(ullensaker_df, ullensaker_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_etter.xlsx")
    print("Ferdig med resultater etter")

#%% Ullensaker laste inn fra excel
if fra_excel:
    ullensaker_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score.xlsx")
    ullensaker_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_for.xlsx", None)
    ullensaker_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_etter.xlsx", None)

#%%  Ullensaker plotting
ev.artype_barplot(ullensaker_results_for, ullensaker_results, 60, "MCC", title="Ullensaker kommune før endringer")
ev.artype_barplot(ullensaker_results_etter, ullensaker_results, 60, "MCC", title="Ullensaker kommune etter endringer")

#%% Etnedal
if fra_excel:
    # Laster inn csv-filer
    etnedal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_pred_ar5_endring.csv", low_memory=False)
    etnedal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_ruter_med_tresatt_myr.csv")
    
    etnedal_results = ev.evaluate_predictions(etnedal_df, 100, etnedal_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score.xlsx")
    print("Ferdig med resultater totalt")
    etnedal_results_for = ev.evaluate_artype_for(etnedal_df, etnedal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score_artype_for.xlsx")
    print("Ferdig med resultater før")
    etnedal_results_etter = ev.evaluate_artype_etter(etnedal_df, etnedal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score_artype_etter.xlsx")
    print("Ferdig med resultater etter")

#%% Etnedal laste inn fra excel
if fra_excel:
    etnedal_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_score.xlsx")
    etnedal_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_score_artype_for.xlsx", None)
    etnedal_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_score_artype_etter.xlsx", None)

#%% Etnedal plotting

ev.artype_barplot(etnedal_results_for, etnedal_results, 50, "MCC", title="Etnedal kommune før endringer")
ev.artype_barplot(etnedal_results_etter, etnedal_results, 50, "MCC" ,title="Etnedal kommune etter endringer")

#%% Gjerdrum

if not fra_excel:
    # Laster inn csv-filer
    gjerdrum_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_pred_ar5_endring.csv", low_memory=False)
    gjerdrum_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_ruter_med_tresatt_myr.csv")
    
    gjerdrum_results = ev.evaluate_predictions(gjerdrum_df, 100, gjerdrum_tmyr['Id'], None, metrics="many", path = r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score.xlsx")
    print("Ferdig med resultater totalt")
    gjerdrum_results_for = ev.evaluate_artype_for(gjerdrum_df, gjerdrum_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score_artype_for.xlsx")
    print("Ferdig med resultater før")
    gjerdrum_results_etter = ev.evaluate_artype_etter(gjerdrum_df, gjerdrum_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score_artype_etter.xlsx")
    print("Ferdig med resultater etter")
    
#%% Gjerdrum laste inn fra excel

if fra_excel:
    gjerdrum_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score.xlsx")
    gjerdrum_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score_artype_for.xlsx", None)
    gjerdrum_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score_artype_etter.xlsx", None)
    
#%% Gjerdrum plotting

ev.artype_barplot(gjerdrum_results_for, gjerdrum_results, 60, "MCC", y=[-0.2, 0.4], title="Gjerdrum kommune før endringer")
ev.artype_barplot(gjerdrum_results_etter, gjerdrum_results, 60, "MCC", y=[-0.2, 0.4], title="Gjerdrum kommune etter endringer")

#%% Samlet

# Laster inn dataframes og tresatt myr
nes_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_pred_ar5_endring.csv", low_memory=False)
nes_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_ruter_med_tresatt_myr.csv")
nordaurdal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_pred_ar5_endring.csv", low_memory=False)
nordaurdal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_ruter_med_tresatt_myr.csv")
ullensaker_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_pred_ar5_endring.csv", low_memory=False)
ullensaker_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_ruter_med_tresatt_myr.csv")
etnedal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_pred_ar5_endring.csv", low_memory=False)
etnedal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_ruter_med_tresatt_myr.csv")
gjerdrum_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_pred_ar5_endring.csv", low_memory=False)
gjerdrum_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_ruter_med_tresatt_myr.csv")
dfs = [nes_df, nordaurdal_df, ullensaker_df, etnedal_df, gjerdrum_df]
tmyrs = [nes_tmyr, nordaurdal_tmyr, ullensaker_tmyr, etnedal_tmyr, gjerdrum_tmyr]
kommuner = ["Nes", "Nord-Aurdal", "Ullensaker", "Etnedal", "Gjerdrum"]

# Prediksjoner
preds_stack = []
for df, tmyr in zip(dfs, tmyrs):
    preds = ev.prediksjoner(df, 50, 100)
    preds = ev.fjern_tmyr(preds, tmyr['Id'])
    preds_stack.append(preds)

samlet_preds = pd.concat(preds_stack, ignore_index=True)

samlet_results = ev.scores_df(samlet_preds, "many")
samlet_results.to_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score.xlsx")


#%% Samlet artype før



#%% Samlet artype etter

# Hjelpefunksjon for artyper
def f(row):
        if np.isnan(row['ARTYPE_NY']):
            a = row['ARTYPE']
        else:
            a = row['ARTYPE_NY']
        return a 

# Artype subsets samlet
subsets_etter = {11: None, 12: None, 21: None, 22: None, 23: None, 30: None, 50: None, 60: None, 70: None, 80: None, 81: None, 82: None, 99: None}
for i, df in enumerate(dfs):
    # Definerer ARTYPE_ETTER
    df['ARTYPE_ETTER'] = df.apply(f, axis=1)
    # Larger artypene som finnes i kommunen
    uniques = df['ARTYPE_ETTER'].unique()
    for artype_etter in uniques:
        print(f"Begynner på artype {artype_etter}, kommune nr. {i}")
        if not np.isnan(artype_etter):
            # Subset med artype
            df_subset = df[df['ARTYPE_ETTER']==artype_etter]
            
            # Fjerner polygoner fra ruter med tresatt myr
            df_subset = ev.fjern_tmyr(df_subset, tmyrs[i]['Id'])
            
            # Lager kommune-id
            df_subset['Kommune'] = [kommuner[i] for _ in range(df_subset.shape[0])]
            df_subset['KommuneID'] = [kommuner[i] + str(rute_id) for rute_id in df_subset["Id"]]
            
            # Legger til rader i samlet dataframe for artypen
            if subsets_etter[artype_etter] is None:
                subsets_etter[artype_etter] = df_subset
            else:
                subsets_etter[artype_etter] = pd.concat([subsets_etter[artype_etter], df_subset], ignore_index=True)
            print(f"Lagt til subset i samlet dataframe for artype {artype_etter}, kommune nr. {i}")


samlet_results_etter = {}
with pd.ExcelWriter(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score_artype_etter.xlsx") as writer:     
    for artype, subset in subsets_etter.items():
        if subset is not None:
            print(f"Beregner metrics for artype {artype} (samlet).")
            # Lager prediksjoner
            preds = ev.prediksjoner(subset, 50, 100, id_column="KommuneID")
            # Beregner metrics
            results = ev.scores_df(preds, "many")
            # Lagrer excel-fil
            results.to_excel(writer, str(int(artype)))
            # Lagrer resultater for artypen i dictionary
            samlet_results_etter[str(artype)] = results



#%% Samlet plotting

ev.artype_barplot(samlet_results_etter, samlet_results, 50, "MCC", y=[-0.3, 0.3], title="Alle kommuner samlet etter endringer")

