import re


'''
Stupid EnergyPLAN's output format is ridiculous and so is the input: the format of the keys is SO inconsistent.
I spent some hours extracting by hand the correct associations between UI field and abbreviation in the the input
file (the `keys` array below) because nothing is documented anywhere. This script extracts from a sample input
file the correct spelling of these keys and prints them in a format that can be copy-pasted into input_gen.py.
You'll notice in the output that sometimes the words "input" and "inv" are spelled with a capital letter, sometimes not.

Wow. Just. Wow.
'''


f = open('/home/alex/Data/GDrive/Unitn/PhD/EnergyPLAN/8.SUANFARMA/0.Tests/nat-cool-test-input.txt', 'r', encoding='utf-16').read()


### Keys for the costs tab / Heat and Electricity
keys = ['CHP2', 'CHP3', 'Heatstorage2', 'Waste_CHP', 'absorp_HP', 'HP2', 'HP3', 'Boilers_dh_gr1', 'Boilers_dh', 'EHgr2gr3', 'PP', 'Nuclear', 'Interconnection', 'Pump', 'Turbine', 'PumpStorage', 'pump2', 'turbine2', 'PumpStorage2', 'ind_CHP_elec', 'ind_CHP_heat', 'SteamStorage']

print('{')
for abbr in keys:
    inv = re.search('(input_Inv_%s)\s*=\s*\d+' % abbr, f, re.IGNORECASE).group(1)
    years = re.search('(input_Period_%s)\s*=\s*\d+' % abbr, f, re.IGNORECASE).group(1)
    fom = re.search('(input_FOM_%s)\s*=\s*\d+' % abbr, f, re.IGNORECASE).group(1)
    print("  '%s': {'Inv': '%s', 'Years': '%s', 'FOM': '%s'}," % (abbr, inv, years, fom))
print('}')