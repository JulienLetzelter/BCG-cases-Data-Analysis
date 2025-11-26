"""
Informations sur les départements français
Contient les numéros de départements, leurs coordonnées géographiques et leurs régions
"""

# Mapping des noms de départements vers leurs numéros
# Source: data_correction.py
DEPARTMENT_NUMBERS = {
    'Ain': '01',
    'Aisne': '02',
    'Allier': '03',
    'Alpes_de_Haute_Provence': '04',
    'Hautes_Alpes': '05',
    'Alpes_Maritimes': '06',
    'Ardeche': '07',
    'Ardennes': '08',
    'Ariege': '09',
    'Aube': '10',
    'Aude': '11',
    'Aveyron': '12',
    'Bouches_du_Rhone': '13',
    'Calvados': '14',
    'Cantal': '15',
    'Charente': '16',
    'Charente_Maritime': '17',
    'Cher': '18',
    'Correze': '19',
    'Corse_du_Sud': '2A',
    'Haute_Corse': '2B',
    'Cote_d_Or': '21',
    'Cotes_d_Armor': '22',
    'Creuse': '23',
    'Dordogne': '24',
    'Doubs': '25',
    'Drome': '26',
    'Eure': '27',
    'Eure_et_Loir': '28',
    'Finistere': '29',
    'Gard': '30',
    'Haute_Garonne': '31',
    'Gers': '32',
    'Gironde': '33',
    'Herault': '34',
    'Ille_et_Vilaine': '35',
    'Indre': '36',
    'Indre_et_Loire': '37',
    'Isere': '38',
    'Jura': '39',
    'Landes': '40',
    'Loir_et_Cher': '41',
    'Loire': '42',
    'Haute_Loire': '43',
    'Loire_Atlantique': '44',
    'Loiret': '45',
    'Lot': '46',
    'Lot_et_Garonne': '47',
    'Lozere': '48',
    'Maine_et_Loire': '49',
    'Manche': '50',
    'Marne': '51',
    'Haute_Marne': '52',
    'Mayenne': '53',
    'Meurthe_et_Moselle': '54',
    'Meuse': '55',
    'Morbihan': '56',
    'Moselle': '57',
    'Nievre': '58',
    'Nord': '59',
    'Oise': '60',
    'Orne': '61',
    'Pas_de_Calais': '62',
    'Puy_de_Dome': '63',
    'Pyrenees_Atlantiques': '64',
    'Hautes_pyrenees': '65',
    'Pyrenees_Orientales': '66',
    'Bas_Rhin': '67',
    'Haut_Rhin': '68',
    'Rhone': '69',
    'Haute_Saone': '70',
    'Saone_et_Loire': '71',
    'Sarthe': '72',
    'Savoie': '73',
    'Haute_Savoie': '74',
    'Paris': '75',
    'Seine_Maritime': '76',
    'Seine_et_Marne': '77',
    'Yvelines': '78',
    'Deux_Sevres': '79',
    'Somme': '80',
    'Tarn': '81',
    'Tarn_et_Garonne': '82',
    'Var': '83',
    'Vaucluse': '84',
    'Vendee': '85',
    'Vienne': '86',
    'Haute_Vienne': '87',
    'Vosges': '88',
    'Yonne': '89',
    'Territoire_de_Belfort': '90',
    'Essonne': '91',
    'Hauts_de_Seine': '92',
    'Seine_Saint_Denis': '93',
    'Val_de_Marne': '94',
    'Val_d_Oise': '95',
}

