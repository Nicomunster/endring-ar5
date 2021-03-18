# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:21:10 2021

@author: nicol
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, balanced_accuracy_score, confusion_matrix, matthews_corrcoef, roc_curve, roc_auc_score, auc


def prediksjoner(df, area_threshold, n_thresholds, id_column='Id'):
    """Grupperer arealer i samme rute og beregner prediksjoner for hver gridcode-verdi."""
    # Fjerner ugyldige verdier
    df = df[df['gridcode']!=-1.0]
    # Velger kolonner
    df['endring'] = df['endring'].fillna(0)
    df = df[[id_column, "gridcode", "endring", "areal_bit"]]

    # Grupperer etter Id og endring/ikke endring
    g = df.groupby([id_column, "gridcode", "endring"], as_index=False).sum()
    # Fjerner de med areal mindre enn 10 % av ruta
    g = g[g['areal_bit']>=area_threshold]
    # Setter endring til hele ruta hvis det fortsatt finnes endring
    grouped = g.groupby([id_column, "gridcode"], as_index=False).sum()
    
    for i in range(n_thresholds+1):
        grouped["thr" + str(i)] = grouped["gridcode"] <= i
        
    return grouped


def fjern_tmyr(df, tmyr):
    """Fjerner alle ruter med tresatt myr. Input tmyr er en liste med Id til ruter med tresatt myr."""
    df = df[~df.isin(tmyr)]
    return df


def fjern_annet(df, skygge):
    """Fjerner alle ruter i input"""
    df = df[~df.isin(skygge)]
    return df


def scores_df(df, metrics):
    """Beregner mål på klassifikasjonsnøyaktighet"""
    if metrics == 'all':
        metrics = ["Positive", "Negative", "Pred. Positive", "Pred. Negative", "TP", "TN", "FP", "FN", "TPR (Recall)", "TNR", "FPR", "FNR", "PPV (Precision)", "NPV", "Accuracy", "Balanced Accuracy", "F1"]
    elif metrics == 'many':
        metrics = ["Positive", "Negative", "Pred. Positive", "Pred. Negative", "TP", "TN", "FP", "FN", "TPR (Recall)", "TNR", "PPV (Precision)", "NPV", "Accuracy", "Balanced Accuracy", "F1", "MCC"]
    results = {}
    results["threshold"] = list(range(101))
    for metric in metrics:
        results[metric] = []
    
    for thr in results["threshold"]:
        if "PPV (Precision)" in metrics:
            pre = precision_score(df['endring'], df["thr" + str(thr)])
            results["PPV (Precision)"].append(pre)
        if "TPR (Recall)" in metrics:
            TPR = recall_score(df['endring'], df["thr" + str(thr)])
            results["TPR (Recall)"].append(TPR)
        if "F1" in metrics:
            f1 = f1_score(df['endring'], df["thr" + str(thr)])
            results["F1"].append(f1)
        if "Accuracy" in metrics:
            acc = accuracy_score(df['endring'], df["thr" + str(thr)])
            results["Accuracy"].append(acc)
        if "Balanced Accuracy" in metrics:
            bal_acc = balanced_accuracy_score(df['endring'], df["thr" + str(thr)])
            results["Balanced Accuracy"].append(bal_acc)
        if "MCC" in metrics:
            mcc = matthews_corrcoef(df['endring'], df["thr" + str(thr)])
            results["MCC"].append(mcc)
        
        TN, FP, FN, TP = confusion_matrix(df['endring'], df["thr" + str(thr)], labels=[0, 1]).ravel()/df.shape[0]
        if "TP" in metrics:
            results["TP"].append(TP)
        if "TN" in metrics:
            results["TN"].append(TN)
        if "FP" in metrics:
            results["FP"].append(FP)
        if "FN" in metrics:
            results["FN"].append(FN)
        if "TNR" in metrics:
            results["TNR"].append(TN/(TN+FP))
        if "FPR" in metrics:
            results["FPR"].append(FP/(FP+TN))
        if "FNR" in metrics:
            results["FNR"].append(FN/(FN+TP))
        if "NPV" in metrics:
            results["NPV"].append(TN/(TN+FN))
        if "Positive" in metrics:
            results["Positive"].append(TP+FN)
        if "Negative" in metrics:
            results["Negative"].append(TN+FP)
        if "Pred. Positive" in metrics:
            results["Pred. Positive"].append(TP+FP)
        if "Pred. Negative" in metrics:
            results["Pred. Negative"].append(TN+FN)

    score_df = pd.DataFrame(results)    
    return score_df


def roc(y_true, y_prob):
    """Plotter Receiver Operating CHaracteristic (ROC) Kurven, og returnerer ROC AUC."""
    # Beregner FPR og TPR 
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    ns_probs = [0 for _ in range(len(y_true))]
    nfpr, ntpr, _ = roc_curve(y_true, ns_probs)

    # Beregner arealet under kurven
    roc_auc = roc_auc_score(y_true, y_prob)
    
    # Plotter kurven
    plt.plot(fpr, tpr, label=f'Modell, auc={round(auc, 2)}')
    plt.plot(nfpr, ntpr, label='No skill')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate (Recall)')
    plt.legend()
    plt.show()
    
    return roc_auc


def prc(precision, recall):
    """Plotter Precision-Recall kurven og returnerer AUC."""
    # Beregner AUC
    prc_auc = auc(recall, precision)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(recall, precision, label='Modell, auc = ')
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Precision-Recall Curve')
    fig.legend()
    plt.show()
    
    return prc_auc


def save_xls(list_dfs, xls_path, area_thr_str):
    with pd.ExcelWriter(xls_path) as writer:
        for n, df in enumerate(list_dfs):
            df.to_excel(writer, area_thr_str[n])
        writer.save()
        

