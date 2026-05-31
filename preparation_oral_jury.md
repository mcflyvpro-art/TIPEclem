# Préparation à l'oral TIPE — SO₂ comme conservateur dans le vin
**Jury simulé — Niveau concours CCP/Mines/Centrale — PCSI**

---

## Catégorie 1 — Chimie des équilibres

**Q1 : Présentez les trois formes sous lesquelles le dioxyde de soufre existe en solution aqueuse et donnez les équilibres acido-basiques correspondants.**

**R :** En solution aqueuse, le SO₂ dissous se comporte comme un diacide faible selon deux équilibres successifs :

- $\text{SO}_2(\text{aq}) + \text{H}_2\text{O} \rightleftharpoons \text{HSO}_3^- + \text{H}^+$, avec $pK_{a1} = 1{,}81$
- $\text{HSO}_3^- \rightleftharpoons \text{SO}_3^{2-} + \text{H}^+$, avec $pK_{a2} = 6{,}91$

À pH acide (vin : pH 3–4), la forme dominante est $\text{HSO}_3^-$, mais une fraction non négligeable de SO₂ moléculaire subsiste. C'est **cette fraction qui conditionne l'efficacité conservatrice**. La forme $\text{SO}_3^{2-}$ est quasi absente à pH vinique.

---

**Q2 : Établissez l'expression de la fraction molaire de SO₂ moléculaire en fonction de [H⁺], Ka₁ et Ka₂. Calculez numériquement cette fraction à pH = 3,5.**

**R :** Le bilan de matière sur le soufre(IV) donne :

$$f = \frac{[\text{SO}_2]}{C} = \frac{[\text{H}^+]^2}{[\text{H}^+]^2 + K_{a1}[\text{H}^+] + K_{a1} \cdot K_{a2}}$$

À pH = 3,5 : $[\text{H}^+] = 10^{-3{,}5} \approx 3{,}16 \times 10^{-4}$ mol/L

- $K_{a1} = 10^{-1{,}81} \approx 1{,}55 \times 10^{-2}$
- $K_{a1} \cdot K_{a2} = 10^{-8{,}72} \approx 1{,}90 \times 10^{-9}$

Numérateur : $(3{,}16 \times 10^{-4})^2 \approx 9{,}99 \times 10^{-8}$

Dénominateur : $9{,}99 \times 10^{-8} + (1{,}55 \times 10^{-2})(3{,}16 \times 10^{-4}) \approx 5{,}00 \times 10^{-6}$

$$\boxed{f \approx \frac{9{,}99 \times 10^{-8}}{5{,}00 \times 10^{-6}} \approx 2{,}0\%}$$

À pH 3,5, seulement **2 % du SO₂ total est sous forme active**.

---

**Q3 : Comment évolue qualitativement la fraction de SO₂ moléculaire lorsque le pH passe de 3,0 à 4,0 ? Quelle conséquence pratique pour le vigneron ?**

**R :** $f$ est une fonction décroissante du pH : lorsque $[\text{H}^+]$ diminue, le numérateur $[\text{H}^+]^2$ décroît plus vite que le dénominateur. Ainsi, entre pH 3,0 et 4,0, $f$ passe de ~7,7 % à ~0,97 % (facteur ~8). **Conséquence** : pour maintenir $[\text{SO}_2]_{\text{mol}} \geq 0{,}8$ mg/L (seuil antimicrobien), le vigneron doit ajouter ~8 fois plus de SO₂ total à pH 4,0 qu'à pH 3,0 — tout en restant sous les limites réglementaires.

---

**Q4 : Tracez et commentez le diagramme de prédominance des espèces du SO₂. Quelle espèce prédomine dans la gamme de pH d'un vin rouge (pH ≈ 3,3–3,7) ?**

**R :** Frontières verticales aux pH = $pK_{a1} = 1{,}81$ et $pK_{a2} = 6{,}91$ :
- pH < 1,81 : SO₂ moléculaire prédomine
- 1,81 < pH < 6,91 : **HSO₃⁻ prédomine** (zone du vin)
- pH > 6,91 : SO₃²⁻ prédomine

