donor_dict = \
    {
        1: 3,
        2: 6,
        3: 9,
        4: 12,
        5: 11,
        6: 8,
        7: 5,
        8: 2,
        9: 1,
        10: 4,
        11: 7,
        12: 10,
    }

cell_dict = {
    'CD68': {
        'legend': "Macrophage (CD68+)",
        'short': "CD68+",
        'group': "Immune Cells",
        'color': "gold",
        'marker': 'circle',
        'size': 15.89,
        'histogram_location': [3, 1],
    },
    'CD31': {
        'legend': "Endothelial cells (CD31)",
        'short': "CD31",
        'group': 'Vessel & Skin',
        'color': "red",
        'marker': 'circle',
        'size': 16.83,
        'histogram_location': [0, 0],
    },
    'T-Helper': {
        'legend': "T-Helper Cells (CD4)",
        'short': "T-Helper",
        'group': "Immune Cells",
        'color': "blue",
        'marker': 'circle',
        'size': 16.96,
        'histogram_location': [2, 2],
    },
    'T-Reg': {
        'legend': "T-Regulatory Cells (FOXP3)",
        'short': "T-Reg",
        'group': "Immune Cells",
        'color': "mediumspringgreen",
        'marker': 'circle',
        'size': 17.75,
        'histogram_location': [2, 3],
    },
    'T-Killer': {
        'legend': "T-Killer Cells (CD8)",
        'short': "T-Killer",
        'group': "Immune Cells",
        'color': "purple",
        'marker': 'circle',
        'size': 16,
        'histogram_location': [2, 4],
    },
    'P53': {
        'legend': "P53",
        'short': "P53",
        'group': "UV Damage",
        'color': "chocolate",
        'marker': 'cross',
        'size': 16,
        'histogram_location': [3, 2],
    },
    'KI67': {
        'legend': "KI67",
        'short': "KI67",
        'group': 'Proliferation',
        'color': "cyan",
        'marker': 'cross',
        'size': 16,
        'histogram_location': [3, 3],
    },
    'DDB2': {
        'legend': "DDB2",
        'short': "DDB2",
        'group': "UV Damage",
        'color': "olivedrab",
        'marker': 'cross',
        'size': 16,
        'histogram_location': [3, 4],
    },
    'Skin': {
        'legend': "Skin Surface",
        'short': "Skin",
        'group': 'Vessel & Skin',
        'color': "darkgrey",
        'marker': 'diamond',
        'size': 5,
        'histogram_location': [0, 0],
    },
}

cell_dict['Macrophage'] = cell_dict['CD68']
cell_dict['Blood Vessel'] = cell_dict['CD31']
cell_dict['T-Regulatory'] = cell_dict['T-Reg']
cell_dict['T-Regulator'] = cell_dict['T-Reg']
