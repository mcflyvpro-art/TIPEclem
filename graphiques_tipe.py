"""
TIPE - Optimisation du SO2 comme conservateur dans le vin
Génération des 4 graphiques expérimentaux
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # pas de fenêtre interactive, sauvegarde directe
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

COULEURS = ['#2C5F8A', '#E07B39', '#3A8A5F', '#9B3A8A']

Ka1 = 10**(-1.81)
Ka2 = 10**(-6.91)

def fraction_moleculaire(pH):
    H = 10**(-pH)
    return H**2 / (H**2 + Ka1 * H + Ka1 * Ka2)

def fraction_bisulfite(pH):
    H = 10**(-pH)
    return (Ka1 * H) / (H**2 + Ka1 * H + Ka1 * Ka2)

def fraction_sulfite(pH):
    H = 10**(-pH)
    return (Ka1 * Ka2) / (H**2 + Ka1 * H + Ka1 * Ka2)


# ─── Fonctions de tracé individuelles ───────────────────────────────────────

def plot_graphique1(ax):
    pH_range = np.linspace(0, 10, 500)
    f_mol    = fraction_moleculaire(pH_range) * 100
    f_bisulf = fraction_bisulfite(pH_range) * 100
    f_sulf   = fraction_sulfite(pH_range) * 100

    ax.plot(pH_range, f_mol,    color=COULEURS[0], lw=2.5, label='SO₂ moléculaire (actif)')
    ax.plot(pH_range, f_bisulf, color=COULEURS[1], lw=2.5, label='HSO₃⁻ (inactif)')
    ax.plot(pH_range, f_sulf,   color=COULEURS[2], lw=2.5, label='SO₃²⁻ (inactif)')
    ax.axvspan(3.0, 4.0, alpha=0.12, color='gold', label='Zone vin (pH 3–4)')

    for pH_val, ls in [(3.0, '--'), (3.5, ':'), (4.0, '--')]:
        f = fraction_moleculaire(pH_val) * 100
        ax.axvline(pH_val, color='gray', ls=ls, lw=1, alpha=0.6)
        ax.annotate(f'pH {pH_val}\n{f:.1f}%', xy=(pH_val, f),
                    xytext=(pH_val + 0.25, f + 9),
                    fontsize=8, color=COULEURS[0],
                    arrowprops=dict(arrowstyle='->', color=COULEURS[0], lw=1))

    ax.set_xlabel('pH')
    ax.set_ylabel('Fraction molaire (%)')
    ax.set_title('Exp. 1 — Distribution des espèces du SO₂ en fonction du pH')
    ax.legend(loc='center right')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 110)
    ax.grid(True, alpha=0.3)


def plot_graphique2(ax):
    ax2_inset = ax.inset_axes([0.50, 0.52, 0.46, 0.42])
    t = np.linspace(0, 120, 300)
    params = [
        (3.0, 0.008, COULEURS[0]),
        (3.5, 0.018, COULEURS[1]),
        (4.0, 0.035, COULEURS[2]),
    ]
    SO2_0 = 80

    for pH_val, k, col in params:
        SO2_t  = SO2_0 * np.exp(-k * t)
        ln_SO2 = np.log(SO2_t)
        ax.plot(t, SO2_t, color=col, lw=2, label=f'pH = {pH_val}')
        ax2_inset.plot(t, ln_SO2, color=col, lw=1.5, ls='--')

    ax.axhline(10, color='red', ls='-.', lw=1.5, alpha=0.8, label='Seuil détection 10 mg/L')
    ax.set_xlabel('Temps (h)')
    ax.set_ylabel('[SO₂] libre (mg/L)')
    ax.set_title("Exp. 2 — Cinétique d'oxydation\n[SO₂] = f(t) et vérification ordre 1")
    ax.legend()
    ax.set_ylim(0, 95)
    ax.grid(True, alpha=0.3)

    ax2_inset.set_xlabel('t (h)', fontsize=8)
    ax2_inset.set_ylabel('ln[SO₂]', fontsize=8)
    ax2_inset.set_title('ln[SO₂] = f(t)', fontsize=8)
    ax2_inset.tick_params(labelsize=7)
    ax2_inset.grid(True, alpha=0.3)
    ax2_inset.annotate('pente = −k',
                       xy=(60, np.log(SO2_0 * np.exp(-0.018 * 60))),
                       xytext=(70, np.log(SO2_0 * np.exp(-0.008 * 60))),
                       fontsize=7, arrowprops=dict(arrowstyle='->', lw=0.8))


def plot_graphique3(ax):
    t3 = np.linspace(0, 96, 300)
    SO2_0 = 80
    conditions = [
        ('Fermeture hermétique (sans O₂)', 0.005, COULEURS[0], '-'),
        ('Contact limité O₂ (bouchon classique)', 0.022, COULEURS[1], '--'),
        ('Exposition pleine O₂ (barrique ouverte)', 0.055, COULEURS[2], '-.'),
    ]

    for label, k, col, ls in conditions:
        ax.plot(t3, SO2_0 * np.exp(-k * t3), color=col, lw=2.2, ls=ls, label=label)

    ax.axhline(20, color='darkred', ls=':', lw=1.5, alpha=0.7)
    ax.annotate('Seuil minimum\nefficace ~20 mg/L', xy=(0, 20), xytext=(5, 25),
                fontsize=8.5, color='darkred')
    ax.fill_between(t3,
                    SO2_0 * np.exp(-0.005 * t3),
                    SO2_0 * np.exp(-0.055 * t3),
                    alpha=0.08, color=COULEURS[0],
                    label="Zone d'efficacité variable")

    ax.set_xlabel('Temps (h)')
    ax.set_ylabel('[SO₂] libre (mg/L)')
    ax.set_title("Exp. 3 — Effet de l'exposition à O₂ sur la durée de protection")
    ax.legend(loc='upper right')
    ax.set_ylim(0, 95)
    ax.grid(True, alpha=0.3)


def plot_graphique4(ax):
    pH_vals = np.linspace(2.8, 4.5, 200)
    seuil_mol = 0.5
    t_cible   = 30

    def k_apparent(pH):
        return 0.005 * np.exp(0.8 * (pH - 3.0))

    dose_requise = np.array([
        seuil_mol / (fraction_moleculaire(pH) * np.exp(-k_apparent(pH) * t_cible))
        for pH in pH_vals
    ])

    ax.axhline(150, color='darkred', ls='--', lw=1.5, label='Limite CE vins rouges (150 mg/L)', alpha=0.8)
    ax.axhline(200, color='firebrick', ls='-.', lw=1.5, label='Limite CE blancs/rosés (200 mg/L)', alpha=0.8)
    ax.fill_between(pH_vals, 150, 350, alpha=0.08, color='red', label='Hors réglementation')
    ax.fill_between(pH_vals, 0, np.minimum(dose_requise, 350), alpha=0.15, color=COULEURS[0])
    ax.plot(pH_vals, dose_requise, color=COULEURS[0], lw=2.5,
            label=f'Dose initiale pour [SO₂ mol.] ≥ 0.5 mg/L après {t_cible}h')

    mask = pH_vals <= 4.0
    pH_opt   = pH_vals[mask][np.argmin(dose_requise[mask])]
    dose_opt = dose_requise[np.argmin(np.abs(pH_vals - pH_opt))]
    ax.annotate(f'pH optimal\n≈ {pH_opt:.2f}',
                xy=(pH_opt, dose_opt), xytext=(pH_opt + 0.2, dose_opt + 30),
                fontsize=9, color=COULEURS[0],
                arrowprops=dict(arrowstyle='->', color=COULEURS[0]))

    ax.set_xlabel('pH du vin')
    ax.set_ylabel('[SO₂] initiale à ajouter (mg/L)')
    ax.set_title('Exp. 4 + Synthèse — Abaque pratique\nDose initiale optimale en fonction du pH')
    ax.legend()
    ax.set_xlim(2.8, 4.5)
    ax.set_ylim(0, 350)
    ax.grid(True, alpha=0.3)


# ─── Sauvegarde individuelle (pour insertion dans les docx) ─────────────────

individual = [
    ('graphique_1_distribution.png', plot_graphique1,
     'Exp. 1 — Distribution des espèces du SO₂'),
    ('graphique_2_cinetique.png', plot_graphique2,
     'Exp. 2 — Cinétique d\'oxydation'),
    ('graphique_3_oxygene.png', plot_graphique3,
     'Exp. 3 — Effet de l\'oxygène'),
    ('graphique_4_abaque.png', plot_graphique4,
     'Exp. 4 — Abaque dose/pH'),
]

for fname, plot_fn, title in individual:
    fig_ind, ax_ind = plt.subplots(figsize=(10, 6), constrained_layout=True)
    plot_fn(ax_ind)
    fig_ind.savefig(fname, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig_ind)
    print(f"Sauvegardé : {fname}")


# ─── Figure combinée 2×2 ────────────────────────────────────────────────────

fig = plt.figure(figsize=(16, 14), constrained_layout=True)
fig.suptitle(
    "TIPE — Optimisation du SO₂ dans le vin\n"
    "Influence du pH et de la concentration sur l'efficacité du conservateur",
    fontsize=15, fontweight='bold'
)

gs = GridSpec(2, 2, figure=fig)
axes = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]),
        fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])]

plot_graphique1(axes[0])
plot_graphique2(axes[1])
plot_graphique3(axes[2])
plot_graphique4(axes[3])

fig.savefig('graphiques_tipe.png',    dpi=200, bbox_inches='tight', facecolor='white')
fig.savefig('graphiques_tipe_hd.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig)

print("\nFigure combinée : graphiques_tipe.png / graphiques_tipe_hd.png")
print("Tous les graphiques ont été générés avec succès !")
