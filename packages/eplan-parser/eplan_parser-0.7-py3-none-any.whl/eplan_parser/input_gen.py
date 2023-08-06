#!/usr/bin/env python3

from typing import List, Tuple


'''
    This wonderful list cannot be generated automatically because the input file is a mess. Some letters are capital and some are not.
    See get_keys.py for more info.
'''
key_map = {
  'CHP2':            {'Inv': 'input_Inv_CHP2', 'Years': 'input_Period_CHP2', 'FOM': 'input_FOM_CHP2'},
  'CHP3':            {'Inv': 'input_Inv_CHP3', 'Years': 'input_Period_CHP3', 'FOM': 'input_FOM_CHP3'},
  'Heatstorage2':    {'Inv': 'input_Inv_Heatstorage2', 'Years': 'input_Period_Heatstorage2', 'FOM': 'input_FOM_Heatstorage2'},
  'Waste_CHP':       {'Inv': 'input_Inv_Waste_CHP', 'Years': 'input_Period_Waste_CHP', 'FOM': 'input_FOM_Waste_CHP'},
  'absorp_HP':       {'Inv': 'input_Inv_absorp_HP', 'Years': 'input_Period_absorp_HP', 'FOM': 'input_FOM_absorp_HP'},
  'HP2':             {'Inv': 'input_Inv_HP2', 'Years': 'input_Period_HP2', 'FOM': 'input_FOM_HP2'},
  'HP3':             {'Inv': 'input_Inv_HP3', 'Years': 'input_Period_HP3', 'FOM': 'input_FOM_HP3'},
  'Boilers_dh_gr1':  {'Inv': 'input_Inv_Boilers_dh_gr1', 'Years': 'input_Period_Boilers_dh_gr1', 'FOM': 'input_FOM_Boilers_dh_gr1'},
  'Boilers_dh':      {'Inv': 'input_Inv_Boilers_dh', 'Years': 'input_Period_Boilers_dh', 'FOM': 'input_FOM_Boilers_dh'},
  'EHgr2gr3':        {'Inv': 'input_Inv_EHgr2gr3', 'Years': 'input_Period_EHgr2gr3', 'FOM': 'input_FOM_EHgr2gr3'},
  'PP':              {'Inv': 'input_Inv_PP', 'Years': 'input_Period_PP', 'FOM': 'input_FOM_PP'},
  'Nuclear':         {'Inv': 'input_Inv_Nuclear', 'Years': 'input_Period_Nuclear', 'FOM': 'input_FOM_Nuclear'},
  'Interconnection': {'Inv': 'Input_inv_Interconnection', 'Years': 'Input_Period_Interconnection', 'FOM': 'Input_FOM_Interconnection'},
  'Pump':            {'Inv': 'input_Inv_Pump', 'Years': 'input_Period_Pump', 'FOM': 'input_FOM_Pump'},
  'Turbine':         {'Inv': 'input_Inv_Turbine', 'Years': 'input_Period_Turbine', 'FOM': 'input_FOM_Turbine'},
  'PumpStorage':     {'Inv': 'input_Inv_PumpStorage', 'Years': 'input_Period_PumpStorage', 'FOM': 'input_FOM_PumpStorage'},
  'pump2':           {'Inv': 'input_Inv_pump2', 'Years': 'input_Period_pump2', 'FOM': 'input_FOM_pump2'},
  'turbine2':        {'Inv': 'input_Inv_turbine2', 'Years': 'input_Period_turbine2', 'FOM': 'input_FOM_turbine2'},
  'PumpStorage2':    {'Inv': 'input_Inv_PumpStorage2', 'Years': 'input_Period_PumpStorage2', 'FOM': 'input_FOM_PumpStorage2'},
  'ind_CHP_elec':    {'Inv': 'Input_Inv_ind_CHP_elec', 'Years': 'Input_Period_ind_CHP_elec', 'FOM': 'Input_FOM_ind_CHP_elec'},
  'ind_CHP_heat':    {'Inv': 'Input_Inv_ind_CHP_heat', 'Years': 'Input_Period_ind_CHP_heat', 'FOM': 'Input_FOM_ind_CHP_heat'},
  'SteamStorage':    {'Inv': 'input_Inv_SteamStorage', 'Years': 'input_Period_SteamStorage', 'FOM': 'input_FOM_SteamStorage'},
}


def parse_input_file(fname: str) -> List[Tuple[str, str]]:
    lines = [l.strip() for l in open(fname, 'r', encoding='utf-16')]
    res = []

    for i in range(len(lines)):
        l = lines[i]
        if l == 'EnergyPLAN version' or l.endswith('='):
            res.append((l, lines[i+1]))

    return res


def gen_input_file(base_fname: str, new_fname: str, change_set: dict[str, str]):
    base_data = parse_input_file(base_fname)
    new_data = open(new_fname, 'w', encoding='utf-16')

    for key, val in base_data:
        if key in change_set:
            new_data.write(key + '\n')
            new_data.write(change_set[key] + '\n')
        else:
            new_data.write(key + '\n')
            new_data.write(val + '\n')
    
    new_data.close()
