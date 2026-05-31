# Optimisation de l'utilisation du dioxyde de soufre (SO₂) comme conservateur antioxydant dans le vin

**Niveau** : PCSI — Classe Préparatoire aux Grandes Écoles (Physique-Chimie-Sciences de l'Ingénieur)
**Année** : 2025–2026
**Thème TIPE** : Optimisation, Sobriété, Efficacité

---

## I. Problématique et ancrage thématique

### I.1. Contexte général

Le dioxyde de soufre ($\text{SO}_2$) est utilisé en œnologie depuis l'Antiquité romaine comme agent conservateur, antioxydant et antimicrobien. Sa présence dans le vin résulte soit d'une production naturelle par les levures lors de la fermentation alcoolique, soit d'un ajout volontaire par le vigneron, le plus souvent sous forme de métabisulfite de potassium ($\text{K}_2\text{S}_2\text{O}_5$). Son efficacité repose sur une propriété chimique fondamentale : seule la forme moléculaire dissoute $\text{SO}_2 \cdot \text{H}_2\text{O}$, minoritaire dans le vin, possède une activité antimicrobienne et antioxydante réelle.

Or, le $\text{SO}_2$ est un allergène reconnu, susceptible de provoquer des crises d'asthme chez les personnes sensibles. L'Union européenne encadre strictement son utilisation par le **Règlement CE n°606/2009**, qui fixe des teneurs maximales de **150 mg/L** pour les vins rouges et **200 mg/L** pour les vins blancs et rosés. Ces limites sont, par ailleurs, régulièrement débattues dans une société qui aspire à une alimentation moins chargée en additifs.

### I.2. Problème posé

Le vigneron se trouve ainsi confronté à un double impératif contradictoire : utiliser suffisamment de $\text{SO}_2$ pour protéger le vin de l'oxydation et des contaminations microbiennes, tout en restant en dessous des seuils réglementaires et en réduisant l'impact sanitaire de son produit. La question centrale de ce travail est donc :

> **Quelle est la dose minimale de $\text{SO}_2$ efficace en tant qu'antioxydant, et comment le pH du vin permet-il d'optimiser cette dose ?**

### I.3. Ancrage thématique

Ce sujet s'inscrit pleinement dans le triptyque **Optimisation — Sobriété — Efficacité** :

- **Optimisation** : il s'agit de trouver le couple $([\text{SO}_2], \text{pH})$ qui maximise l'efficacité antioxydante sous contrainte réglementaire.
- **Sobriété** : réduire la dose de $\text{SO}_2$ sans sacrifier la qualité du vin constitue une démarche de sobriété chimique, en accord avec les attentes sociétales contemporaines.
- **Efficacité** : comprendre la spéciation du $\text{SO}_2$ permet d'en maximiser la fraction active pour une dose totale donnée.

---

## II. Contexte scientifique

### II.1. Spéciation du dioxyde de soufre en solution aqueuse

Lorsque le $\text{SO}_2$ est dissous dans le vin, il établit deux équilibres acide-base successifs :

$$\text{SO}_2 \cdot \text{H}_2\text{O} \rightleftharpoons \text{HSO}_3^- + \text{H}^+ \qquad pK_{a1} = 1{,}81$$

$$\text{HSO}_3^- \rightleftharpoons \text{SO}_3^{2-} + \text{H}^+ \qquad pK_{a2} = 6{,}91$$

On distingue ainsi trois espèces soufrées en solution :

| Espèce | Nom courant | Rôle biologique |
|---|---|---|
| $\text{SO}_2 \cdot \text{H}_2\text{O}$ | SO₂ moléculaire | **Seule forme active** (antimicrobien + antioxydant) |
| $\text{HSO}_3^-$ | Ion hydrogénosulfite | Inactif |
| $\text{SO}_3^{2-}$ | Ion sulfite | Inactif |

Le vin présente un pH compris entre 3,0 et 4,0, situé entre $pK_{a1}$ et $pK_{a2}$ : la forme **largement majoritaire** est $\text{HSO}_3^-$ (inactif), et seule une fraction minoritaire de $\text{SO}_2$ moléculaire assure la protection.

### II.2. Fraction moléculaire en fonction du pH

La **fraction molaire** de la forme active est donnée par :

$$f(\text{pH}) = \frac{[\text{H}^+]^2}{[\text{H}^+]^2 + K_{a1}[\text{H}^+] + K_{a1} \cdot K_{a2}}$$

| pH | $f$ (%) | $[\text{SO}_2]_{\text{mol}}$ pour 50 mg/L total | Dose pour $[\text{SO}_2]_{\text{mol}} = 0{,}6$ mg/L |
|---|---|---|---|
| 3,0 | ~7,7 % | ~3,9 mg/L | **~8 mg/L** |
| 3,5 | ~2,9 % | ~1,5 mg/L | **~21 mg/L** |
| 4,0 | ~0,97 % | ~0,5 mg/L | **~62 mg/L** |

**Résultat clé** : abaisser le pH de 4,0 à 3,0 multiplie par ~8 la concentration en $\text{SO}_2$ moléculaire actif pour une dose totale identique.

### II.3. Cinétique d'oxydation — modèle d'ordre 1

La consommation de $\text{SO}_2$ libre par oxydation suit une **cinétique d'ordre 1** :

$$\frac{d[\text{SO}_2]}{dt} = -k \cdot [\text{SO}_2] \implies [\text{SO}_2](t) = [\text{SO}_2]_0 \cdot e^{-kt}$$

En passant au logarithme : $\ln[\text{SO}_2](t) = \ln[\text{SO}_2]_0 - k \cdot t$

La représentation de $\ln[\text{SO}_2]$ en fonction de $t$ donne une **droite de pente $-k$**, ce qui permet de déterminer la constante de vitesse $k$ et la **demi-vie** :

$$t_{1/2} = \frac{\ln 2}{k}$$

| Condition | $k_{\text{obs}}$ (h⁻¹) | $t_{1/2}$ (heures) |
|---|---|---|
| pH 3,0, sans métaux | ≈ 0,002 | ≈ 350 h |
| pH 3,5, sans métaux | ≈ 0,005 | ≈ 140 h |
| pH 3,5, + Fe³⁺ (5 mg/L) | ≈ 0,020 | ≈ 35 h |

### II.4. Méthode de dosage — titrimétrie iodimétrique

La concentration en $\text{SO}_2$ libre est mesurée par **titrage iodimétrique** (méthode OIV-MA-AS323-04B) :

$$\text{SO}_2 + \text{I}_2 + 2\,\text{H}_2\text{O} \longrightarrow \text{H}_2\text{SO}_4 + 2\,\text{HI}$$

Point d'équivalence : virage bleu-violet de l'**empois d'amidon** (indicateur de l'excès de $\text{I}_2$).

