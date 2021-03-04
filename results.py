# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:24:51 2021

@author: nicol
"""

import pandas as pd
import evaluate as ev


#%% Nes

# Laster inn csv-filer
nes_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_pred_ar5_endring.csv", low_memory=False)
nes_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_ruter_med_tresatt_myr.csv")

nes_results = ev.evaluate_predictions(nes_df, 100, nes_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score.xlsx")
nes_results_for = ev.evaluate_artype_for(nes_df, nes_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_for.xlsx")
nes_results_etter = ev.evaluate_artype_etter(nes_df, nes_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3034_Nes_2010_nobyg_4cities_300epochs\resultater\nes_score_artype_etter.xlsx")


#%% Nes plotting
ev.artype_barplot(nes_results_for, 30, "MCC")
ev.artype_barplot(nes_results_etter, 30, "MCC")

#%% Nord-Aurdal

# Laster inn csv-filer
nordaurdal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_pred_ar5_endring.csv", low_memory=False)
nordaurdal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_ruter_med_tresatt_myr.csv")

nordaurdal_results = ev.evaluate_predictions(nordaurdal_df, 100, nordaurdal_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score.xlsx")
print("Ferdig med resultater totalt")
nordaurdal_results_for = ev.evaluate_artype_for(nordaurdal_df, nordaurdal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_for.xlsx")
print("Ferdig med resultater før")
nordaurdal_results_etter = ev.evaluate_artype_etter(nordaurdal_df, nordaurdal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3451_Nord_Aurdal_2010_nobyg_4cities_300epochs\resultater\nordaurdal_score_artype_etter.xlsx")
print("Ferdig med totale resultater etter")

#%% Nord-Aurdal plotting
ev.artype_barplot(nordaurdal_results_for, 50, "MCC")
ev.artype_barplot(nordaurdal_results_etter, 50, "MCC")


#%% Ullensaker

# Laster inn csv-filer
ullensaker_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_pred_ar5_endring.csv", low_memory=False)
ullensaker_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_ruter_med_tresatt_myr.csv")

ullensaker_results = ev.evaluate_predictions(ullensaker_df, 100, ullensaker_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score.xlsx")
print("Ferdig med resultater totalt")
ullensaker_results_for = ev.evaluate_artype_for(ullensaker_df, ullensaker_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_for.xlsx")
print("Ferdig med resultater før")
ullensaker_results_etter = ev.evaluate_artype_etter(ullensaker_df, ullensaker_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3033_Ullensaker_2010_nobyg_4cities_300epochs\resultater\ullensaker_score_artype_etter.xlsx")
print("Ferdig med resultater etter")

#%%  Ullensaker plotting
ev.artype_barplot(ullensaker_results_for, 60, "MCC")
ev.artype_barplot(ullensaker_results_etter, 60, "MCC")

#%% Etnedal

# Laster inn csv-filer
etnedal_df = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_pred_ar5_endring.csv", low_memory=False)
etnedal_tmyr = pd.read_csv(r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\Resultater\etnedal_ruter_med_tresatt_myr.csv")

etnedal_results = ev.evaluate_predictions(etnedal_df, 100, etnedal_tmyr['Id'], None, metrics="many", path=r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score.xlsx")
print("Ferdig med resultater totalt")
etnedal_results_for = ev.evaluate_artype_for(etnedal_df, etnedal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score_artype_for.xlsx")
print("Ferdig med resultater før")
etnedal_results_etter = ev.evaluate_artype_etter(etnedal_df, etnedal_tmyr['Id'], r"C:\Users\nicol\Documents\Masteroppgave\Februarprediksjoner\3450_Etnedal_2010_nobyg_4cities_300epochs\resultater\etnedal_score_artype_etter.xlsx")
print("Ferdig med resultater etter")


#%% Etnedal plotting

ev.artype_barplot(etnedal_results_for, etnedal_results.at[50, "MCC"], 50, "MCC")
ev.artype_barplot(etnedal_results_etter, etnedal_results.at[50, "MCC"], 50, "MCC")


