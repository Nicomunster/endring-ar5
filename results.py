# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:24:51 2021

@author: nicol
"""

import numpy as np
import pandas as pd
import evaluate as ev

fra_excel = False
#%% Laste inn filer
if not fra_excel:
    print("Nes")
    nes_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_pred_ar5_endring.csv", low_memory=False)
    nes_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_ruter_med_tresatt_myr.csv")    
    nes_results = ev.evaluate_predictions(nes_df, 100, nes_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score.xlsx")
    nes_results_for = ev.evaluate_artype_for(nes_df, nes_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_for.xlsx")
    nes_results_etter = ev.evaluate_artype_etter(nes_df, nes_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_etter.xlsx")
    print("Nord-Aurdal")
    nordaurdal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_pred_ar5_endring.csv", low_memory=False)
    nordaurdal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_ruter_med_tresatt_myr.csv")
    nordaurdal_results = ev.evaluate_predictions(nordaurdal_df, 100, nordaurdal_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score.xlsx")
    nordaurdal_results_for = ev.evaluate_artype_for(nordaurdal_df, nordaurdal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_for.xlsx")
    nordaurdal_results_etter = ev.evaluate_artype_etter(nordaurdal_df, nordaurdal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_etter.xlsx")
    ullensaker_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_pred_ar5_endring.csv", low_memory=False)
    ullensaker_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_ruter_med_tresatt_myr.csv")
    print("Ullensaker")
    ullensaker_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_pred_ar5_endring.csv", low_memory=False)
    ullensaker_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_ruter_med_tresatt_myr.csv")
    ullensaker_results = ev.evaluate_predictions(ullensaker_df, 100, ullensaker_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score.xlsx")
    ullensaker_results_for = ev.evaluate_artype_for(ullensaker_df, ullensaker_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_for.xlsx")
    ullensaker_results_etter = ev.evaluate_artype_etter(ullensaker_df, ullensaker_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_etter.xlsx")
    print("Etnedal")
    etnedal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_pred_ar5_endring.csv", low_memory=False)
    etnedal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_ruter_med_tresatt_myr.csv")    
    etnedal_results = ev.evaluate_predictions(etnedal_df, 100, etnedal_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score.xlsx")
    etnedal_results_for = ev.evaluate_artype_for(etnedal_df, etnedal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score_artype_for.xlsx")
    etnedal_results_etter = ev.evaluate_artype_etter(etnedal_df, etnedal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score_artype_etter.xlsx")
    print("Gjerdrum")
    gjerdrum_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_pred_ar5_endring.csv", low_memory=False)
    gjerdrum_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_ruter_med_tresatt_myr.csv")
    gjerdrum_results = ev.evaluate_predictions(gjerdrum_df, 100, gjerdrum_tmyr['Id'], None, metrics="many", path = r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score.xlsx")
    gjerdrum_results_for = ev.evaluate_artype_for(gjerdrum_df, gjerdrum_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score_artype_for.xlsx")
    gjerdrum_results_etter = ev.evaluate_artype_etter(gjerdrum_df, gjerdrum_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score_artype_etter.xlsx")
    print("Sør-Odal")
    sorodal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3415_Sør-Odal_2010_nobyg_4cities_300epochs\Resultater\sorodal_pred_ar5_endring.csv", low_memory=False)
    sorodal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3415_Sør-Odal_2010_nobyg_4cities_300epochs\Resultater\sorodal_ruter_med_tresatt_myr.csv")
    sorodal_results = ev.evaluate_predictions(sorodal_df, 100, sorodal_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3415_Sør-Odal_2010_nobyg_4cities_300epochs\Resultater\sorodal_score.xlsx")
    sorodal_results_for = ev.evaluate_artype_for(sorodal_df, sorodal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3415_Sør-Odal_2010_nobyg_4cities_300epochs\Resultater\sorodal_score_artype_for.xlsx")
    sorodal_results_etter = ev.evaluate_artype_etter(sorodal_df, sorodal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3415_Sør-Odal_2010_nobyg_4cities_300epochs\Resultater\sorodal_score_artype_etter.xlsx")
    print("Eidskog")
    eidskog_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3416_Eidskog_2010_nobyg_4cities_300epochs\Resultater\eidskog_pred_ar5_endring.csv", low_memory=False)
    eidskog_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3416_Eidskog_2010_nobyg_4cities_300epochs\Resultater\eidskog_ruter_med_tresatt_myr.csv")
    eidskog_results = ev.evaluate_predictions(eidskog_df, 100, eidskog_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3416_Eidskog_2010_nobyg_4cities_300epochs\Resultater\eidskog_score.xlsx")
    eidskog_results_for = ev.evaluate_artype_for(eidskog_df, eidskog_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3416_Eidskog_2010_nobyg_4cities_300epochs\Resultater\eidskog_score_artype_for.xlsx")
    eidskog_results_etter = ev.evaluate_artype_etter(eidskog_df, eidskog_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3416_Eidskog_2010_nobyg_4cities_300epochs\Resultater\eidskog_score_artype_etter.xlsx")
    print("Samlet")
    # Laster inn dataframes og tresatt myr
    dfs = [nes_df, nordaurdal_df, ullensaker_df, etnedal_df, gjerdrum_df, sorodal_df, eidskog_df]
    tmyrs = [nes_tmyr, nordaurdal_tmyr, ullensaker_tmyr, etnedal_tmyr, gjerdrum_tmyr, sorodal_tmyr, eidskog_tmyr]
    kommuner = ["Nes", "Nord-Aurdal", "Ullensaker", "Etnedal", "Gjerdrum", "Sør-Odal", "Eidskog"]
    
    # Prediksjoner
    preds_stack = []
    for df, tmyr in zip(dfs, tmyrs):
        preds = ev.prediksjoner(df, 50, 100)
        preds = ev.fjern_tmyr(preds, tmyr['Id'])
        preds_stack.append(preds)
    
    samlet_preds = pd.concat(preds_stack, ignore_index=True)
    
    samlet_results = ev.scores_df(samlet_preds, "many")
    samlet_results.to_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score.xlsx")
    
    
    # Samlet artype før
    subsets_for = {11: None, 12: None, 21: None, 22: None, 23: None, 30: None, 50: None, 60: None, 70: None, 80: None, 81: None, 82: None, 99: None}
    for i, df in enumerate(dfs):
        uniques = df['ARTYPE'].unique()
        for artype_for in uniques:
            print(f"Begynner på artype {artype_for}, kommune nr. {i}, før endringer.")
            if not np.isnan(artype_for):
                # Subset med artype
                df_subset = df[df['ARTYPE']==artype_for]
                
                # Fjerner polygoner fra ruter med tresatt myr
                df_subset = ev.fjern_tmyr(df_subset, tmyrs[i]['Id'])
                
                # Lager kommune-id
                df_subset['Kommune'] = [kommuner[i] for _ in range(df_subset.shape[0])]
                df_subset['KommuneID'] = [kommuner[i] + str(rute_id) for rute_id in df_subset["Id"]]
                
                # Legger til rader i samlet dataframe for artypen
                if subsets_for[artype_for] is None:
                    subsets_for[artype_for] = df_subset
                else:
                    subsets_for[artype_for] = pd.concat([subsets_for[artype_for], df_subset], ignore_index=True)
                print(f"Lagt til subset i samlet dataframe for artype {artype_for}, kommune nr. {i}, før endringer.")
            
    samlet_results_for = {}
    with pd.ExcelWriter(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score_artype_for.xlsx") as writer:     
        for artype, subset in subsets_for.items():
            if subset is not None:
                print(f"Beregner metrics for artype {artype} (samlet), før endringer.")
                # Lager prediksjoner
                preds = ev.prediksjoner(subset, 50, 100, id_column="KommuneID")
                # Beregner metrics
                results = ev.scores_df(preds, "many")
                # Lagrer excel-fil
                results.to_excel(writer, str(int(artype)))
                # Lagrer resultater for artypen i dictionary
                samlet_results_for[str(artype)] = results
    
    # Samlet artype etter
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
            print(f"Begynner på artype {artype_etter}, kommune nr. {i}, etter endringer.")
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
                print(f"Lagt til subset i samlet dataframe for artype {artype_etter}, kommune nr. {i}, etter endringer.")
    
    
    samlet_results_etter = {}
    with pd.ExcelWriter(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score_artype_etter.xlsx") as writer:     
        for artype, subset in subsets_etter.items():
            if subset is not None:
                print(f"Beregner metrics for artype {artype} (samlet), etter endringer.")
                # Lager prediksjoner
                preds = ev.prediksjoner(subset, 50, 100, id_column="KommuneID")
                # Beregner metrics
                results = ev.scores_df(preds, "many")
                # Lagrer excel-fil
                results.to_excel(writer, str(int(artype)))
                # Lagrer resultater for artypen i dictionary
                samlet_results_etter[str(artype)] = results


if fra_excel:
    # Nes
    nes_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score.xlsx")
    nes_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_for.xlsx", None)
    nes_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_etter.xlsx", None)
    # Nord-Aurdal
    nordaurdal_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score.xlsx")
    nordaurdal_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_for.xlsx", None)
    nordaurdal_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_etter.xlsx", None)
    # Ullensaker
    ullensaker_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score.xlsx")
    ullensaker_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_for.xlsx", None)
    ullensaker_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_etter.xlsx", None)
    # Etnedal
    etnedal_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_score.xlsx")
    etnedal_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_score_artype_for.xlsx", None)
    etnedal_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_score_artype_etter.xlsx", None)
    # Gjerdrum
    gjerdrum_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score.xlsx")
    gjerdrum_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score_artype_for.xlsx", None)
    gjerdrum_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3032_Gjerdrum_2010_nobyg_4cities_300epochs\Resultater\gjerdrum_score_artype_etter.xlsx", None)
    # Sør-Odal
    sorodal_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3415_Sør-Odal_2010_nobyg_4cities_300epochs\Resultater\sorodal_score.xlsx")
    sorodal_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3415_Sør-Odal_2010_nobyg_4cities_300epochs\Resultater\sorodal_score_artype_for.xlsx", None)
    sorodal_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3415_Sør-Odal_2010_nobyg_4cities_300epochs\Resultater\sorodal_score_artype_etter.xlsx", None)
    # Eidskog
    eidskog_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3416_Eidskog_2010_nobyg_4cities_300epochs\Resultater\eidskog_score.xlsx")
    eidskog_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3416_Eidskog_2010_nobyg_4cities_300epochs\Resultater\eidskog_score_artype_for.xlsx", None)
    eidskog_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3416_Eidskog_2010_nobyg_4cities_300epochs\Resultater\eidskog_score_artype_etter.xlsx", None)
    # Samlet
    samlet_results = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score.xlsx")
    samlet_results_for = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score_artype_for.xlsx", None)
    samlet_results_etter = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score_artype_etter.xlsx", None)
    
results_dict = {"Nes": {"Resultater": nes_results, "Etter": nes_results_etter, "Før": nes_results_for},
                "Nord-Aurdal": {"Resultater": nordaurdal_results, "Etter": nordaurdal_results_etter, "Før": nordaurdal_results_for},
                "Ullensaker": {"Resultater": ullensaker_results, "Etter": ullensaker_results_etter, "Før": ullensaker_results_for},
                "Etnedal": {"Resultater": etnedal_results, "Etter": etnedal_results_etter, "Før": etnedal_results_for},
                "Gjerdrum": {"Resultater": gjerdrum_results, "Etter": gjerdrum_results_etter, "Før": gjerdrum_results_for},
                "Sør-Odal": {"Resultater": sorodal_results, "Etter": sorodal_results_etter, "Før": sorodal_results_for},
                "Eidskog": {"Resultater": eidskog_results, "Etter": eidskog_results_etter, "Før": eidskog_results_for},
                "Samlet": {"Resultater": samlet_results, "Etter": samlet_results_etter, "Før": samlet_results_for}}

#%% Plotting

def plot_kommuner(kommuner, tid, gridcode, metric):
    """
    Plott artyper for flere kommuner.
    Inputs:
        kommuner: liste med kommunenavn.
        tid: enten "Før", "Etter", eller ["Før", "Etter"].
        gridcode: terskelverdi for prediksjoner.
        metric: nøyaktighetsmål til bruk for plotting, f. eks. "MCC" eller "F1".
    """
    if isinstance(tid, str):
        tid = [tid]
    for kommune in kommuner:
        results = results_dict[kommune]["Resultater"]
        results_for = results_dict[kommune]["Før"]
        results_etter = results_dict[kommune]["Etter"]
        if kommune!="Samlet":
            kommune = kommune + " kommune"
        if "Før" in tid:
            ev.artype_barplot(results_for, results, gridcode, metric, title=kommune+" før endringer")
        if "Etter" in tid:
            ev.artype_barplot(results_etter, results, gridcode, metric, title=kommune+" etter endringer")
        
kommuner = ["Nes", "Nord-Aurdal", "Ullensaker", "Etnedal", "Gjerdrum", "Sør-Odal", "Eidskog", "Samlet"]
#kommuner = ["Nes", "Ullensaker", "Gjerdrum"]
plot_kommuner(kommuner, "Før", 50, "MCC")