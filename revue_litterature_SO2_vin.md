# Le Dioxyde de Soufre comme Conservateur Antioxydant dans le Vin : Optimisation en Fonction du pH et de la Concentration

---

## 1. Introduction — Historique et enjeux du SO₂ comme conservateur vinaire

L'utilisation du dioxyde de soufre ($\text{SO}_2$) dans la vinification est l'une des pratiques œnologiques les plus anciennes et les mieux documentées. Dès l'Antiquité romaine, les amphores étaient sulfurées par combustion de soufre afin de prévenir l'altération du vin. Cette technique empirique, mentionnée notamment par Pline l'Ancien dans son *Historia Naturalis*, s'est perpétuée à travers les siècles pour devenir, à l'ère moderne, un pilier technologique incontournable de l'industrie vinicole mondiale.

Le $\text{SO}_2$ remplit simultanément trois fonctions essentielles dans le vin :

- **Antimicrobienne** : il inhibe la croissance des levures non-*Saccharomyces*, des bactéries acétiques (*Acetobacter*) et des bactéries lactiques indésirables.
- **Antioxydante** : il piège l'oxygène dissous et les radicaux libres, retardant les oxydations enzymatiques et chimiques responsables du brunissement et de la perte aromatique.
- **Antioxydasique** : il inhibe la laccase et la polyphénoloxydase, enzymes fongiques et raisinesques catalysant l'oxydation des polyphénols.

Dans le contexte actuel du thème **Optimisation / Sobriété / Efficacité**, le $\text{SO}_2$ constitue un sujet d'étude exemplaire : comment maximiser son efficacité fonctionnelle tout en minimisant les doses ajoutées, dont les effets indésirables sur la santé humaine et la demande sociétale croissante pour des vins « naturels » imposent la réduction ? Cette question mobilise directement les outils de la chimie de PCSI : équilibres acide-base, cinétique d'ordre 1, oxydoréduction et dosages titrimetriques.

---

## 2. Formes chimiques du SO₂ en solution — Équilibres acide-base

### 2.1 Dissolution et équilibres

Lorsque le $\text{SO}_2$ gazeux est dissous dans le vin, il participe à une succession d'équilibres acide-base dans la gamme de pH du vin ($3{,}0 \leq \text{pH} \leq 4{,}0$) :

$$\text{SO}_2 \cdot \text{H}_2\text{O} \rightleftharpoons \text{H}^+ + \text{HSO}_3^- \qquad pK_{a1} \approx 1{,}81$$

$$\text{HSO}_3^- \rightleftharpoons \text{H}^+ + \text{SO}_3^{2-} \qquad pK_{a2} \approx 6{,}91$$

On distingue ainsi trois espèces soufrées en solution :

| Espèce | Nom courant | Rôle biologique |
|---|---|---|
| $\text{SO}_2 \cdot \text{H}_2\text{O}$ | SO₂ moléculaire (libre) | **Seule forme active** |
| $\text{HSO}_3^-$ | Ion hydrogénosulfite | Inactif |
| $\text{SO}_3^{2-}$ | Ion sulfite | Inactif |

> **Remarque structurante** : dans la littérature œnologique, on désigne par « $\text{SO}_2$ moléculaire » la concentration en $\text{SO}_2 \cdot \text{H}_2\text{O}$, car c'est la seule forme capable de traverser les membranes biologiques et d'exercer l'action antimicrobienne et antioxydante (Ribéreau-Gayon et al., 2017 [1]).

### 2.2 Fraction moléculaire en fonction du pH

La fraction molaire de la forme active se calcule à partir des deux équilibres successifs. En posant $[\text{H}^+] = 10^{-\text{pH}}$, $K_{a1} = 10^{-1{,}81}$ et $K_{a2} = 10^{-6{,}91}$, le bilan de masse sur le soufre(IV) donne :

$$f(\text{pH}) = \frac{[\text{SO}_2 \cdot \text{H}_2\text{O}]}{C_{\text{SO}_2}^{\text{total}}} = \frac{[\text{H}^+]^2}{[\text{H}^+]^2 + K_{a1}[\text{H}^+] + K_{a1} \cdot K_{a2}}$$