Dans la gamme œnologique (pH 3,3–3,7), **HSO₃⁻ est l'espèce largement dominante** (>98 %). Ce diagramme illustre pourquoi la dose totale de SO₂ doit être bien supérieure à la concentration cible active.

---

**Q5 : Pourquoi parle-t-on de « SO₂ libre » et de « SO₂ combiné » en œnologie ? Ces notions coïncident-elles avec les formes chimiques acido-basiques ?**

**R :** Le **SO₂ libre** désigne les formes en équilibre (SO₂ moléculaire + HSO₃⁻ + SO₃²⁻). Le **SO₂ combiné** correspond au SO₂ ayant réagi avec des composés carbonylés du vin (acétaldéhyde, sucres) pour former des adduits hydroxysufonates $[\text{R-CH(OH)-SO}_3^-]$, inactifs. Le **SO₂ total** = libre + combiné. La superposition n'est pas exacte : le SO₂ libre est la catégorie acido-basique ; le SO₂ combiné est une catégorie de réactivité distincte. Seul le SO₂ moléculaire (fraction du libre) est actif.

---

## Catégorie 2 — Cinétique chimique

**Q6 : Rappelez la définition d'une loi d'ordre 1, établissez [SO₂](t) et précisez les conditions expérimentales validant ce postulat.**

**R :** Une réaction est d'ordre 1 par rapport à SO₂ si $v = k[\text{SO}_2]$, avec $k$ en s⁻¹. L'intégration donne :

$$[\text{SO}_2](t) = [\text{SO}_2]_0 \cdot e^{-kt}$$

Conditions de validité : (1) oxygène en large excès (pseudo-ordre 1 apparent), (2) pH et température maintenus constants, (3) linéarité de $\ln[\text{SO}_2] = f(t)$ vérifiée expérimentalement sur plusieurs demi-vies avec $R^2 > 0{,}99$.

---

**Q7 : Comment tracez-vous le graphique permettant de vérifier l'ordre 1 et d'extraire k ?**

**R :** En prenant le logarithme :

$$\ln[\text{SO}_2](t) = \ln[\text{SO}_2]_0 - k \cdot t$$

On trace **ln[SO₂] = f(t)** (droite si ordre 1) :
- **pente** = $-k$ (constante de vitesse)
- **ordonnée à l'origine** = $\ln[\text{SO}_2]_0$ (concentration initiale)

Ajustement par régression linéaire, vérification $R^2 \geq 0{,}99$, résidus aléatoires.

---

**Q8 : Définissez le temps de demi-vie t₁/₂ d'une réaction d'ordre 1. Calculez-le pour k = 0,012 h⁻¹.**

**R :** Le temps de demi-vie est la durée pour que la concentration soit divisée par deux :

$$t_{1/2} = \frac{\ln 2}{k} = \frac{0{,}693}{0{,}012} \approx \mathbf{57{,}8 \text{ h} \approx 2{,}4 \text{ jours}}$$

**Propriété remarquable** : $t_{1/2}$ est **indépendant de $[\text{SO}_2]_0$** (ordre 1). Pour le vigneron : la moitié du SO₂ est perdue en ~2,4 jours, nécessitant des sulfitages réguliers.

---

**Q9 : Quels facteurs physico-chimiques modifient la constante de vitesse k ? Comment les avez-vous contrôlés ?**

**R :** Facteurs influençant $k$ :
1. **Température** : loi d'Arrhénius ($k = A e^{-E_a/RT}$)
2. **pH** : formes HSO₃⁻ et SO₃²⁻ plus réactives vis-à-vis de certains oxydants
3. **[O₂] dissous** : principal oxydant
4. **Ions métalliques** (Fe²⁺, Cu²⁺) : catalyseurs de l'oxydation
5. **Polyphénols et sucres** : compétition pour O₂

Contrôle dans le protocole : bain thermostaté (T constante), tampon acétate (pH constant), atmosphère contrôlée (bécher ouvert/fermé).

