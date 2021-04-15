# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:24:51 2021

@author: nicol
"""

import os
import numpy as np
import pandas as pd
import evaluate as ev

fra_excel = False

#%% Laste inn filer og beregne resultater

kommuner = ["Gjerdrum", "Ullensaker", "Nes", "Sør-Odal", "Eidskog", "Nord-Aurdal", "Etnedal", "Gjesdal", "Sola", "Randaberg"]
results = {kommune: {} for kommune in kommuner}
if not fra_excel:
    for kommune in kommuner:
        print("Laster inn:", kommune)
        results[kommune]["Data"] = pd.read_csv(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", kommune.lower()+"_pred_ar5_endring.csv"), low_memory=False)
        if kommune in ["Sola", "Randaberg"]:
            tmyr = pd.read_csv(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", kommune.lower()+"_ruter_med_tresatt_myr.csv"))["Id"].values.tolist()
            hav = pd.read_csv(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", kommune.lower()+"_ruter_med_hav.csv"))["Id"].values.tolist()
            results[kommune]["Tresatt myr"] = tmyr + hav
            print(len(set(results[kommune]["Tresatt myr"])))
        else:
            results[kommune]["Tresatt myr"] = pd.read_csv(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", kommune.lower()+"_ruter_med_tresatt_myr.csv"))
        print("Beregner resultater:", kommune)
        
        preds = ev.prediksjoner_artype(results[kommune]["Data"], 50, 100)
        
        results[kommune]["Resultater totalt"] = ev.scores_df(preds)

        results[kommune]["Resultater artype før"] = {}
        xls_path = os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", kommune.lower()+"_score_artype_for_1artype.xlsx")
        with pd.ExcelWriter(xls_path) as writer:
            for artype in preds["ARTYPE"].unique():
                subset = preds[preds["ARTYPE"]==artype]
                subset = ev.fjern_tmyr(subset, results[kommune]["Tresatt myr"]["Id"])
                subset_scores = ev.scores_df(subset)
                results[kommune]["Resultater artype før"][artype] = subset_scores
                subset_scores.to_excel(writer, str(int(artype)))

# Laste inn fra excel
for kommune in kommuner:
    results[kommune]["Resultater totalt"] = pd.read_excel(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", kommune.lower()+"_score_1artype.xlsx"))
    results[kommune]["Resultater artype før"] = pd.read_excel(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", kommune.lower()+"_score_artype_for_1artype.xlsx"), None)

# Samlet
#results["Samlet"] = {}
#results["Samlet"]["Resultater totalt"] = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score.xlsx")
#results["Samlet"]["Resultater artype før"] = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score_artype_for.xlsx", None)
#results["Samlet"]["Resultater artype etter"] = pd.read_excel(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\Samlet\Resultater\samlet_score_artype_etter.xlsx", None)

#%% Plotting

def plot_kommuner(kommuner, results_dict, tid, gridcode, metric, title=None):
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
        results = results_dict[kommune]["Resultater totalt"]
        results_for = results_dict[kommune]["Resultater artype før"]
        results_etter = results_dict[kommune]["Resultater artype etter"]
        if kommune!="Samlet":
            kommune = kommune + " kommune"
        if "Før" in tid:
            if title is None:
                plot_title = metric + " i " + kommune + " fordelt på arealtype"
            else:
                plot_title = title
            if kommune=="Samlet":
                plot_title = metric + " i alle kommuner fordelt på arealtype"
            ev.artype_barplot(results_for, results, gridcode, metric, title=plot_title)
        if "Etter" in tid:
            ev.artype_barplot(results_etter, results, gridcode, metric, title=kommune+" etter endringer")
        
kommuner = ["Gjerdrum", "Ullensaker", "Nes", "Sør-Odal", "Eidskog", "Nord-Aurdal", "Etnedal", "Gjesdal", "Sola", "Randaberg"]
plot_kommuner(kommuner, results, "Før", 50, "MCC")