Cette expression, issue directement de la résolution du système d'équilibres, montre que $f$ croît quand $[\text{H}^+]$ augmente, c'est-à-dire quand le pH diminue. Le tableau suivant illustre ce résultat crucial :

| pH | $[\text{H}^+]$ (mol/L) | $f(\text{pH})$ (%) | $[\text{SO}_2]_{\text{mol}}$ pour 50 mg/L total |
|---|---|---|---|
| 3,0 | $10^{-3}$ | ≈ 6,0 % | ≈ 3,0 mg/L |
| 3,2 | $6{,}3 \times 10^{-4}$ | ≈ 3,8 % | ≈ 1,9 mg/L |
| 3,5 | $3{,}2 \times 10^{-4}$ | ≈ 1,9 % | ≈ 0,95 mg/L |
| 3,8 | $1{,}6 \times 10^{-4}$ | ≈ 0,96 % | ≈ 0,48 mg/L |
| 4,0 | $10^{-4}$ | ≈ 0,61 % | ≈ 0,30 mg/L |

*Calculs effectués avec $K_{a1} = 1{,}55 \times 10^{-2}$ mol/L et $K_{a2} = 1{,}23 \times 10^{-7}$ mol/L (Waterhouse et al., 2016 [2]).*

---

## 3. Influence du pH sur l'efficacité — Analyse quantitative

### 3.1 Relation entre pH et concentration active

L'efficacité antimicrobienne du $\text{SO}_2$ est corrélée non pas à la concentration totale en sulfites, mais à la concentration en **$\text{SO}_2$ moléculaire**. Ribéreau-Gayon et al. (2017) [1] indiquent qu'un seuil de $0{,}5$ à $0{,}8$ mg/L de $\text{SO}_2$ moléculaire est nécessaire pour exercer une protection antimicrobienne efficace en vinification.

En partant de la relation $[\text{SO}_2]_{\text{mol}} = f(\text{pH}) \times C_{\text{total}}$, on peut calculer la dose totale de sulfites nécessaire pour atteindre ce seuil :

$$C_{\text{total}}^{\text{requis}} = \frac{[\text{SO}_2]_{\text{mol}}^{\text{seuil}}}{f(\text{pH})}$$

| pH | $f$ (%) | Dose totale pour $[\text{SO}_2]_{\text{mol}} = 0{,}6$ mg/L |
|---|---|---|
| 3,0 | 6,0 | **10 mg/L** |
| 3,5 | 1,9 | **32 mg/L** |
| 4,0 | 0,61 | **98 mg/L** |

Ce tableau révèle l'enjeu d'optimisation fondamental : **à pH 4,0, il faut environ 10 fois plus de $\text{SO}_2$ total qu'à pH 3,0** pour obtenir la même protection.

### 3.2 Règle empirique : l'effet d'une variation de 0,5 unité pH

En différenciant $\ln f(\text{pH})$ par rapport au pH dans la zone $3{,}0$–$4{,}0$, on obtient une approximation analytique utile. Dans cette gamme, $[\text{H}^+] \gg K_{a2}$ mais $[\text{H}^+]$ est du même ordre de grandeur que $K_{a1}$, ce qui donne :

$$f \approx \frac{[\text{H}^+]}{[\text{H}^+] + K_{a1}}$$

La dérivée logarithmique montre que $f$ varie approximativement d'un **facteur 3 pour une diminution de 0,5 unité de pH**, ce qui est cohérent avec les données du tableau ci-dessus (passage de pH 3,5 à pH 3,0 : facteur $6{,}0/1{,}9 \approx 3{,}2$). Cette règle, souvent mentionnée par les œnologues praticiens, découle donc rigoureusement de la chimie des équilibres acide-base.

**Conséquence pratique** : en abaissant le pH du vin de 0,5 unité (par acidification tartrique autorisée), le vigneron peut diviser par 3 la dose de $\text{SO}_2$ nécessaire, tout en maintenant la même protection microbiologique. C'est un exemple concret de stratégie d'optimisation chimique.

---

