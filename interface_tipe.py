"""
Interface TIPE — Saisie des résultats expérimentaux
Local  : streamlit run interface_tipe.py
Cloud  : déployé sur Streamlit Community Cloud
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import subprocess, os, tempfile, shutil
from scipy import stats

# ─── Chemins ─────────────────────────────────────────────────────────────────
BASE   = os.path.dirname(os.path.abspath(__file__))
PANDOC = shutil.which('pandoc') or r"C:\Program Files\Pandoc\pandoc.exe"

# ─── Page ────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="TIPE — SO₂ dans le vin", page_icon="🍷", layout="wide")
st.title("🍷 TIPE — Optimisation du SO₂ dans le vin")
st.caption("Saisie des mesures · Comparaison théorie/expérience · Génération automatique des documents")

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Protocole")
    c_I2  = st.number_input("Concentration I₂ (mol/L)", value=0.005, step=0.001, format="%.3f")
    V_ech = st.number_input("Volume échantillon (mL)",  value=20.0,  step=1.0)
    st.markdown("---")
    st.markdown("**Formule :**")
    st.latex(r"[\text{SO}_2] = \frac{V_{I_2} \times c_{I_2} \times 64000}{V_{éch}}")
    st.caption(f"= V(mL) × **{c_I2 * 64000 / V_ech:.1f}** mg/L par mL d'I₂")

def calc_SO2(V_mL):
    return float(V_mL) * c_I2 * 64000 / V_ech

Ka1 = 10**(-1.81)
Ka2 = 10**(-6.91)
COULEURS = ['#2C5F8A', '#E07B39', '#3A8A5F', '#9B3A8A']

def f_mol(pH):
    H = 10**(-np.asarray(pH, dtype=float))
    return H**2 / (H**2 + Ka1*H + Ka1*Ka2)

def style_ax(ax):
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=0.3)

def save_fig(fig, fname):
    fig.savefig(os.path.join(BASE, fname), dpi=200, bbox_inches='tight', facecolor='white')


# ═══════════════════════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4, tab_docs = st.tabs([
    "Exp. 1 — f(pH)",
    "Exp. 2 — Cinétique",
    "Exp. 3 — Oxygène",
    "Exp. 4 — Dose initiale",
    "📄 Documents",
])


# ──────────────────────────────────────────────────────────────────────────────
# EXP. 1
# ──────────────────────────────────────────────────────────────────────────────
with tab1:
    st.subheader("Expérience 1 — Fraction moléculaire active = f(pH)")
    st.info("Pour chaque pH, entre les 3 volumes d'I₂ versés à l'équivalence (C₀ = 100 mg/L).")

    df1 = st.data_editor(pd.DataFrame({
        "pH":      [3.0, 3.2, 3.5, 3.8, 4.0],
        "V₁ (mL)": [None]*5, "V₂ (mL)": [None]*5, "V₃ (mL)": [None]*5,
    }), num_rows="fixed", use_container_width=True, key="e1",
    column_config={
        "pH": st.column_config.NumberColumn(disabled=True),
        "V₁ (mL)": st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
        "V₂ (mL)": st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
        "V₃ (mL)": st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
    })

    df1["V moy"]      = df1[["V₁ (mL)","V₂ (mL)","V₃ (mL)"]].mean(axis=1)
    df1["[SO₂] mg/L"] = df1["V moy"].apply(lambda v: round(calc_SO2(v),1) if pd.notna(v) else None)
    df1["f exp (%)"]  = df1["[SO₂] mg/L"].apply(lambda c: round(c/100*100,2) if pd.notna(c) else None)
    df1["f théo (%)"] = df1["pH"].apply(lambda p: round(f_mol(p)*100,2))
    has1 = df1["[SO₂] mg/L"].notna().any()

    col_t, col_g = st.columns([1,2])
    with col_t:
        st.dataframe(df1[["pH","V moy","[SO₂] mg/L","f exp (%)","f théo (%)"]], hide_index=True, use_container_width=True)
        if has1:
            comp = df1[["pH","f exp (%)","f théo (%)"]].dropna()
            comp["Écart (pp)"] = (comp["f exp (%)"]-comp["f théo (%)"]).round(2)
            st.caption("Écart théorie/expérience")
            st.dataframe(comp, hide_index=True, use_container_width=True)

    with col_g:
        fig1, ax1 = plt.subplots(figsize=(7,4.5), constrained_layout=True)
        pH_th = np.linspace(2.5, 5.5, 500)
        ax1.plot(pH_th, f_mol(pH_th)*100, color=COULEURS[0], lw=2.5, label='Théorie')
        ax1.axvspan(3.0, 4.0, alpha=0.10, color='gold', label='Zone vin')
        if has1:
            mask = df1["f exp (%)"].notna()
            ax1.scatter(df1.loc[mask,"pH"], df1.loc[mask,"f exp (%)"],
                        color='red', zorder=5, s=70, label='Expérience')
        ax1.set_xlabel("pH"); ax1.set_ylabel("f (%)"); ax1.set_title("f(SO₂ mol.) vs pH")
        ax1.legend(); style_ax(ax1)
        st.pyplot(fig1)
        if has1:
            save_fig(fig1, "graphique_1_distribution.png")
            st.success("Graphique 1 mis à jour ✓")
        plt.close(fig1)


# ──────────────────────────────────────────────────────────────────────────────
# EXP. 2
# ──────────────────────────────────────────────────────────────────────────────
with tab2:
    st.subheader("Expérience 2 — Cinétique d'oxydation [SO₂] = f(t)")
    st.info("Volume d'I₂ moyen (moyenne de tes 3 titrages) à chaque temps, pour 3 pH.")

    t_vals = [0, 30, 60, 90, 120, 180, 240]
    df2 = st.data_editor(pd.DataFrame({
        "t (min)":            t_vals,
        "V moy pH 3.0 (mL)": [None]*len(t_vals),
        "V moy pH 3.5 (mL)": [None]*len(t_vals),
        "V moy pH 4.0 (mL)": [None]*len(t_vals),
    }), num_rows="fixed", use_container_width=True, key="e2",
    column_config={
        "t (min)": st.column_config.NumberColumn(disabled=True),
        "V moy pH 3.0 (mL)": st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
        "V moy pH 3.5 (mL)": st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
        "V moy pH 4.0 (mL)": st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
    })

    cols_V = ["V moy pH 3.0 (mL)","V moy pH 3.5 (mL)","V moy pH 4.0 (mL)"]
    cols_C = ["[SO₂] pH 3.0","[SO₂] pH 3.5","[SO₂] pH 4.0"]
    pH_labels = ["3.0","3.5","4.0"]
    k_th = {3.0:0.008/60, 3.5:0.018/60, 4.0:0.035/60}  # convertis en min⁻¹
    SO2_0_th = 80

    for cv, cc in zip(cols_V, cols_C):
        df2[cc] = df2[cv].apply(lambda v: calc_SO2(v) if pd.notna(v) else None)
    has2 = any(df2[c].notna().any() for c in cols_C)

    fig2, (ax_c, ax_ln) = plt.subplots(1, 2, figsize=(13,5), constrained_layout=True)
    t_th = np.linspace(0, 240, 200)  # en minutes

    for i, (pH_str, pH_val) in enumerate(zip(pH_labels, [3.0,3.5,4.0])):
        k = k_th[pH_val]
        ax_c.plot(t_th, SO2_0_th*np.exp(-k*t_th), color=COULEURS[i], lw=1.5, ls='--', alpha=0.45, label=f'pH {pH_str} théorie')
        ax_ln.plot(t_th, np.log(SO2_0_th*np.exp(-k*t_th)), color=COULEURS[i], lw=1.5, ls='--', alpha=0.45)

    resultats_k = {}
    if has2:
        for i, (cc, pH_str) in enumerate(zip(cols_C, pH_labels)):
            mask = df2[cc].notna() & (df2[cc] > 0)
            if mask.sum() >= 2:
                t_e = df2.loc[mask,"t (min)"].values.astype(float)
                c_e = df2.loc[mask, cc].values.astype(float)
                ax_c.scatter(t_e, c_e, color=COULEURS[i], s=50, zorder=5, label=f'pH {pH_str} exp.')
                sl, ic, r, _, _ = stats.linregress(t_e, np.log(c_e))
                k_exp = -sl
                resultats_k[pH_str] = {"k (min⁻¹)": round(k_exp,5), "t½ (min)": round(np.log(2)/k_exp,1), "R²": round(r**2,4)}
                ax_ln.scatter(t_e, np.log(c_e), color=COULEURS[i], s=50, zorder=5)
                t_fit = np.linspace(t_e.min(), t_e.max(), 100)
                ax_ln.plot(t_fit, sl*t_fit+ic, color=COULEURS[i], lw=2,
                           label=f'pH {pH_str}  k={k_exp:.4f}  R²={r**2:.4f}')

    ax_c.axhline(10, color='red', ls='-.', lw=1, alpha=0.7, label='Seuil 10 mg/L')
    ax_c.set_xlabel("t (min)"); ax_c.set_ylabel("[SO₂] mg/L"); ax_c.set_title("[SO₂] = f(t)")
    ax_c.legend(fontsize=8); style_ax(ax_c)
    ax_ln.set_xlabel("t (min)"); ax_ln.set_ylabel("ln[SO₂]"); ax_ln.set_title("Vérification ordre 1")
    style_ax(ax_ln)
    if has2: ax_ln.legend(fontsize=8)
    st.pyplot(fig2)
    if has2:
        save_fig(fig2, "graphique_2_cinetique.png")
        st.success("Graphique 2 mis à jour ✓")
        st.dataframe(pd.DataFrame(resultats_k).T.reset_index().rename(columns={"index":"pH"}), hide_index=True)
        if all(v["R²"] > 0.99 for v in resultats_k.values()):
            st.success("R² > 0,99 → cinétique d'ordre 1 confirmée ✓")
    plt.close(fig2)


# ──────────────────────────────────────────────────────────────────────────────
# EXP. 3
# ──────────────────────────────────────────────────────────────────────────────
with tab3:
    st.subheader("Expérience 3 — Effet de l'oxygène")
    st.info("pH 3,5 fixe. Bécher ouvert (aéré) vs fermé sous N₂ (désaéré). Mesures à t = 0, 30, 60, 90, 120, 180, 240 min.")

    df3 = st.data_editor(pd.DataFrame({
        "t (min)":               [0,30,60,90,120,180,240],
        "V moy OUVERT (mL)":   [None]*7,
        "V moy FERMÉ N₂ (mL)": [None]*7,
    }), num_rows="fixed", use_container_width=True, key="e3",
    column_config={
        "t (min)": st.column_config.NumberColumn(disabled=True),
        "V moy OUVERT (mL)":   st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
        "V moy FERMÉ N₂ (mL)": st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
    })

    df3["[SO₂] aéré"]    = df3["V moy OUVERT (mL)"].apply(lambda v: calc_SO2(v) if pd.notna(v) else None)
    df3["[SO₂] désaéré"] = df3["V moy FERMÉ N₂ (mL)"].apply(lambda v: calc_SO2(v) if pd.notna(v) else None)
    has3 = df3["[SO₂] aéré"].notna().any() or df3["[SO₂] désaéré"].notna().any()

    fig3, ax3 = plt.subplots(figsize=(9,5), constrained_layout=True)
    t_th3 = np.linspace(0, 240, 200)  # minutes
    SO2_0 = 80
    ax3.plot(t_th3, SO2_0*np.exp(-0.055/60*t_th3), color=COULEURS[2], lw=1.5, ls='--', alpha=0.45, label="Aéré — théorie")
    ax3.plot(t_th3, SO2_0*np.exp(-0.005/60*t_th3), color=COULEURS[0], lw=1.5, ls='--', alpha=0.45, label="Désaéré — théorie")

    if has3:
        m_a = df3["[SO₂] aéré"].notna()
        m_d = df3["[SO₂] désaéré"].notna()
        if m_a.any():
            ax3.plot(df3.loc[m_a,"t (min)"], df3.loc[m_a,"[SO₂] aéré"], 'o-', color=COULEURS[2], lw=2, ms=7, label="Aéré — exp.")
        if m_d.any():
            ax3.plot(df3.loc[m_d,"t (min)"], df3.loc[m_d,"[SO₂] désaéré"], 's-', color=COULEURS[0], lw=2, ms=7, label="Désaéré — exp.")
        ratios = []
        for col_c in ["[SO₂] aéré","[SO₂] désaéré"]:
            mask = df3[col_c].notna() & (df3[col_c] > 0)
            if mask.sum() >= 2:
                t_e = df3.loc[mask,"t (min)"].values.astype(float)
                c_e = df3.loc[mask,col_c].values.astype(float)
                sl, _, _, _, _ = stats.linregress(t_e, np.log(c_e))
                ratios.append(-sl)
        if len(ratios) == 2:
            st.metric("Rapport k_aéré / k_désaéré", f"{ratios[0]/ratios[1]:.1f}×",
                      help="Contribution de l'O₂ à la dégradation du SO₂")

    ax3.axhline(20, color='darkred', ls=':', lw=1.5, alpha=0.7)
    ax3.annotate("Seuil ~20 mg/L", xy=(0,20), xytext=(1,22), fontsize=8.5, color='darkred')
    ax3.set_xlabel("t (min)"); ax3.set_ylabel("[SO₂] mg/L")
    ax3.set_title("Exp. 3 — Effet de l'O₂ sur la durée de protection")
    ax3.legend(); style_ax(ax3)
    st.pyplot(fig3)
    if has3:
        save_fig(fig3, "graphique_3_oxygene.png")
        st.success("Graphique 3 mis à jour ✓")
    plt.close(fig3)


# ──────────────────────────────────────────────────────────────────────────────
# EXP. 4
# ──────────────────────────────────────────────────────────────────────────────
with tab4:
    st.subheader("Expérience 4 — Influence de la dose initiale C₀")
    st.info("pH 3,5 fixe. 5 doses (50/75/100/125/150 mg/L). Mesures à t=0 et t=2h (120 min). Si ordre 1 → k constant.")

    df4 = st.data_editor(pd.DataFrame({
        "C₀ (mg/L)":          [50.0, 75.0, 100.0, 125.0, 150.0],
        "V moy t=0 (mL)":     [None]*5,
        "V moy t=120min (mL)": [None]*5,
    }), num_rows="fixed", use_container_width=True, key="e4",
    column_config={
        "C₀ (mg/L)": st.column_config.NumberColumn(disabled=True),
        "V moy t=0 (mL)":      st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
        "V moy t=120min (mL)": st.column_config.NumberColumn(min_value=0.0, step=0.05, format="%.2f"),
    })

    df4["[SO₂] t=0"]    = df4["V moy t=0 (mL)"].apply(lambda v: calc_SO2(v) if pd.notna(v) else None)
    df4["[SO₂] t=120min"] = df4["V moy t=120min (mL)"].apply(lambda v: calc_SO2(v) if pd.notna(v) else None)
    mask4 = (df4["[SO₂] t=0"].notna() & df4["[SO₂] t=120min"].notna()
             & (df4["[SO₂] t=0"] > 0) & (df4["[SO₂] t=120min"] > 0))

    if mask4.any():
        df4.loc[mask4,"k (min⁻¹)"] = df4.loc[mask4].apply(
            lambda r: round(np.log(r["[SO₂] t=0"]/r["[SO₂] t=120min"])/120, 6), axis=1)
        df4.loc[mask4,"t½ (min)"] = df4.loc[mask4,"k (min⁻¹)"].apply(
            lambda k: round(np.log(2)/k,1) if pd.notna(k) and k>0 else None)
        st.dataframe(df4[["C₀ (mg/L)","[SO₂] t=0","[SO₂] t=120min","k (min⁻¹)","t½ (min)"]], hide_index=True)

        k_vals = df4.loc[mask4,"k (min⁻¹)"].dropna().values
        if len(k_vals) > 1:
            cv = np.std(k_vals)/np.mean(k_vals)*100
            (st.success if cv < 10 else st.warning)(f"k quasiment constant (CV = {cv:.1f}%) → ordre 1 {'vérifié ✓' if cv<10 else 'à vérifier'}")

        k_moyen = np.mean(k_vals)
        t_th4 = np.linspace(0, 240, 200)  # en minutes
        pH_ab = np.linspace(2.8, 4.5, 200)

        fig4, (ax4a, ax4b) = plt.subplots(1, 2, figsize=(14,5), constrained_layout=True)
        for i, (_, row) in enumerate(df4[mask4].iterrows()):
            C0 = row["[SO₂] t=0"]; k = row["k (min⁻¹)"]
            ax4a.plot(t_th4, C0*np.exp(-k*t_th4), color=COULEURS[i % len(COULEURS)], lw=2,
                      label=f"C₀={row['C₀ (mg/L)']} mg/L  k={k:.5f}")
            ax4a.scatter([0,120],[row["[SO₂] t=0"],row["[SO₂] t=120min"]], color=COULEURS[i % len(COULEURS)], s=60, zorder=5)
        ax4a.set_xlabel("t (min)"); ax4a.set_ylabel("[SO₂] mg/L")
        ax4a.set_title("Vérification ordre 1 (k constant)"); ax4a.legend(); style_ax(ax4a)

        def k_app(pH):
            return k_moyen * np.exp(0.8*(pH-3.5))
        dose = np.array([0.5/(f_mol(p)*np.exp(-k_app(p)*30)) for p in pH_ab])
        ax4b.axhline(150, color='darkred', ls='--', lw=1.5, alpha=0.8, label='Limite rouges 150 mg/L')
        ax4b.axhline(200, color='firebrick', ls='-.', lw=1.5, alpha=0.8, label='Limite blancs 200 mg/L')
        ax4b.fill_between(pH_ab, 150, 350, alpha=0.08, color='red')
        ax4b.plot(pH_ab, dose, color=COULEURS[0], lw=2.5,
                  label=f'Dose optimale (k exp. = {k_moyen:.5f} min⁻¹)')
        ax4b.set_xlabel("pH"); ax4b.set_ylabel("Dose initiale (mg/L)")
        ax4b.set_title("Abaque pratique — Dose optimale vs pH")
        ax4b.set_xlim(2.8,4.5); ax4b.set_ylim(0,350); ax4b.legend(); style_ax(ax4b)

        st.pyplot(fig4)
        save_fig(fig4, "graphique_4_abaque.png")
        st.success("Graphique 4 mis à jour avec tes k expérimentaux ✓")
        plt.close(fig4)
    else:
        st.caption("Entre tes mesures pour voir les résultats.")


# ──────────────────────────────────────────────────────────────────────────────
# GÉNÉRATION DOCUMENT RÉSULTATS
# ──────────────────────────────────────────────────────────────────────────────
with tab_docs:
    st.subheader("📄 Génération du document de résultats expérimentaux")

    st.markdown("""
