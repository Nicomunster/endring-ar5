# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:24:51 2021

@author: nicol
"""

import os
import pandas as pd
import evaluate as ev

fra_excel = True

#%% Laste inn filer og beregne resultater

kommuner = ["Gjerdrum", "Ullensaker", "Nes", "Sør-Odal", "Eidskog", "Nord-Aurdal", "Etnedal", 
            "Gjesdal", "Sola", "Randaberg", "Samlet"]
results = {kommune: {} for kommune in kommuner}
if not fra_excel:
    for kommune in kommuner:
        # Laste inn prediksjonsdata
        print("Laster inn:", kommune)
        if kommune == "Samlet":
            results[kommune]["Data"] = results[kommuner[0]]["Data"]
            for concat_kommune in kommuner[1:-1]:
                results[kommune]["Data"] = pd.concat([results[kommune]["Data"], results[concat_kommune]["Data"]], 
                                                     ignore_index=True)
        else:
            results[kommune]["Data"] = pd.read_csv(os.path.join(
                r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune,
                "Resultater", kommune.lower()+"_pred_ar5_endring.csv"), low_memory=False)
            results[kommune]["Data"]["komm_Id"] = kommune + "_" + results[kommune]["Data"]["Id"].astype(str)
        
        # Laste inn tresatt myr data
        if kommune in ["Sola", "Randaberg"]:
            tmyr = pd.read_csv(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, 
                                            "Resultater", 
                                            kommune.lower()+"_ruter_med_tresatt_myr.csv"))["Id"].values.tolist()
            hav = pd.read_csv(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, 
                                           "Resultater", kommune.lower()+"_ruter_med_hav.csv"))["Id"].values.tolist()
            results[kommune]["Tresatt myr"] = tmyr + hav
        elif kommune == "Samlet":
            results[kommune]["Tresatt myr"] = []
            for tmyr_kommune in kommuner:
                results[kommune]["Tresatt myr"].append(results[tmyr_kommune]["Tresatt myr"])
        else:
            results[kommune]["Tresatt myr"] = pd.read_csv(os.path.join(
                                                    r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", 
                                                    kommune, "Resultater", kommune.lower()+
                                                    "_ruter_med_tresatt_myr.csv"))["Id"].values.tolist()
        
        print("Gjør klar prediksjoner:", kommune)
        # Beregne prediksjoner
        preds = ev.prediksjoner_artype(results[kommune]["Data"], 50, 100, id_column="komm_Id", komm=kommune)
        # preds = ev.fjern_tmyr(preds, results[kommune]["Tresatt myr"])
        
        print("Fjerner unødvendige arealtyper:", kommune)
        preds = preds[~preds["ARTYPE"].isin([12., 70., 80., 81., 82., 99.])]
        
        if kommune=="Samlet":
            preds.to_csv(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", 
                         kommune.lower()+"_preds.csv"))
        else:
            preds.to_excel(os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", 
                         kommune.lower()+"_preds.xlsx"))
        
        # Resultater totalt
        print("Beregner metrics totalt:", kommune)
        results[kommune]["Resultater totalt"] = ev.scores_df(preds, 
                                                             metrics=["Positive", "Negative", "Pred. Positive", 
                                                                      "Pred. Negative", "TP", "TN", "FP", "FN", 
                                                                      "Precision", "Recall", "Accuracy", "F1", "MCC"])
        results[kommune]["Resultater totalt"].to_excel(
            os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", 
                         kommune.lower()+"_score_1artype.xlsx"))
        
        # resultater arealtype før
        results[kommune]["Resultater artype før"] = {}
        xls_path = os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", kommune, "Resultater", 
                                kommune.lower()+"_score_artype_for_1artype.xlsx")
        with pd.ExcelWriter(xls_path) as writer:
            for artype in preds["ARTYPE"].unique():
                print("Beregner metrics for arealtype", artype)
                subset = preds[preds["ARTYPE"]==artype]
                subset_scores = ev.scores_df(subset, metrics=["Positive", "Negative", "Pred. Positive", 
                                                              "Pred. Negative", "TP", "TN", "FP", "FN", 
                                                              "Precision", "Recall", "Accuracy", "F1", "MCC"])
                results[kommune]["Resultater artype før"][artype] = subset_scores
                subset_scores.to_excel(writer, str(int(artype)))
        print("------------------------------------")

# Laste inn fra excel
for kommune in kommuner:
    results[kommune]["Resultater totalt"] = pd.read_excel(
        os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", 
                     kommune, "Resultater", kommune.lower()+"_score_1artype.xlsx"))
    results[kommune]["Resultater artype før"] = pd.read_excel(
        os.path.join(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner", 
                     kommune, "Resultater", kommune.lower()+"_score_artype_for_1artype.xlsx"), None)


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
        #results_etter = results_dict[kommune]["Resultater artype etter"]
        if kommune!="Samlet":
            kommune = kommune + " kommune"
        if "Før" in tid:
            if title is None:
                plot_title = metric + " i " + kommune + " fordelt på arealtype"
            else:
                plot_title = title
            if kommune=="Samlet":
                plot_title = metric + " i alle kommuner fordelt på arealtype"
            ev.kommune_barplot(results_for, results, gridcode, metric, title=plot_title)
        if "Etter" in tid:
            ev.kommune_barplot(results_etter, results, gridcode, metric, title=kommune+" etter endringer")

def plot_artyper(kommuner, results_dict, gridcode, metric, title=None):
    """Et søyeldiagram for hevr arealtype, som viser forskjellige kommuner.
    """
    
    artype_props = {"11": {'Navn':'Bebygd', 'Farge': '#fcdbd9'},
#                    "12": {'Navn':'Samferdsel', 'Farge': '#b3784c'},
                    "21": {'Navn':'Fulldyrka jord', 'Farge': '#ffd16e'},
                    "22": {'Navn':'Overflatedyrka jord', 'Farge': '#ffff4c'},
                    "23": {'Navn':'Innmarksbeite', 'Farge': '#ffffad'},
                    "30": {'Navn':'Skog', 'Farge': '#9ecc73'},
                    "50": {'Navn':'Åpen fastmark', 'Farge': '#d9d9d9'},
                    "60": {'Navn':'Myr', 'Farge': '#d1d1ff'},
#                    "70": {'Navn':'Snøisbre', 'Farge': '#e6ffff'},
#                    "80": {'Navn':'Vann', 'Farge': '#ccf5ff'},
#                    "81": {'Navn':'Ferskvann', 'Farge': '#91e7ff'},
#                    "82": {'Navn':'Hav', 'Farge': '#ccfefe'},
                    "100": {'Navn':'Totalt', 'Farge': '#000000'}
                    }
    artyper = list(sorted(artype_props.keys()))
    artype_dict = {}
    
    # Organiserer arealtypenes resultater i en dictionary
    for artype in artyper:
        artype_dict[artype] = {kommune: None for kommune in kommuner}
    for kommune, kdict in results_dict.items():
        for artype in artyper:
            if artype == "100":
                artype_dict[artype][kommune] = kdict["Resultater totalt"]
            elif artype in kdict["Resultater artype før"].keys():
                artype_dict[artype][kommune] = kdict["Resultater artype før"][artype]
        
    # Sender til plottingsfunksjon for hver arealtype
    for artype, artype_dict in artype_dict.items():
        if artype == "100":
            plot_title = metric + " for alle arealtyper fordelt på kommuner"
        else:
            plot_title = metric + " for " + artype_props[artype]["Navn"].lower() + " fordelt på kommuner"
        ev.artype_barplot(artype, artype_dict, gridcode, metric, title=plot_title)

kommuner = ["Gjerdrum", "Ullensaker", "Nes", "Sør-Odal", "Eidskog", "Nord-Aurdal", "Etnedal", 
            "Gjesdal", "Sola", "Randaberg", "Samlet"]
plot_kommuner(kommuner, results, "Før", 50, "MCC")

