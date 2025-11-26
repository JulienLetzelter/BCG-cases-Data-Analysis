# BCG Cases Data Analysis

Analyse et prédiction du rendement d'orge en France à partir de données climatiques et géographiques.

## Installation

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Configuration requise

**Important** : Le fichier `climate_data_from_1982.parquet` doit être ajouté manuellement dans le dossier `raw_data/`. Ce fichier est trop volumineux pour être versionné sur Git. Sans ce fichier, les notebooks ne pourront pas s'exécuter correctement.

## Structure du projet

### Notebooks d'analyse

- **`data_description_yield.ipynb`** : Analyse descriptive des données de rendement d'orge par département français (1982-2018). Visualisations temporelles, distributions statistiques et cartes géographiques.

- **`model.ipynb`** : Construction d'un modèle de prédiction du rendement d'orge utilisant des features climatiques (périodes hivernale, élongation de la tige, remplissage du grain) et géographiques. Génère les prédictions pour 2019-2050.

- **`map_barley_yield_2040.ipynb`** : Visualisation cartographique interactive des prédictions de rendement d'orge pour l'année 2040 par département.

### Données

- **`raw_data/`** : Dossier contenant les données brutes
  - `barley_yield_from_1982.csv` : Données de rendement d'orge corrigées (générées par `data_correction.py`)
  - `climate_data_from_1982.parquet` : Données climatiques (à ajouter manuellement)
  - `original_data/barley_yield_from_1982.csv` : Données originales de rendement
  - `data_correction.py` : Script de correction des données (ajout des numéros de départements, calcul des rendements manquants)

- **`data_model_prediction/`** : Prédictions générées par le modèle
  - `predictions_yield_2019_2050.csv` : Prédictions de rendement pour 2019-2050, ce fichier est generé à partir du notebook 'model.ipynb'

### Utilitaires

- **`utils/department_info.py`** : Module contenant les informations sur les départements français (numéros, coordonnées géographiques, régions). Utilisé par les notebooks et le script de correction.

## Workflow

1. Ajouter le fichier `climate_data_from_1982.parquet` dans `raw_data/`
2. Exécuter `raw_data/data_correction.py` pour générer les données corrigées (si nécessaire)
3. Exécuter `data_description_yield.ipynb` pour l'analyse descriptive
4. Exécuter `model.ipynb` pour entraîner le modèle et générer les prédictions
5. Exécuter `map_barley_yield_2040.ipynb` pour visualiser les prédictions sur carte