def evaluate_predictions(df, tmyr, skygge, metrics="many", path=None, gridcodes=100, area_thr=50):
    """Beregner nøyaktighetsmål basert på dataframe.
    Inputs:
        df: dataframe med ruter, inkludert endring og gridcode.
        gridcodes: int, antall sannsynlighetskategorier.
        tmyr: Liste eller None. Listen er liste over Id til ruter med tresatt 
              myr. Her blir alle prediksjoner satt til negative. Hvis None, 
              blir ingenting gjort.
        metrics: Liste med metrics, eller "many", eller "all".
        path: Sti hvor excel-fila skal lagres. Hvis None, så lagres ikke excel-fil.
        area_thr: terskelverdi i m^2 for fjerning av små arealer.
    Output:
        Resultater i dataframe. Lagrer også til excel-fil.
    """
    # Formaterer prediksjoner
    preds = prediksjoner(df, area_thr, gridcodes)

    # Fjerner tresatt myr
    if tmyr is not None:
        preds = fjern_tmyr(preds, tmyr)

    # Fjerner skygge
    if skygge is not None:
        preds = fjern_skygge(preds, skygge)

    # Beregner nøyaktighetsmål
    results = scores_df(preds, metrics)

    # Lagrer til excel
    if path is not None:
        results.to_excel(path)
    
    return results


def evaluate_artype_for(df, tmyr, xls_path, area_thr=50, gridcodes=100, metrics='many'):
    """Beregner resultater delt på hvilken artype som var."""
    results_dict = {}
    with pd.ExcelWriter(xls_path) as writer:
        uniques = df['ARTYPE'].unique()
        for artype in uniques:
            if not np.isnan(artype):
                df_subset = df[df['ARTYPE']==artype]
                preds = prediksjoner(df_subset, area_thr, gridcodes)
                if tmyr is not None:
                    preds = fjern_tmyr(preds, tmyr)
                results = scores_df(preds, metrics)
                results.to_excel(writer, str(int(artype)))
                results_dict[str(artype)] = results
    return results_dict
            
            
def evaluate_artype_etter(df, tmyr, xls_path, area_thr=50, gridcodes=100, metrics='many', from_preds=False):
    """Beregner resultater delt på hvilken artype som er etter endringene."""
    results_dict = {}
    
    # Funksjon for å lage ny kolonne for artype etter endring
    def f(row):
        if np.isnan(row['ARTYPE_NY']):
            a = row['ARTYPE']
        else:
            a = row['ARTYPE_NY']
        return a 
    
    # Bruker funksjonen til å lage ny kolonne
    df['ARTYPE_ETTER'] = df.apply(f, axis=1)
    
    with pd.ExcelWriter(xls_path) as writer:
        uniques = df['ARTYPE_ETTER'].unique()
        for artype_etter in uniques:
            if not np.isnan(artype_etter):
                df_subset = df[df['ARTYPE_ETTER']==artype_etter]
                preds = prediksjoner(df_subset, area_thr, gridcodes)
                if tmyr is not None:
                    preds = fjern_tmyr(preds, tmyr)
                results = scores_df(preds, metrics)
                results.to_excel(writer, str(int(artype_etter)))
                results_dict[str(artype_etter)] = results
    return results_dict


def artype_barplot(results_dict, total_df, gridcode, metric, y=None, title=None):
    """Plotter resultater basert på artype."""
    # Dictionary som lagrer navn of farge til ARTYPE-kodene
    artype_props = {"11": {'Navn':'Bebygd', 'Farge': '#fcdbd9'},
                    "12": {'Navn':'Samferdsel', 'Farge': '#b3784c'},
                    "21": {'Navn':'Fulldyrka jord', 'Farge': '#ffd16e'},
                    "22": {'Navn':'Overflatedyrka jord', 'Farge': '#ffff4c'},
                    "23": {'Navn':'Innmarksbeite', 'Farge': '#ffffad'},
                    "30": {'Navn':'Skog', 'Farge': '#9ecc73'},
                    "50": {'Navn':'Åpen fastmark', 'Farge': '#d9d9d9'},
                    "60": {'Navn':'Myr', 'Farge': '#1d7a8d'},
                    "70": {'Navn':'Snøisbre', 'Farge': '#e6ffff'},
                    "80": {'Navn':'Vann', 'Farge': '#ccf5ff'},
                    "81": {'Navn':'Ferskvann', 'Farge': '#91e7ff'},
                    "82": {'Navn':'Hav', 'Farge': '#ccfefe'},
                    "100": {'Navn':'Totalt', 'Farge': '#000000'}}
    artyper = list(sorted(artype_props.keys()))
    

    scores = list()
    for i, artype in enumerate(artyper):
        if artype == "100":
            scores.append(total_df.at[gridcode, metric])
        elif artype not in results_dict.keys() and float(artype) not in results_dict.keys():
            scores.append(0)
        else:
            df = results_dict[artype]
            score = df.at[gridcode, metric]
            scores.append(score)
    
    # Navn og farge til artyper
    artyper_navn = [artype_props[a]['Navn'] for a in artyper]
    artyper_farger = [artype_props[a]['Farge'] for a in artyper]
    
    #Plotting
    plt.figure(figsize=(8,6))
    plt.xlabel("Arealtype")
    plt.ylabel(metric)
    if title is not None:
        plt.title(title)
    if y is not None:
        plt.ylim(y)
    else:
        if metric == "MCC":
            plt.ylim([-0.3, 0.5])
        elif metric == "F1":
            plt.ylim([0, 0.7])
    ax = sns.barplot(artyper_navn, scores, palette=artyper_farger)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    plt.tight_layout()
    plt.show()
        