# Mapping des numéros de départements vers leurs coordonnées (latitude, longitude)
# Source: model.ipynb - coordonnées approximatives des chefs-lieux de départements
DEPARTMENT_COORDINATES = {
    '01': (46.2043, 5.2266),  # Ain - Bourg-en-Bresse
    '02': (49.4431, 3.4109),  # Aisne - Laon
    '03': (46.3448, 3.4446),  # Allier - Moulins
    '04': (44.0925, 6.2357),  # Alpes-de-Haute-Provence - Digne-les-Bains
    '05': (44.5592, 6.0784),  # Hautes-Alpes - Gap
    '06': (43.7102, 7.2620),  # Alpes-Maritimes - Nice
    '07': (44.9333, 4.3833),  # Ardèche - Privas
    '08': (49.7708, 4.7194),  # Ardennes - Charleville-Mézières
    '09': (42.9600, 1.6000),  # Ariège - Foix
    '10': (48.2978, 4.0783),  # Aube - Troyes
    '11': (43.2131, 2.3522),  # Aude - Carcassonne
    '12': (44.3494, 2.5750),  # Aveyron - Rodez
    '13': (43.2965, 5.3698),  # Bouches-du-Rhône - Marseille
    '14': (49.1829, -0.3707),  # Calvados - Caen
    '15': (45.0333, 2.8833),  # Cantal - Aurillac
    '16': (45.6500, 0.1500),  # Charente - Angoulême
    '17': (46.1591, -1.1520),  # Charente-Maritime - La Rochelle
    '18': (47.0833, 2.4000),  # Cher - Bourges
    '19': (45.2667, 1.7667),  # Corrèze - Tulle
    '2A': (41.9267, 8.7369),  # Corse-du-Sud - Ajaccio
    '2B': (42.6999, 9.4500),  # Haute-Corse - Bastia
    '21': (47.3220, 5.0415),  # Côte-d'Or - Dijon
    '22': (48.4534, -2.7266),  # Côtes-d'Armor - Saint-Brieuc
    '23': (46.1700, 1.8700),  # Creuse - Guéret
    '24': (45.1833, 0.7167),  # Dordogne - Périgueux
    '25': (47.2378, 6.0244),  # Doubs - Besançon
    '26': (44.9333, 4.8833),  # Drôme - Valence
    '27': (49.0236, 1.1500),  # Eure - Évreux
    '28': (48.4439, 1.4881),  # Eure-et-Loir - Chartres
    '29': (48.3904, -4.4860),  # Finistère - Quimper
    '30': (44.1333, 4.0833),  # Gard - Nîmes
    '31': (43.6047, 1.4442),  # Haute-Garonne - Toulouse
    '32': (43.6458, 0.5875),  # Gers - Auch
    '33': (44.8378, -0.5792),  # Gironde - Bordeaux
    '34': (43.6109, 3.8767),  # Hérault - Montpellier
    '35': (48.1147, -1.6794),  # Ille-et-Vilaine - Rennes
    '36': (46.8167, 1.6833),  # Indre - Châteauroux
    '37': (47.3941, 0.6847),  # Indre-et-Loire - Tours
    '38': (45.1885, 5.7245),  # Isère - Grenoble
    '39': (46.6756, 5.5531),  # Jura - Lons-le-Saunier
    '40': (43.8927, -1.0067),  # Landes - Mont-de-Marsan
    '41': (47.5833, 1.3333),  # Loir-et-Cher - Blois
    '42': (45.4333, 4.3833),  # Loire - Saint-Étienne
    '43': (45.0500, 3.8833),  # Haute-Loire - Le Puy-en-Velay
    '44': (47.2173, -1.5534),  # Loire-Atlantique - Nantes
    '45': (47.9022, 1.9042),  # Loiret - Orléans
    '46': (44.4500, 1.4333),  # Lot - Cahors
    '47': (44.2000, 0.6167),  # Lot-et-Garonne - Agen
    '48': (44.5167, 3.5000),  # Lozère - Mende
    '49': (47.4733, -0.5517),  # Maine-et-Loire - Angers
    '50': (49.1197, -1.0903),  # Manche - Saint-Lô
    '51': (49.2539, 4.0347),  # Marne - Châlons-en-Champagne
    '52': (48.1100, 5.1400),  # Haute-Marne - Chaumont
    '53': (48.0667, -0.7667),  # Mayenne - Laval
    '54': (48.6928, 6.1844),  # Meurthe-et-Moselle - Nancy
    '55': (49.1333, 5.3833),  # Meuse - Bar-le-Duc
    '56': (47.7461, -2.7603),  # Morbihan - Vannes
    '57': (49.1197, 6.1758),  # Moselle - Metz
    '58': (47.0000, 3.1500),  # Nièvre - Nevers
    '59': (50.6292, 3.0573),  # Nord - Lille
    '60': (49.4431, 2.8267),  # Oise - Beauvais
    '61': (48.4300, 0.0900),  # Orne - Alençon
    '62': (50.2906, 2.7819),  # Pas-de-Calais - Arras
    '63': (45.7772, 3.0870),  # Puy-de-Dôme - Clermont-Ferrand
    '64': (43.2951, -0.3708),  # Pyrénées-Atlantiques - Pau
    '65': (43.2333, 0.0667),  # Hautes-Pyrénées - Tarbes
    '66': (42.6976, 2.8954),  # Pyrénées-Orientales - Perpignan
    '67': (48.5734, 7.7521),  # Bas-Rhin - Strasbourg
    '68': (47.7500, 7.3333),  # Haut-Rhin - Colmar
    '69': (45.7640, 4.8357),  # Rhône - Lyon
    '70': (47.6333, 6.0333),  # Haute-Saône - Vesoul
    '71': (46.3075, 4.8306),  # Saône-et-Loire - Mâcon
    '72': (48.0020, 0.1996),  # Sarthe - Le Mans
    '73': (45.5667, 5.9167),  # Savoie - Chambéry
    '74': (46.2043, 6.1432),  # Haute-Savoie - Annecy
    '75': (48.8566, 2.3522),  # Paris - Paris
    '76': (49.4431, 1.0993),  # Seine-Maritime - Rouen
    '77': (48.9569, 2.6289),  # Seine-et-Marne - Melun
    '78': (48.8014, 2.1301),  # Yvelines - Versailles
    '79': (46.3237, -0.4647),  # Deux-Sèvres - Niort
    '80': (49.8942, 2.2958),  # Somme - Amiens
    '81': (43.9294, 2.1481),  # Tarn - Albi
    '82': (44.0167, 1.3500),  # Tarn-et-Garonne - Montauban
    '83': (43.1242, 6.0745),  # Var - Toulon
    '84': (44.0556, 5.0481),  # Vaucluse - Avignon
    '85': (46.6702, -1.4275),  # Vendée - La Roche-sur-Yon
    '86': (46.5802, 0.3404),  # Vienne - Poitiers
    '87': (45.8333, 1.2500),  # Haute-Vienne - Limoges
    '88': (48.1733, 6.4519),  # Vosges - Épinal
    '89': (47.7974, 3.5687),  # Yonne - Auxerre
    '90': (47.6333, 6.8667),  # Territoire de Belfort - Belfort
    '91': (48.6300, 2.3000),  # Essonne - Évry
    '92': (48.8406, 2.2531),  # Hauts-de-Seine - Nanterre
    '93': (48.9352, 2.3530),  # Seine-Saint-Denis - Bobigny
    '94': (48.7872, 2.4033),  # Val-de-Marne - Créteil
    '95': (49.0889, 2.1319),  # Val-d'Oise - Pontoise
}

