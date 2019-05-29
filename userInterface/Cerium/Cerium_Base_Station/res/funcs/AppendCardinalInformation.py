# Takes numerical vehicle heading value, appends a degree symbol and a
# a cardinal direction abbreviation.

def AppendCardinalInformation(data):
    function_name = "Append_Cardinal_Information()"
    numerical_data = float(data)
    data = data + u"\u00B0" + " "
    if(numerical_data > 270):
        data = data + "North West"
    elif(numerical_data == 270):
        data = data + "West"
    elif(numerical_data > 180):
        data = data + "South West"
    elif(numerical_data == 180):
        data = data + "South"
    elif(numerical_data > 90):
        data = data + "South East"
    elif(numerical_data == 90):
        data = data + "East"
    elif(numerical_data > 0):
        data = data + "North East"
    elif(numerical_data == 0):
        data = data + "North"
    return data