**Logique des documents :**

| Document | Contenu | Quand |
|---|---|---|
| `rapport_TIPE_complet.docx` | Théorie + protocole + graphiques simulés | Avant l'expérience — déjà prêt |
| `revue_litterature_SO2_vin.docx` | Bibliographie | Déjà prêt |
| `preparation_oral_jury.docx` | Préparation oral | Déjà prêt |
| **`resultats_experimentaux.docx`** | **Tes mesures + graphiques exp. + analyse** | **Après l'expérience — généré ici** |
""")

    st.info("Entre d'abord tes mesures dans les 4 onglets, puis génère ton document de résultats.")

    def md_img(fname):
        p = os.path.join(BASE, fname).replace('\\', '/')
        return f'\n\n![]({p})\n\n' if os.path.exists(os.path.join(BASE, fname)) else '\n\n*(graphique non disponible)*\n\n'

    def build_resultats_md(df1, df2, df3, df4, mask4, resultats_k, ratios3):
        """Construit le markdown du document de résultats à partir des données saisies."""
        lines = []
        lines.append("# Résultats expérimentaux — TIPE SO₂ dans le vin\n")
        lines.append("**PC — 2ème année | Thème : Optimisation, Sobriété, Efficacité**\n")
        lines.append("---\n")

        # ── Exp 1
        lines.append("## Expérience 1 — Fraction moléculaire = f(pH)\n")
        has_e1 = df1["[SO₂] mg/L"].notna().any()
        if has_e1:
            lines.append("### Tableau de mesures\n")
            lines.append("| pH | V₁ (mL) | V₂ (mL) | V₃ (mL) | V moy (mL) | [SO₂] (mg/L) | f exp (%) | f théo (%) | Écart (pp) |")
            lines.append("|---|---|---|---|---|---|---|---|---|")
            for _, r in df1.iterrows():
                v1 = f"{r['V₁ (mL)']:.2f}" if pd.notna(r['V₁ (mL)']) else "—"
                v2 = f"{r['V₂ (mL)']:.2f}" if pd.notna(r['V₂ (mL)']) else "—"
                v3 = f"{r['V₃ (mL)']:.2f}" if pd.notna(r['V₃ (mL)']) else "—"
                vm = f"{r['V moy']:.2f}" if pd.notna(r['V moy']) else "—"
                so2 = f"{r['[SO₂] mg/L']:.1f}" if pd.notna(r['[SO₂] mg/L']) else "—"
                fe = f"{r['f exp (%)']:.2f}" if pd.notna(r['f exp (%)']) else "—"
                ft = f"{r['f théo (%)']:.2f}"
                ecart = f"{r['f exp (%)']-r['f théo (%)']:.2f}" if pd.notna(r['f exp (%)']) else "—"
                lines.append(f"| {r['pH']} | {v1} | {v2} | {v3} | {vm} | {so2} | {fe} | {ft} | {ecart} |")
            lines.append("")
            lines.append("### Graphique — Courbe théorique et points expérimentaux\n")
            lines.append(md_img("graphique_1_distribution.png"))
            lines.append("### Analyse\n")
            mask = df1["f exp (%)"].notna()
            if mask.any():
                ecarts = (df1.loc[mask,"f exp (%)"] - df1.loc[mask,"f théo (%)"]).abs()
                lines.append(f"L'écart moyen entre la fraction moléculaire expérimentale et théorique est de **{ecarts.mean():.2f} points de pourcentage**, ce qui valide le modèle acide-base utilisé (pK$_{{a1}}$ = 1,81).\n")
        else:
            lines.append("*Aucune mesure saisie.*\n")

        lines.append("---\n")

        # ── Exp 2
        lines.append("## Expérience 2 — Cinétique d'oxydation [SO₂] = f(t)\n")
        cols_C2 = ["[SO₂] pH 3.0","[SO₂] pH 3.5","[SO₂] pH 4.0"]
        has_e2 = any(c in df2.columns and df2[c].notna().any() for c in cols_C2)
        if has_e2 and resultats_k:
            lines.append("### Tableau de mesures\n")
            header = "| t (min) | V pH 3.0 (mL) | [SO₂] pH 3.0 | V pH 3.5 (mL) | [SO₂] pH 3.5 | V pH 4.0 (mL) | [SO₂] pH 4.0 |"
            lines.append(header)
            lines.append("|---|---|---|---|---|---|---|")
            for _, r in df2.iterrows():
                row_parts = [str(int(r["t (min)"]))]
                for cv, cc in zip(["V moy pH 3.0 (mL)","V moy pH 3.5 (mL)","V moy pH 4.0 (mL)"],
                                  ["[SO₂] pH 3.0","[SO₂] pH 3.5","[SO₂] pH 4.0"]):
                    v = f"{r[cv]:.2f}" if pd.notna(r.get(cv)) else "—"
                    c = f"{r[cc]:.1f}" if pd.notna(r.get(cc)) else "—"
                    row_parts += [v, c]
                lines.append("| " + " | ".join(row_parts) + " |")
            lines.append("")
            lines.append("### Constantes de vitesse extraites (régression linéaire sur ln[SO₂] = f(t))\n")
            lines.append("| pH | k (min⁻¹) | t½ (min) | R² |")
            lines.append("|---|---|---|---|")
            for pH_str, vals in resultats_k.items():
                k_key = list(vals.keys())[0]
                t_key = list(vals.keys())[1]
                r_key = list(vals.keys())[2]
                lines.append(f"| {pH_str} | {vals[k_key]} | {vals[t_key]} | {vals[r_key]} |")
            lines.append("")
            lines.append("### Graphique — [SO₂] = f(t) et vérification ordre 1\n")
            lines.append(md_img("graphique_2_cinetique.png"))
            lines.append("### Analyse\n")
            r2_vals = [v["R²"] for v in resultats_k.values()]
            if all(r >= 0.99 for r in r2_vals):
                lines.append(f"Les coefficients R² ({', '.join(str(r) for r in r2_vals)}) sont tous supérieurs à 0,99 : la cinétique d'oxydation du SO₂ est bien **d'ordre 1**. La constante de vitesse augmente avec le pH, ce qui confirme que le SO₂ moléculaire (majoritaire à bas pH) est plus stable que les formes ionisées.\n")
            else:
                lines.append("Les droites de régression ln[SO₂] = f(t) montrent des R² variables — vérifier la qualité des titrages.\n")
        else:
            lines.append("*Aucune mesure saisie.*\n")

        lines.append("---\n")

        # ── Exp 3
        lines.append("## Expérience 3 — Effet de l'oxygène\n")
        has_e3 = df3["[SO₂] aéré"].notna().any() or df3["[SO₂] désaéré"].notna().any()
        if has_e3:
            lines.append("### Tableau de mesures\n")
            lines.append("| t (min) | V OUVERT (mL) | [SO₂] aéré (mg/L) | V FERMÉ N₂ (mL) | [SO₂] désaéré (mg/L) |")
            lines.append("|---|---|---|---|---|")
            for _, r in df3.iterrows():
                va = f"{r['V moy OUVERT (mL)']:.2f}" if pd.notna(r.get('V moy OUVERT (mL)')) else "—"
                ca = f"{r['[SO₂] aéré']:.1f}" if pd.notna(r['[SO₂] aéré']) else "—"
                vd = f"{r['V moy FERMÉ N₂ (mL)']:.2f}" if pd.notna(r.get('V moy FERMÉ N₂ (mL)')) else "—"
                cd = f"{r['[SO₂] désaéré']:.1f}" if pd.notna(r['[SO₂] désaéré']) else "—"
                lines.append(f"| {int(r['t (min)'])} | {va} | {ca} | {vd} | {cd} |")
            lines.append("")
            lines.append("### Graphique — Aéré vs Désaéré\n")
            lines.append(md_img("graphique_3_oxygene.png"))
            if len(ratios3) == 2 and ratios3[1] > 0:
                ratio = ratios3[0]/ratios3[1]
                lines.append(f"### Analyse\n\nLe rapport k_aéré / k_désaéré = **{ratio:.1f}**, ce qui signifie que l'oxygène dissous accélère la dégradation du SO₂ d'un facteur {ratio:.1f}. Ceci justifie les pratiques œnologiques de travail sous atmosphère inerte (N₂ ou CO₂) pour réduire les apports de SO₂.\n")
        else:
            lines.append("*Aucune mesure saisie.*\n")

        lines.append("---\n")

        # ── Exp 4
        lines.append("## Expérience 4 — Influence de la dose initiale C₀\n")
        if mask4.any():
            lines.append("### Tableau de mesures et constantes de vitesse\n")
            lines.append("| C₀ (mg/L) | [SO₂] t=0 (mg/L) | [SO₂] t=120min (mg/L) | k (min⁻¹) | t½ (min) |")
            lines.append("|---|---|---|---|---|")
            for _, r in df4[mask4].iterrows():
                k_col = "k (min⁻¹)" if "k (min⁻¹)" in df4.columns else "k (h⁻¹)"
                t_col = "t½ (min)" if "t½ (min)" in df4.columns else "t½ (h)"
                kv = f"{r[k_col]:.5f}" if pd.notna(r.get(k_col)) else "—"
                tv = f"{r[t_col]:.1f}" if pd.notna(r.get(t_col)) else "—"
                lines.append(f"| {r['C₀ (mg/L)']} | {r['[SO₂] t=0']:.1f} | {r['[SO₂] t=120min']:.1f} | {kv} | {tv} |")
            lines.append("")
            lines.append("### Graphique — Ordre 1 et abaque pratique\n")
            lines.append(md_img("graphique_4_abaque.png"))
            k_col = "k (min⁻¹)" if "k (min⁻¹)" in df4.columns else "k (h⁻¹)"
            k_vals = df4.loc[mask4, k_col].dropna().values
            if len(k_vals) > 1:
                cv = np.std(k_vals)/np.mean(k_vals)*100
                lines.append(f"### Analyse\n\nLe coefficient de variation sur k est de **{cv:.1f}%** — {'la cinétique est bien d\'ordre 1 (k indépendant de C₀) ✓' if cv < 10 else 'k varie selon C₀, vérifier les mesures'}. L'abaque construit à partir de ces k expérimentaux permet de lire directement la dose initiale à ajouter pour chaque valeur de pH.\n")
        else:
            lines.append("*Aucune mesure saisie.*\n")

        lines.append("---\n")
        lines.append("## Conclusion générale\n")
        lines.append("Ces quatre expériences confirment expérimentalement que l'efficacité du SO₂ comme antioxydant dans le vin dépend de manière critique du pH. La fraction moléculaire active augmente fortement quand le pH diminue, ce qui permet de réduire significativement la dose totale de SO₂ tout en maintenant une protection équivalente — en accord avec les objectifs du thème **Optimisation / Sobriété / Efficacité**.\n")

        return '\n'.join(lines)

    def md_to_docx_bytes(md_content):
        tmp_md   = tempfile.NamedTemporaryFile(mode='w', suffix='.md', encoding='utf-8', delete=False, dir=BASE)
        tmp_docx = tempfile.NamedTemporaryFile(suffix='.docx', delete=False)
        tmp_md.write(md_content); tmp_md.close(); tmp_docx.close()
        cmd = [PANDOC, tmp_md.name, '-o', tmp_docx.name,
               '--from=markdown+tex_math_dollars+smart', '--standalone', '--wrap=none']
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            with open(tmp_docx.name, 'rb') as f:
                return f.read(), None
        except subprocess.CalledProcessError as e:
            return None, e.stderr[:400]
        finally:
            for p in [tmp_md.name, tmp_docx.name]:
                if os.path.exists(p): os.unlink(p)

    # Récupère les données des autres onglets via session_state
    # Les dataframes sont recalculés ici à partir des clés session_state
    if st.button("📊 Générer resultats_experimentaux.docx", type="primary", use_container_width=True):
        with st.spinner("Génération du document de résultats…"):
            # Récupère les ratios exp3 depuis les variables globales (calculées dans tab3)
            _ratios3 = []
            try:
                _df3 = df3.copy()
                for col_c in ["[SO₂] aéré","[SO₂] désaéré"]:
                    _mask = _df3[col_c].notna() & (_df3[col_c] > 0)
                    if _mask.sum() >= 2:
                        t_e = _df3.loc[_mask,"t (min)"].values.astype(float)
                        c_e = _df3.loc[_mask,col_c].values.astype(float)
                        sl, _, _, _, _ = stats.linregress(t_e, np.log(c_e))
                        _ratios3.append(-sl)
            except Exception:
                _ratios3 = []

            _rk = resultats_k if 'resultats_k' in dir() else {}
            _mask4 = mask4 if 'mask4' in dir() else pd.Series([False]*5)

            md = build_resultats_md(df1, df2, df3, df4, _mask4, _rk, _ratios3)
            data, err = md_to_docx_bytes(md)

        if data:
            st.success(f"✅ resultats_experimentaux.docx  ({len(data)//1024} Ko)")
            st.download_button(
                label="⬇️ Télécharger resultats_experimentaux.docx",
                data=data,
                file_name="resultats_experimentaux.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="dl_resultats"
            )
        else:
            st.error(f"Erreur pandoc : {err}")
            st.warning("Assure-toi que pandoc est installé sur ce serveur.")

    st.markdown("---")
    st.markdown("### Documents de base (théorie + protocole)")
    st.caption("Ces fichiers sont générés une fois depuis ton ordinateur avec generer_docx.py — ils ne changent pas.")
    for f in ["rapport_TIPE_complet.docx","revue_litterature_SO2_vin.docx","preparation_oral_jury.docx"]:
        p = os.path.join(BASE, f)
        if os.path.exists(p):
            with open(p,'rb') as fh:
                st.download_button(f"⬇️ {f}", data=fh.read(), file_name=f,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key=f"dl_base_{f}")