---

**Q10 : Si ln[SO₂] = f(t) présente une courbure, quelles hypothèses émettez-vous ?**

**R :** La non-linéarité indique que l'ordre 1 n'est pas vérifié globalement. Hypothèses :
1. **Ordre différent de 1** (tester $1/[\text{SO}_2] = f(t)$ pour ordre 2)
2. **k variable** si le pH évolue au cours de la réaction (production de $\text{H}_2\text{SO}_4$)
3. **Mécanisme en deux étapes** : dégradation rapide du SO₂ libre + libération lente du SO₂ combiné
4. **Épuisement de l'O₂** si pas en large excès

---

## Catégorie 3 — Dosage et métrologie

**Q11 : Décrivez le principe du titrage iodimétrique du SO₂ et écrivez les demi-réactions et l'équation bilan.**

**R :** Le titrage repose sur l'oxydation du SO₂ par le diiode en milieu acide.

Demi-réactions :
- Oxydation : $\text{SO}_2 + 2\text{H}_2\text{O} \rightarrow \text{SO}_4^{2-} + 4\text{H}^+ + 2e^-$
- Réduction : $\text{I}_2 + 2e^- \rightarrow 2\text{I}^-$

Équation bilan :

$$\text{SO}_2 + \text{I}_2 + 2\text{H}_2\text{O} \rightarrow \text{H}_2\text{SO}_4 + 2\text{HI}$$

Stœchiométrie **1:1** (1 mol SO₂ pour 1 mol I₂). Point d'équivalence repéré par le **virage bleu-violet de l'empois d'amidon** (complexe amylose-I₃⁻).

---

**Q12 : Établissez la formule de calcul de [SO₂] (mg/L).**

**R :** À l'équivalence : $n(\text{SO}_2) = n(\text{I}_2) = c(\text{I}_2) \times V(\text{I}_2)$.

$$[\text{SO}_2] \text{ (mg/L)} = \frac{V(\text{I}_2)_{\text{mL}} \times c(\text{I}_2)_{\text{mol/L}} \times 64{,}06 \times 1000}{V_{\text{éch, mL}}}$$

Où $M(\text{SO}_2) = 64{,}06$ g/mol et les volumes sont en mL.

---

**Q13 : Quelles sont les principales sources d'erreur systématique dans ce dosage ? Comment les minimiser ?**

**R :**
1. **Volatilité du SO₂** → travailler rapidement, flacons bouchés, acidifier juste avant dosage
2. **Oxydation de I⁻ par l'air** → fioles iodées opaques, solution fraîche, standardisation régulière
3. **Virage imprécis** sur vin rouge → dosage en retour ou filtration préalable
4. **Dosage du SO₂ combiné** → tamponner à pH adéquat pour ne doser que le SO₂ libre
5. **Erreur de lecture burette** → lire le bas du ménisque, 3 essais concordants

---

**Q14 : Estimez l'incertitude sur [SO₂] par propagation des incertitudes.**

**R :** $[\text{SO}_2] = f(V(\text{I}_2), c(\text{I}_2), V_{\text{éch}})$. Incertitude relative composée :

$$\frac{u([\text{SO}_2])}{[\text{SO}_2]} = \sqrt{\left(\frac{u(V_{\text{I}_2})}{V_{\text{I}_2}}\right)^2 + \left(\frac{u(c_{\text{I}_2})}{c_{\text{I}_2}}\right)^2 + \left(\frac{u(V_{\text{éch}})}{V_{\text{éch}}}\right)^2}$$

Ordres de grandeur : $u(V)/V \approx 1$–2 %, $u(c)/c \approx 0{,}5$ %, $u(V_{\text{éch}})/V_{\text{éch}} \approx 0{,}2$ %.

Incertitude relative combinée ≈ **1,5–2 %** → pour [SO₂] = 100 mg/L : incertitude élargie ($k=2$) ≈ ±3–4 mg/L.

---

