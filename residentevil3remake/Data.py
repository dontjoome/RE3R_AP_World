import json
import os
import pkgutil

# blatantly copied from the minecraft ap world because why not
def load_data_file(*args) -> dict:
    data_directory = "data"
    fname = os.path.join(data_directory, *args)

    try:
        filedata = json.loads(pkgutil.get_data(__name__, fname).decode())
    except:
        filedata = []

    return filedata

class Data:
    item_table = []
    location_table = []
    region_table = []
    region_connections_table = []

    item_name_groups = {}

    def load_data(character, scenario):
        character_offsets = { 'jill': 0 }        
        scenario_offsets = { 'a': 0 }
        scenario_suffix = ' ({}{})'.format(character[0].upper(), scenario.upper())

        location_start = item_start = 3300000000 + character_offsets[character] + scenario_offsets[scenario]

        ###
        # Add standard regions
        ###

        new_region_table = load_data_file(character, scenario, 'regions.json')
        Data.region_table.extend([
            {
                **reg,
                'name': reg['name'] + scenario_suffix if reg['name'] != 'Menu' else reg['name'], # add the scenario abbreviation so they're unique
                'character': character,
                'scenario': scenario
            }
            for reg in new_region_table
        ])

        ###
        # Add standard region connections
        ###
            
        new_region_connections_table = load_data_file(character, scenario, 'region_connections.json')
        Data.region_connections_table.extend([
            {
                **conn,
                'from': conn['from'] + scenario_suffix if conn['from'] != 'Menu' else conn['from'], # add the scenario abbreviation so they're unique
                'to': conn['to'] + scenario_suffix if conn['to'] != 'Menu' else conn['to'], # add the scenario abbreviation so they're unique
                'character': character,
                'scenario': scenario
            }
            for conn in new_region_connections_table
        ])

        ###
        # Add item table for all difficulties
        ###
        
        new_item_table = load_data_file(character, 'items.json')
        Data.item_table.extend([
            { 
                **item, 
                'id': item['id'] if item.get('id') else item_start + key
            } 
            for key, item in enumerate(new_item_table)
        ])

        # For the items that have groups, add them to the item group names
        new_items_with_groups = [item for _, item in enumerate(new_item_table) if "groups" in item.keys()]

        for item_with_group in new_items_with_groups:
            item_name = item_with_group["name"]
            group_names = item_with_group["groups"]

            for group_name in group_names:
                if group_name not in Data.item_name_groups.keys():
                    Data.item_name_groups[group_name] = []

                Data.item_name_groups[group_name].append(item_name)

        ###
        # Add standard location table
        ###

        new_location_table = load_data_file(character, scenario, 'locations.json')
        Data.location_table.extend([
            { 
                **loc, 
                'id': loc['id'] if loc.get('id') else location_start + key,
                'region': loc['region'] + scenario_suffix, # add the scenario abbreviation so they're unique
                'character': character,
                'scenario': scenario,
                'difficulty': None
            }
            for key, loc in enumerate(new_location_table)
        ])