$$[\text{SO}_2] \text{ (mg/L)} = \frac{V(\text{I}_2)_{\text{mL}} \times c(\text{I}_2)_{\text{mol/L}} \times 64 \times 1000}{V_{\text{éch, mL}}}$$

### II.5. Cadre réglementaire

| Type de vin | Teneur maximale (SO₂ total) |
|---|---|
| Vin rouge | **150 mg/L** |
| Vin blanc, rosé | **200 mg/L** |
| Vin biologique rouge | 100 mg/L |
| Vin biologique blanc/rosé | 150 mg/L |

Mention obligatoire **« contient des sulfites »** au-delà de 10 mg/L.

---

## III. Protocole expérimental

### III.1. Matériel et réactifs

| Matériel | Spécifications | Quantité |
|---|---|---|
| Burette graduée | 25 mL, classe B, ±0,05 mL | 2 |
| Fioles jaugées | 250 mL et 1000 mL, classe A | 4 |
| pH-mètre + électrode | Résolution 0,01 unité pH | 1 |
| Agitateur magnétique | Avec chauffage | 2 |
| Béchers | 250 mL | 8 |
| Chronomètre | Précision 1 s | 1 |
| **Réactifs** | | |
| Acide tartrique | $\text{C}_4\text{H}_6\text{O}_6$, pureté ≥ 99,5 % | 10 g |
| Métabisulfite de potassium | $\text{K}_2\text{S}_2\text{O}_5$, grade alimentaire | 5 g |
| Solution d'iode | $c(\text{I}_2) = 0{,}02\ \text{mol/L}$, titrée | 500 mL |
| Iodure de potassium | KI, pour solubiliser I₂ | 5 g |
| Empois d'amidon | Solution à 1 %, fraîchement préparée | 100 mL |
| Acide sulfurique dilué | 1 mol/L | 50 mL |
| Soude | NaOH, 0,1 mol/L | 200 mL |
| Eau ultra-pure | Résistivité ≥ 1 MΩ·cm | 5 L |