**Q15 : Pourquoi réaliser un essai à blanc ? Que mesure-t-il et comment corrige-t-on le résultat ?**

**R :** L'essai à blanc titre le volume $V_{\text{blanc}}$ de I₂ consommé par les **réducteurs de la matrice autres que SO₂** (polyphénols, acide ascorbique, Fe²⁺, indicateur lui-même). Correction :

$$V_{\text{I}_2, \text{corrigé}} = V_{\text{I}_2, \text{échantillon}} - V_{\text{blanc}}$$

Sans blanc, on **surestime [SO₂]**. Dans un vin réel, l'erreur peut atteindre 5–15 mg/L, significatif par rapport aux limites réglementaires.

---

## Catégorie 4 — Protocole et démarche expérimentale

**Q16 : Justifiez le choix d'une solution modèle plutôt que du vin réel. Quelles sont les limites ?**

**R :** Avantages de la solution modèle :
- **Contrôle exact** de [SO₂]₀, pH, température, composition
- **Reproductibilité** : pas de variabilité liée au millésime ou cépage
- **Dosage simplifié** : pas d'interférences des polyphénols et pigments

**Limites** : la matrice du vin réel joue un rôle (polyphénols compétiteurs pour O₂, SO₂ combiné plus important, effet tampon naturel). Les valeurs de $k$ sur solution modèle ne sont pas directement transposables au vin réel.

---

**Q17 : Décrivez la préparation d'une solution tampon à pH = 3,5. Comment vérifiez-vous le pH obtenu ?**

**R :** Pour le tampon acétate ($pK_a = 4{,}76$), Henderson-Hasselbalch : $3{,}5 = 4{,}76 + \log[\text{A}^-]/[\text{AH}]$ → $[\text{A}^-]/[\text{AH}] = 10^{-1{,}26} \approx 0{,}055$. En pratique : 100 mL AcOH 0,1 mol/L + 5,5 mL AcONa 0,1 mol/L. Ajustement fin avec HCl dilué. Vérification : **pH-mètre étalonné** sur 2 points (tampons commerciaux pH 4,0 et 7,0 traçables), avant et après ajout du métabisulfite.

---

**Q18 : Comment assurez-vous la reproductibilité de vos mesures cinétiques ?**

**R :** Reproductibilité assurée par :
1. **3 expériences cinétiques indépendantes** (mêmes conditions, jours différents)
2. **Titrages en triplicat** par point temporel → moyenne et écart-type
3. **Régression linéaire** de $\ln[\text{SO}_2] = f(t)$ → $k$ avec intervalle de confiance 95 % ($k \pm t_{\text{Student}} \times u(k)$)
4. $R^2 > 0{,}99$ requis pour valider le modèle ordre 1

---

**Q19 : Quel contrôle négatif avez-vous mis en place pour distinguer réaction chimique et artefact expérimental ?**

**R :** Contrôles négatifs :
1. **Flacon fermé vs ouvert** : si décroissance identique → volatilisation négligeable
2. **Atmosphère inerte (N₂)** : si [SO₂] stable → l'oxydation par O₂ est le mécanisme dominant
3. **Solution tampon sans SO₂ dosée régulièrement** : vérifie la stabilité du blanc (absence de dérive instrumentale)
4. **Dosage immédiat à t=0** : valide la concentration initiale théorique

---

**Q20 : Pourquoi étudier plusieurs valeurs de pH ? Comment avez-vous sélectionné la gamme ?**

**R :** L'étude multi-pH est **indispensable à l'objectif d'optimisation** : quantifier l'influence du pH à la fois sur la fraction active $f$ et sur la cinétique $k$. Gamme pH 3,0–4,5 choisie car :
1. Elle couvre la plage réaliste des vins (rouges 3,3–3,7 ; blancs 3,0–3,4)
2. Elle encadre $pK_{a1}$ sans l'atteindre (hors de portée pratique)
3. Elle met en évidence des variations significatives de $f$ (facteur ~8 entre les extremes)

---

## Catégorie 5 — Liens avec le thème et enjeux