## 4. Cinétique d'oxydation du SO₂ — Modèle d'ordre 1

### 4.1 La réaction d'oxydation

La réaction globale d'oxydation du $\text{SO}_2$ moléculaire par l'oxygène dissous s'écrit :

$$\text{SO}_2 + \frac{1}{2}\text{O}_2 + \text{H}_2\text{O} \longrightarrow \text{H}_2\text{SO}_4$$

En milieu vinaire, cette oxydation est catalysée par les ions métalliques traces, notamment le $\text{Fe}^{3+}$ et le $\text{Cu}^{2+}$, selon un mécanisme de type Fenton modifié impliquant des radicaux libres ($\text{HO}^\bullet$, $\text{SO}_3^{\bullet -}$).

### 4.2 Modèle cinétique d'ordre 1 en SO₂

En conditions de vin (oxygène en large excès ou contrôlé par les échanges avec l'atmosphère), la loi de vitesse se simplifie en une cinétique **pseudo-ordre 1** par rapport au $\text{SO}_2$ moléculaire :

$$\frac{d[\text{SO}_2]_{\text{mol}}}{dt} = -k_{\text{obs}} \cdot [\text{SO}_2]_{\text{mol}}$$

L'intégration donne :

$$[\text{SO}_2]_{\text{mol}}(t) = [\text{SO}_2]_{\text{mol},0} \cdot e^{-k_{\text{obs}} t}$$

La constante de pseudo-ordre 1 $k_{\text{obs}}$ dépend fortement du pH et de la concentration en catalyseurs métalliques :

| Condition | $k_{\text{obs}}$ (h⁻¹) | $t_{1/2}$ (heures) |
|---|---|---|
| pH 3,0, sans métaux | ≈ 0,002 | ≈ 350 h |
| pH 3,5, sans métaux | ≈ 0,005 | ≈ 140 h |
| pH 3,5, + Fe³⁺ (5 mg/L) | ≈ 0,020 | ≈ 35 h |
| pH 3,5, + Cu²⁺ (1 mg/L) | ≈ 0,015 | ≈ 46 h |

*Valeurs indicatives d'après Waterhouse et al. (2016) [2] et Boulton et al. (1996) [4].*

### 4.3 Dépendance au pH de la constante cinétique

Le pH agit doublement : d'une part sur la fraction active $f(\text{pH})$ (effet thermodynamique), d'autre part sur la cinétique d'oxydation elle-même. À pH plus élevé, l'ion $\text{SO}_3^{2-}$ est plus présent, or il est thermodynamiquement plus facilement oxydé que $\text{HSO}_3^-$. Il en résulte une **perte de $\text{SO}_2$ plus rapide aux pH élevés**, combinant deux effets défavorables pour le vigneron : moins de $\text{SO}_2$ actif initialement disponible, et une dégradation plus rapide du stock total.

---

## 5. Réglementation européenne

### 5.1 Cadre réglementaire principal

La teneur en $\text{SO}_2$ des vins commercialisés dans l'Union européenne est encadrée par le **Règlement (CE) n° 606/2009 de la Commission** du 10 juillet 2009 [3]. Ce texte fixe les teneurs maximales autorisées en dioxyde de soufre (exprimées en mg/L de $\text{SO}_2$ total) :

| Type de vin | Teneur résiduelle en sucres | Teneur maximale en SO₂ (mg/L) |
|---|---|---|
| Vins rouges | ≤ 5 g/L | **150 mg/L** |
| Vins blancs et rosés | ≤ 5 g/L | **200 mg/L** |
| Vins blancs et rosés | > 5 g/L | 250–300 mg/L (selon type) |
| Vins liquoreux (Sauternes, etc.) | > 45 g/L | jusqu'à **400 mg/L** |

### 5.2 Obligation d'étiquetage

Tout vin dont la teneur en $\text{SO}_2$ total dépasse **10 mg/L** doit obligatoirement porter la mention **« contient des sulfites »** sur l'étiquette. Cette mention vise à protéger les personnes souffrant d'hypersensibilité aux sulfites, estimées à environ 1% de la population générale et 5% des asthmatiques (Vally & Misso, 2012 [5]).

---

## 6. Méthodes de dosage — Titrimétrie iodimétrique

### 6.1 Méthode de référence OIV

La méthode de référence pour le dosage du $\text{SO}_2$ dans le vin, adoptée par l'**Organisation Internationale de la Vigne et du Vin (OIV)**, est la **méthode iodimétrique** (méthode OIV-MA-AS323-04B). Elle repose sur le titrage direct du $\text{SO}_2$ par une solution titrée de diiode $\text{I}_2$.

### 6.2 Principe chimique

La réaction de dosage est une réaction d'oxydoréduction quantitative :

$$\text{SO}_2 + \text{I}_2 + 2\text{H}_2\text{O} \longrightarrow \text{H}_2\text{SO}_4 + 2\text{HI}$$

Demi-équations redox :

$$\text{SO}_2 + 2\text{H}_2\text{O} \longrightarrow \text{SO}_4^{2-} + 4\text{H}^+ + 2e^- \quad \text{(oxydation)}$$

$$\text{I}_2 + 2e^- \longrightarrow 2\text{I}^- \quad \text{(réduction)}$$

La stœchiométrie est **1 mol de $\text{SO}_2$ pour 1 mol de $\text{I}_2$**.

### 6.3 Calcul de la concentration

$$[\text{SO}_2] \text{ (mg/L)} = \frac{C_{\text{I}_2} \times V_{\text{I}_2} \times M_{\text{SO}_2} \times 1000}{2 \times V_{\text{échantillon}}}$$

Avec $M_{\text{SO}_2} = 64{,}07$ g/mol, $C_{\text{I}_2}$ en mol/L, volumes en mL.

---

## 7. Enjeux actuels — Réduction des sulfites et alternatives

### 7.1 Comparaison des alternatives

| Alternative | Mode d'action | Avantages | Limites |
|---|---|---|---|
| **$\text{SO}_2$** | Antioxydant + antimicrobien + antioxydasique | Polyvalent, bon marché, éprouvé | Allergène potentiel |
| **Acide ascorbique** | Antioxydant (piège $\text{O}_2$) | Non allergène, naturel | Aucune action antimicrobienne |
| **Lysozyme** | Antimicrobien (lyse paroi bactérienne) | Efficace sur bactéries lactiques | Allergène (œuf) |
| **$\text{CO}_2$ / inertage** | Protection physique contre $\text{O}_2$ | Non chimique | Aucune action antimicrobienne |
| **Glutathion** | Antioxydant naturel | Naturel, présent dans le raisin | Coût, efficacité partielle |

---

## 8. Références bibliographiques

[1] Ribéreau-Gayon, P., Dubourdieu, D., Donèche, B., & Lonvaud-Funel, A. (2017). *Traité d'œnologie — Tome 1 : Microbiologie du vin, vinifications* (7ᵉ éd.). Dunod.

[2] Waterhouse, A. L., Sacks, G. L., & Jeffery, D. W. (2016). *Understanding Wine Chemistry*. Wiley-Blackwell. https://doi.org/10.1002/9781118730720

[3] Commission européenne. (2009). *Règlement (CE) n° 606/2009 de la Commission du 10 juillet 2009*. Journal Officiel de l'Union Européenne, L 193, 1–59.

[4] Boulton, R. B., Singleton, V. L., Bisson, L. F., & Kunkee, R. E. (1996). *Principles and Practices of Winemaking*. Springer. https://doi.org/10.1007/978-1-4615-1781-8

[5] Vally, H., & Misso, N. L. A. (2012). Adverse reactions to the sulphite additives. *Food and Chemical Toxicology*, *50*(10), 3771–3780. https://doi.org/10.1016/j.fct.2012.07.028

[6] Institut Français de la Vigne et du Vin (IFV). (2020). *Réduction et substitution du SO₂ en vinification : état des connaissances et recommandations pratiques* [Fiche technique]. IFV.

---

*Document rédigé dans le cadre d'un TIPE de classe préparatoire PCSI — Thème Optimisation / Sobriété / Efficacité.*