### III.2. Préparation de la solution modèle

Dissoudre **4 g/L d'acide tartrique** dans de l'eau ultra-pure (pH initial ≈ 2,8). Ajuster le pH aux valeurs cibles (3,0 ; 3,2 ; 3,5 ; 3,8 ; 4,0) par ajout de NaOH 0,1 mol/L sous contrôle pH-métrique continu.

Le $\text{SO}_2$ est introduit sous forme de $\text{K}_2\text{S}_2\text{O}_5$ :

$$\text{K}_2\text{S}_2\text{O}_5 + \text{H}_2\text{O} \rightarrow 2\,\text{K}^+ + 2\,\text{HSO}_3^-$$

Masse à peser pour une concentration cible $C_0$ (mg/L) dans un volume $V$ (L) :

$$m(\text{K}_2\text{S}_2\text{O}_5) = \frac{C_0 \times V \times 222{,}3}{2 \times 64{,}06}$$

### III.3. Les quatre expériences

**Expérience 1 — Influence du pH : $[\text{SO}_2]_{\text{mol}} = f(\text{pH})$**

Préparer 5 solutions à pH = 3,0 ; 3,2 ; 3,5 ; 3,8 ; 4,0 avec $C_0 = 100$ mg/L de $\text{SO}_2$. Doser immédiatement le $\text{SO}_2$ libre par iodimétrie. Calculer $f$ expérimental et comparer à la valeur théorique.

**Expérience 2 — Cinétique d'oxydation : $[\text{SO}_2] = f(t)$**

À pH 3,5 (puis 3,0 et 4,0), $C_0 = 100$ mg/L, bécher ouvert à 20 °C. Prélever 20 mL toutes les 2 heures pendant 24 heures. Tracer $\ln[\text{SO}_2] = f(t)$ et extraire $k$ par régression linéaire.

**Expérience 3 — Effet de l'oxygène**

À pH fixe 3,5 : comparer l'évolution de $[\text{SO}_2]$ en bécher ouvert (aéré) vs. bécher fermé sous $\text{N}_2$ (désaéré). Mesures à $t = 0$, 6, 12, 24 h.

**Expérience 4 — Influence de la dose initiale**

À pH 3,5, trois solutions avec $C_0 = 50$, 100, 200 mg/L. Mesurer $[\text{SO}_2]$ à $t = 0$ et $t = 12$ h. Vérifier que $k$ est constant → validation de l'ordre 1.

### III.4. Protocole de dosage iodimétrique (mode opératoire)

1. Prélever 20 mL d'échantillon dans un erlenmeyer de 250 mL.
2. Ajouter 5 mL de $\text{H}_2\text{SO}_4$ (1 mol/L) et 5 mL d'empois d'amidon.
3. Remplir la burette avec $\text{I}_2$ titrée ($c = 0{,}02$ mol/L).
4. Titrer sous agitation magnétique jusqu'au **virage bleu persistant ≥ 30 s**.
5. Relever $V_{\text{éq}}(\text{I}_2)$ à ±0,05 mL.
6. Réaliser **3 titrages** par échantillon, retenir la moyenne.

### III.5. Estimation des incertitudes

Pour une burette classe B (25 mL) : $u(V) = 0{,}05/\sqrt{3} \approx 0{,}029$ mL (distribution rectangulaire).

