import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# most abundant specie list from Kerosene combustion
species_list = ["CO", "CO2", "H", "H2", "H2O", "O", "OH", "O2"]  # major components in the exhaust
mol_weights_list = [28, 44, 1, 2, 18, 16, 17, 32]  # molecular weights of components in g/mol

# combustio product abundance list according to Combustion Model of Supersonic Rocket Exhausts in an Entrained Flow Enclosure
abundance_list = [0.29, 0.16, 0.023, 0.069, 0.34, 0.012, 0.066, 0.022]  # composition in combustion chamber

abundance_list_throat = [0.2898, 0.1828, 0.02, 0.067, 0.356, 0.009, 0.056, 0.0189]  # composition at the throat

abundance_list_exit = [0.235, 0.271, 0.00072, 0.0765, 0.41627, 0.00, 0.00048, 0.00001]  # composition at the nozzle exit

data_dict = {"specie": species_list, "mol_weight": mol_weights_list, "abundance": abundance_list}

medium_df = pd.DataFrame(data_dict)
medium_df = medium_df.set_index("specie")

mixture_cp_T = 100 * np.arange(1, 41)  # temperature range to calculate mixture Cp from weighted individual Cp

component_cp_df = pd.DataFrame({'T': mixture_cp_T})

weighted_mol_weight = 0

# generate dataframe with cp values of combustion components from janaf data
for chemical in medium_df.index:
    readout_df = pd.read_csv('../data/'+chemical + '.txt', sep="\t", skiprows=1)
    component_cp_df[chemical] = readout_df['Cp']
    weighted_mol_weight = weighted_mol_weight + medium_df.loc[chemical]["mol_weight"] * medium_df.loc[chemical][
        "abundance"]

print(f"weighted molecular weight {weighted_mol_weight} AMU")

component_cp_df = component_cp_df.set_index('T')
# print(component_cp_df)
component_cp_df['mix_mol'] = np.zeros(len(component_cp_df.index))

for t_curr in component_cp_df.index:
    cp_curr = 0
    for chemical in medium_df.index:
        cp_curr = cp_curr + component_cp_df.loc[t_curr][chemical] * medium_df.loc[chemical]['abundance']
    component_cp_df.loc[t_curr]['mix_mol'] = cp_curr
component_cp_df['mix_kg'] = component_cp_df['mix_mol'] / (weighted_mol_weight * 1e-3)

# print(component_cp_df)

polyfit = np.polyfit(mixture_cp_T, component_cp_df['mix_kg'], 5) # generate 5-th order polynomial fit

Cp_fitted = np.polyval(polyfit, mixture_cp_T) # generate fitted values of Cp using polynomial coefficients
errors = (component_cp_df['mix_kg'] - Cp_fitted) / component_cp_df['mix_kg'] # calculate relative fit errors
# print(errors)
poly_flipped = np.flip(polyfit) # flip order of polynomial coefficients to match OpenFOAM expected format
poly_arr = np.array(poly_flipped)/(8.31/(weighted_mol_weight*1e-3))

print(f'polynomial fit in coeeficients in OpenFOAM notation {poly_arr}' )

#---------------- plot CP vs temperature and its fit to assess data quality -------------------

font = {'family': 'DejaVu Sans',
        'weight': 'normal',
        'size': 16}

matplotlib.rc('font', **font)

plt.plot(mixture_cp_T, component_cp_df['mix_kg'])  # Small corrector coil, G
plt.plot(mixture_cp_T, Cp_fitted)

plt.title(f'Combustion products Cp and its polynomial fit, mean mol weight {weighted_mol_weight:.2f} g/mol')
plt.xlim(left=0)  # set up lower y-axis limit at zero
plt.xlim(right=4000)

plt.xlabel('T, [K]')
plt.ylabel('Cp, [J/Kkg]')
plt.show()
