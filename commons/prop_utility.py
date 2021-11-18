# create a function which should take file and property name as input and return property value.
def get_property_value(file_name, property_name):
    with open(file_name, 'r') as f:
        for line in f:
            if property_name in line:
                return line.split("=")[1].strip()


# # create a function which should take file name and property name and property value as input and update property value.
def update_property_value(file_name, property_name, property_value):
    with open(file_name, "r") as f:
        props = f.readlines()
        with open(file_name, "w") as f:
            for p in props:
                if property_name in p:
                    f.write(property_name + "=" + property_value.strftime("%d-%b-%Y %H:%M:%S") + "\n")