# Mapping des régions vers leurs départements
# Utilise les noms de départements du format DEPARTMENT_NUMBERS
REGIONS = {
    'Auvergne-Rhône-Alpes': ['Ain', 'Allier', 'Ardeche', 'Cantal', 'Drome', 'Isere', 'Loire', 'Haute_Loire', 'Puy_de_Dome', 'Rhone', 'Savoie', 'Haute_Savoie'],
    'Bourgogne-Franche-Comté': ['Cote_d_Or', 'Doubs', 'Jura', 'Nievre', 'Haute_Saone', 'Saone_et_Loire', 'Yonne', 'Territoire_de_Belfort'],
    'Bretagne': ['Cotes_d_Armor', 'Finistere', 'Ille_et_Vilaine', 'Morbihan'],
    'Centre-Val de Loire': ['Cher', 'Eure_et_Loir', 'Indre', 'Indre_et_Loire', 'Loir_et_Cher', 'Loiret'],
    'Corse': ['Corse_du_Sud', 'Haute_Corse'],
    'Grand Est': ['Ardennes', 'Aube', 'Marne', 'Haute_Marne', 'Meurthe_et_Moselle', 'Meuse', 'Moselle', 'Bas_Rhin', 'Haut_Rhin', 'Vosges'],
    'Hauts-de-France': ['Aisne', 'Nord', 'Oise', 'Pas_de_Calais', 'Somme'],
    'Île-de-France': ['Paris', 'Seine_et_Marne', 'Yvelines', 'Essonne', 'Hauts_de_Seine', 'Seine_Saint_Denis', 'Val_de_Marne', 'Val_d_Oise'],
    'Normandie': ['Calvados', 'Eure', 'Manche', 'Orne', 'Seine_Maritime'],
    'Nouvelle-Aquitaine': ['Charente', 'Charente_Maritime', 'Correze', 'Creuse', 'Dordogne', 'Gironde', 'Landes', 'Lot_et_Garonne', 'Pyrenees_Atlantiques', 'Deux_Sevres', 'Vienne', 'Haute_Vienne'],
    'Occitanie': ['Ariege', 'Aude', 'Aveyron', 'Gard', 'Haute_Garonne', 'Gers', 'Herault', 'Lot', 'Lozere', 'Hautes_pyrenees', 'Pyrenees_Orientales', 'Tarn', 'Tarn_et_Garonne'],
    'Pays de la Loire': ['Loire_Atlantique', 'Maine_et_Loire', 'Mayenne', 'Sarthe', 'Vendee'],
    'Provence-Alpes-Côte d\'Azur': ['Alpes_de_Haute_Provence', 'Hautes_Alpes', 'Alpes_Maritimes', 'Bouches_du_Rhone', 'Var', 'Vaucluse']
}

