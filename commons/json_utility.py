# create a function which should take json object and property name as input and return property value.
def get_property_value_from_json(json_object, property_name):
    return json_object['records'][property_name]
