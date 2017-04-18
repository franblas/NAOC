
import json
from lxml import etree

def xml_to_json_script(xml_filepath, obj, main_key, new_filepath):
    tree = etree.parse(xml_filepath)

    regions = tree.findall(obj)

    final_doc = {
        main_key: []
    }

    print len(regions)

    for region in regions:
        childrens = region.getchildren()
        d = dict()
        for children in childrens:
            d[children.tag] = children.text
        final_doc[main_key].append(d)

    with open(new_filepath, 'w') as f:
        json.dump(final_doc, f, indent=2)

// xml_to_json_script('regions/Regions.xml', 'DBRegions', 'regions', 'regions/regions.json')
// xml_to_json_script('regions/Zones.xml', 'Zones', 'zones', 'regions/zones.json')
xml_to_json_script('regions/StartupLocation.xml', 'StartupLocation', 'startup_locations', 'regions/startup_locations.json')