$$\frac{u([\text{SO}_2])}{[\text{SO}_2]} \approx \frac{u(V_{\text{éq}})}{V_{\text{éq}}} \approx 0{,}8\% \text{ pour } V_{\text{éq}} \approx 5 \text{ mL}$$

---

## IV. Résultats attendus et exploitation

### IV.1. Graphique 1 — Fraction moléculaire vs. pH

Courbe décroissante théorique superposée aux points expérimentaux. Vérification de l'accord théorie/expérience. La multipliciation par ~8 de $f$ entre pH 4,0 et 3,0 doit être clairement visible.

### IV.2. Graphique 2 — Cinétique et vérification ordre 1

Tracé de $\ln[\text{SO}_2] = f(t)$ : trois droites de pentes différentes ($-k_{\text{pH 3,0}}$, $-k_{\text{pH 3,5}}$, $-k_{\text{pH 4,0}}$). $R^2 > 0{,}99$ attendu. Calcul de $t_{1/2}$ pour chaque pH.

### IV.3. Graphique 3 — Rôle de l'oxygène

Deux courbes : milieu aéré ($k_A$ élevé) vs milieu désaéré ($k_B$ faible). Le rapport $k_A/k_B$ quantifie la contribution de $\text{O}_2$ à la dégradation.

### IV.4. Graphique 4 — Abaque pH/dose optimale

Pour chaque pH, calcul de la dose $C_0$ nécessaire pour maintenir $[\text{SO}_2]_{\text{mol}} \geq 0{,}8$ mg/L pendant une durée cible, en combinant $f(\text{pH})$ et la loi exponentielle :

$$C_0(\text{pH}) = \frac{0{,}8}{f(\text{pH})} \cdot e^{k(\text{pH}) \cdot t_{\text{cible}}}$$

**Cet abaque est l'outil d'aide à la décision central du TIPE.**

---

## V. Conclusion et perspectives

### V.1. Synthèse

Ce travail démontre que l'efficacité du $\text{SO}_2$ comme antioxydant dans le vin dépend de manière critique du **pH du milieu**. La fraction moléculaire active augmente d'un facteur ~8 quand le pH descend de 4,0 à 3,0. Un ajustement du pH de 4,0 à 3,2 permettrait de réduire la dose totale de $\text{SO}_2$ d'un facteur 3 à 5 pour un niveau de protection identique.

Le modèle cinétique d'ordre 1 fournit un outil quantitatif de prédiction de l'efficacité dans le temps.

### V.2. Limites

- Solution modèle simplifiée (pas de polyphénols, alcool, sucres)
- Constantes $k$ à recalibrer sur vin réel
- Effet antimicrobien non testé directement

### V.3. Perspectives

- Partenariats avec INRAE / IFV sur réduction des intrants
- Modélisation numérique (Python) de l'abaque pH/dose pour tout type de vin
- Développement de capteurs connectés pour pilotage en temps réel du SO₂

---

## Références

Beelman, R. B., & Gallander, J. F. (1979). Wine deacidification. *Advances in Food Research*, 25, 1–53.

Institut Français de la Vigne et du Vin (IFV). (2021). *Réduction des intrants : bilan des essais menés en cave entre 2015 et 2020*. IFV Éditions.

Lisanti, M. T., et al. (2019). Alternative methods to SO₂ for microbiological stabilization of wine. *Comprehensive Reviews in Food Science and Food Safety*, 18(2), 455–479.

Ribéreau-Gayon, P., Dubourdieu, D., Donèche, B., & Lonvaud, A. (2012). *Traité d'œnologie — Tome 1* (6e éd.). Dunod.

Union européenne. (2009). *Règlement (CE) n°606/2009*. Journal officiel de l'Union européenne, L 193, 1–59.

Waterhouse, A. L., & Laurie, V. F. (2006). Oxidation of wine phenolics. *American Journal of Enology and Viticulture*, 57(3), 306–313.

---

*Rapport rédigé dans le cadre du TIPE — session 2025–2026. Thème : Optimisation / Sobriété / Efficacité.*