# Mapping inverse: département -> région
DEPARTMENT_TO_REGION = {}
for region, departments in REGIONS.items():
    for dept in departments:
        DEPARTMENT_TO_REGION[dept] = region


def get_department_number(department_name):
    """
    Retourne le numéro de département à partir de son nom.
    
    Args:
        department_name (str): Nom du département
        
    Returns:
        str: Numéro du département ou None si non trouvé
    """
    return DEPARTMENT_NUMBERS.get(department_name)


def get_department_coordinates(department_number):
    """
    Retourne les coordonnées (latitude, longitude) d'un département à partir de son numéro.
    
    Args:
        department_number (str): Numéro du département
        
    Returns:
        tuple: (latitude, longitude) ou None si non trouvé
    """
    return DEPARTMENT_COORDINATES.get(str(department_number).zfill(2) if len(str(department_number)) == 1 else str(department_number))


def get_coordinates_by_name(department_name):
    """
    Retourne les coordonnées (latitude, longitude) d'un département à partir de son nom.
    
    Args:
        department_name (str): Nom du département
        
    Returns:
        tuple: (latitude, longitude) ou None si non trouvé
    """
    dept_num = get_department_number(department_name)
    if dept_num:
        return get_department_coordinates(dept_num)
    return None


def get_department_region(department_name):
    """
    Retourne la région d'un département à partir de son nom.
    
    Args:
        department_name (str): Nom du département
        
    Returns:
        str: Nom de la région ou None si non trouvé
    """
    return DEPARTMENT_TO_REGION.get(department_name)


def get_region_departments(region_name):
    """
    Retourne la liste des départements d'une région.
    
    Args:
        region_name (str): Nom de la région
        
    Returns:
        list: Liste des noms de départements ou None si région non trouvée
    """
    return REGIONS.get(region_name)


# Dictionnaire combiné: nom de département -> (numéro, latitude, longitude, région)
DEPARTMENT_INFO = {
    name: {
        'number': num,
        'latitude': DEPARTMENT_COORDINATES.get(num, (None, None))[0] if num else None,
        'longitude': DEPARTMENT_COORDINATES.get(num, (None, None))[1] if num else None,
        'region': DEPARTMENT_TO_REGION.get(name)
    }
    for name, num in DEPARTMENT_NUMBERS.items()
}

