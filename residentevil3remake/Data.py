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
        hardcore_offset = 400 # put all hardcore-only locations after standard location spots
        nightmare_offset = 600 # put all nightmare-only locations after hardcore location spots
        inferno_offset = 800 # put all inferno-only locations in the last 100 location spots
        scenario_suffix = ' ({}{})'.format(character[0].upper(), scenario.upper())
        scenario_suffix_hardcore = ' ({}{}H)'.format(character[0].upper(), scenario.upper()) # makes hardcore location variations unique
        scenario_suffix_nightmare = ' ({}{}N)'.format(character[0].upper(), scenario.upper()) # makes nightmare location variations unique
        scenario_suffix_inferno = ' ({}{}I)'.format(character[0].upper(), scenario.upper()) # makes inferno location variations unique

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
        # Add hardcore regions, if applicable
        ###

        hardcore_locations_table = load_data_file(character, scenario, 'locations_hardcore.json')
        hardcore_regions = [loc['region'] for loc in hardcore_locations_table]

        if len(hardcore_regions) > 0:
            Data.region_table.extend([
                {
                    'name': reg + scenario_suffix_hardcore, # add the scenario abbreviation so they're unique
                    'character': character,
                    'scenario': scenario,
                    'zone_id': [regular['zone_id'] for regular in new_region_table if regular['name'] == reg][0]
                }
                for reg in hardcore_regions # instead of using region definitions, we're using the hardcore region additions from the locations themselves
            ])
            
        ###
        # Add nightmare regions, if applicable
        ###

        nightmare_locations_table = load_data_file(character, scenario, 'locations_nightmare.json')
        nightmare_regions = [loc['region'] for loc in nightmare_locations_table]

        if len(nightmare_regions) > 0:
            Data.region_table.extend([
                {
                    'name': reg + scenario_suffix_nightmare, # add the scenario abbreviation so they're unique
                    'character': character,
                    'scenario': scenario,
                    'zone_id': [regular['zone_id'] for regular in new_region_table if regular['name'] == reg][0]
                }
                for reg in nightmare_regions # instead of using region definitions, we're using the nightmare region additions from the locations themselves
            ])

        ###
        # Add inferno regions, if applicable
        ###

        inferno_locations_table = load_data_file(character, scenario, 'locations_inferno.json')
        inferno_regions = [loc['region'] for loc in inferno_locations_table]

        if len(inferno_regions) > 0:
            Data.region_table.extend([
                {
                    'name': reg + scenario_suffix_inferno, # add the scenario abbreviation so they're unique
                    'character': character,
                    'scenario': scenario,
                    'zone_id': [regular['zone_id'] for regular in new_region_table if regular['name'] == reg][0]
                }
                for reg in inferno_regions # instead of using region definitions, we're using the inferno region additions from the locations themselves
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
        # Add hardcore region connections
        ###

        # not a typo. if we loaded hardcore regions, we need to generate hardcore region connections as well
        if len(hardcore_regions) > 0:
            for conn in new_region_connections_table:
                if conn['from'] in hardcore_regions or conn['to'] in hardcore_regions:
                    suffix_from = scenario_suffix_hardcore if conn['from'] in hardcore_regions else scenario_suffix
                    suffix_to = scenario_suffix_hardcore if conn['to'] in hardcore_regions else scenario_suffix

                    new_region_connection = {
                        **conn,
                        'from': conn['from'] + suffix_from, 
                        'to': conn['to'] + suffix_to, 
                        'character': character,
                        'scenario': scenario    
                    }

                    Data.region_connections_table.append(new_region_connection)
                    
        ###
        # Add nightmare region connections
        ###

        # not a typo. if we loaded nightmare regions, we need to generate nightmare region connections as well
        if len(nightmare_regions) > 0:
            for conn in new_region_connections_table:
                if conn['from'] in nightmare_regions or conn['to'] in nightmare_regions:
                    suffix_from = scenario_suffix_nightmare if conn['from'] in nightmare_regions else scenario_suffix
                    suffix_to = scenario_suffix_nightmare if conn['to'] in nightmare_regions else scenario_suffix

                    new_region_connection = {
                        **conn,
                        'from': conn['from'] + suffix_from, 
                        'to': conn['to'] + suffix_to, 
                        'character': character,
                        'scenario': scenario    
                    }

                    Data.region_connections_table.append(new_region_connection)
        
        ###
        # Add inferno region connections
        ###

        # not a typo. if we loaded inferno regions, we need to generate inferno region connections as well
        if len(inferno_regions) > 0:
            for conn in new_region_connections_table:
                if conn['from'] in inferno_regions or conn['to'] in inferno_regions:
                    suffix_from = scenario_suffix_inferno if conn['from'] in inferno_regions else scenario_suffix
                    suffix_to = scenario_suffix_inferno if conn['to'] in inferno_regions else scenario_suffix

                    new_region_connection = {
                        **conn,
                        'from': conn['from'] + suffix_from, 
                        'to': conn['to'] + suffix_to, 
                        'character': character,
                        'scenario': scenario    
                    }

                    Data.region_connections_table.append(new_region_connection)

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

        ###
        # Add hardcore locations
        ###

        hardcore_location_table = load_data_file(character, scenario, 'locations_hardcore.json')

        if len(hardcore_location_table) > 0:
            Data.location_table.extend([
                { 
                    **loc, 
                    'id': loc['id'] if loc.get('id') else location_start + key + hardcore_offset,
                    'region': loc['region'] + scenario_suffix_hardcore, # add the scenario abbreviation so they're unique
                    'character': character,
                    'scenario': scenario,
                    'difficulty': 'hardcore'
                }
                for key, loc in enumerate(hardcore_location_table)
            ])
            
        ###
        # Add nightmare locations
        ###

        nightmare_location_table = load_data_file(character, scenario, 'locations_nightmare.json')

        if len(nightmare_location_table) > 0:
            Data.location_table.extend([
                { 
                    **loc, 
                    'id': loc['id'] if loc.get('id') else location_start + key + nightmare_offset,
                    'region': loc['region'] + scenario_suffix_nightmare, # add the scenario abbreviation so they're unique
                    'character': character,
                    'scenario': scenario,
                    'difficulty': 'nightmare'
                }
                for key, loc in enumerate(nightmare_location_table)
            ])

        ###
        # Add inferno locations
        ###

        inferno_location_table = load_data_file(character, scenario, 'locations_inferno.json')

        if len(inferno_location_table) > 0:
            Data.location_table.extend([
                { 
                    **loc, 
                    'id': loc['id'] if loc.get('id') else location_start + key + inferno_offset,
                    'region': loc['region'] + scenario_suffix_inferno, # add the scenario abbreviation so they're unique
                    'character': character,
                    'scenario': scenario,
                    'difficulty': 'inferno'
                }
                for key, loc in enumerate(inferno_location_table)
            ])