**Q21 : Comment votre travail s'inscrit-il rigoureusement dans le triptyque Optimisation / Sobriété / Efficacité ?**

**R :**
- **Optimisation** : chercher le couple (pH, $[\text{SO}_2]_{\text{total}}$) maximisant $[\text{SO}_2]_{\text{mol}}$ sous contrainte réglementaire — problème d'optimisation sous contraintes.
- **Sobriété** : réduire les sulfites répond aux enjeux sanitaires (allergies, étiquetage) et sociétaux (vins naturels). Résultat : facteur 3 à 5 de réduction en ajustant le pH.
- **Efficacité** : l'efficacité dépend non de la dose totale mais de la fraction moléculaire. Gérer finement le pH maximise cette fraction à dose constante.

---

**Q22 : Quelles sont les limites réglementaires CE n°606/2009 ? Pourquoi diffèrent-elles selon le type de vin ?**

**R :** Limites maximales en SO₂ total :

| Type | Limite |
|---|---|
| Vin rouge | **150 mg/L** |
| Vin blanc / rosé | **200 mg/L** |
| Vin liquoreux | 300–400 mg/L |
| Bio rouge / blanc | 100 / 150 mg/L |

Différences expliquées par : (1) **teneur en composés carbonylés** (blancs/liquoreux ont plus d'aldéhydes et sucres combinant le SO₂) ; (2) **protection naturelle des rouges** (tanins, polyphénols antimicrobiens) ; (3) **compromis réglementaire** entre allergénicité et nécessité technologique.

---

**Q23 : Quelles alternatives au SO₂ existent ? Quelles en sont les limites ?**

**R :**

| Alternative | Action | Limite |
|---|---|---|
| Acide sorbique | Antifongique | Inactif sur bactéries ; goûts indésirables |
| Lysozyme | Antibactérien | Aucune action antioxydante ; allergène (œuf) |
| DMDC | Stérilisant ponctuel | Pas d'action résiduelle ni antioxydante |
| Acide ascorbique | Antioxydant | Peut produire H₂O₂ sans SO₂ présent |
| Inertage N₂/CO₂ | Protection physique | Aucune action antimicrobienne |

Le SO₂ reste unique par sa **double action** (antimicrobienne + antioxydante) et son faible coût. La tendance actuelle est au **multi-barrières**.

---

**Q24 : Quelles sont les limites scientifiques de votre étude ? Comment les dépasser ?**

**R :**
1. **Matrice simplifiée** → validation sur vin synthétique standardisé puis vin réel
2. **Température unique** → répétition à 15, 20, 30°C pour calculer $E_a$ (Arrhénius)
3. **SO₂ libre uniquement** → chromatographie ionique pour distinguer SO₂ mol. / HSO₃⁻
4. **Effet microbiologique non testé** → tests de croissance de *Brettanomyces* à différentes $[\text{SO}_2]_{\text{mol}}$

---

**Q25 : Quelle recommandation pratique et chiffrée formuleriez-vous à un vigneron ?**

**R :** **Maintenir le pH entre 3,2 et 3,4** est le levier le plus efficace :

- À pH 3,2 ($f \approx 5$ %) : 16 mg/L de SO₂ total suffisent pour $[\text{SO}_2]_{\text{mol}} \geq 0{,}8$ mg/L
- À pH 3,8 ($f \approx 0{,}5$ %) : il faudrait 160 mg/L, proche de la limite réglementaire

**Recommandations pratiques** :
- Acidification tartrique si pH > 3,5
- Viser $[\text{SO}_2]_{\text{mol}} \geq 0{,}8$ mg/L (seuil antimicrobien)
- Sulfitage régulier selon $t_{1/2}$ estimé
- Minimiser les apports O₂ (élevage sous atmosphère inerte)

Cette approche réduit les sulfites de **30 à 50 %** par rapport à une pratique non optimisée.

---

*Document de préparation à l'oral TIPE — Jury simulé niveau CCP/Mines/Centrale*
*Thème : Optimisation / Sobriété / Efficacité — Session 2026*
