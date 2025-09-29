# 🩺 Data Analysis Project – Nutrition & Atherosclerosis

## 📌 Description du projet
Ce projet explore la relation entre l’alimentation et les résultats de santé, en se concentrant sur l’**athérosclérose**, une maladie chronique liée aux habitudes alimentaires.  
L’objectif est d’analyser des données patients (paramètres biométriques, résultats médicaux, régimes appliqués, scores post-régimes) afin de développer des **modèles prédictifs**, réaliser des **analyses statistiques** et proposer des **recommandations nutritionnelles personnalisées**.

---

## 📂 Structure du projet
- **`data/`** : Contient les fichiers CSV fournis :
  - `Anonymized_Patient_Parameters_Atherosclerosis.csv` → paramètres démographiques et physiques.
  - `Anonymized_Test_Results_Atherosclerosis.csv` → résultats des tests médicaux initiaux.
  - `Nutritional_Values_Applied_Diet_Atherosclerosis.csv` → valeurs nutritionnelles des régimes appliqués.
  - `Scoring_Results_After_Applying_Diet_Atherosclerosis.csv` → résultats après application des régimes.
- **`notebooks/`** : Notebooks Jupyter pour les analyses exploratoires, tests statistiques et modélisations.
- **`figures/`** : Visualisations et graphiques générés.

---

## 🎯 Sujets et objectifs

### 1️⃣ Modèle Prédictif Multimodal du Risque d’Athérosclérose
- Objectif : prédire le risque (haut/faible) en combinant données démographiques, biologiques, nutritionnelles et résultats post-régimes.
- Méthodes : Feature engineering (IMC, catégories de régimes), Random Forest, XGBoost, Stacking Classifier.

### 2️⃣ Analyse d’Impact des Régimes sur le LDL
- Objectif : comparer l’efficacité des régimes sur la réduction du LDL (avant/après).
- Méthodes : Tests statistiques (ANOVA, t-test), régression linéaire multivariée, visualisations.

### 3️⃣ Clustering des Patients par Profil de Risque
- Objectif : grouper les patients en sous-types (ex : “jeunes avec LDL élevé mais bonne réponse aux régimes méditerranéens”).
- Méthodes : K-means, GMM, silhouette score, analyse des nutriments dominants.

### 4️⃣ Système de Recommandation Hybride
- Objectif : recommander un régime personnalisé basé sur similarité patient + contenu nutritionnel.
- Méthodes : Similarité cosinus, LightFM (collaboratif + content-based).

### 5️⃣ Détection des Patients “Non-Répondeurs”
- Objectif : identifier les patients dont le LDL ne diminue pas malgré un régime.
- Méthodes : Classification (SVM, Isolation Forest), détection de carences nutritionnelles.

---

## ⚙️ Méthodologie
1. **Prétraitement des données** : nettoyage, normalisation, jointure via `case,XXX`.
2. **Exploration** : statistiques descriptives, corrélations, visualisations.
3. **Analyse statistique** : tests paramétriques et non-paramétriques.
4. **Machine Learning** :
   - Modèles supervisés (classification)
   - Modèles non supervisés (clustering)
   - Recommandation hybride
5. **Validation** : cross-validation, métriques cliniques (sensibilité, spécificité, AUC).
6. **Interprétation médicale** : mise en relation des résultats avec la littérature scientifique.

---

## 📊 Cas d’utilisation
- **Recherche médicale** : impact de l’alimentation sur la santé cardiovasculaire.
- **IA & santé** : entraînement de modèles prédictifs multimodaux.
- **Nutrition appliquée** : étude comparative de régimes (méditerranéen, DASH, etc.).

---

## 💻 Technologies utilisées
- **Langage** : Python 3.x  
- **Librairies principales** :
  - `pandas`, `numpy` → manipulation de données
  - `matplotlib`, `seaborn` → visualisations
  - `scikit-learn` → machine learning (classification, clustering, métriques)
  - `xgboost`, `lightfm` → modèles avancés
  - `scipy`, `statsmodels` → tests statistiques
  - `jupyter` → notebooks interactifs

---

## 📦 Installation
1. Cloner le projet :
   ```bash
   git clone https://github.com/<username>/nutrition-atherosclerosis-analysis.git
   cd nutrition-atherosclerosis-analysis

