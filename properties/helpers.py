def modify_input_for_multiple_files(address, type, price, size, office, bedrooms, bathrooms, parking_lots, lt, ln, description, typeOfService, areas,  image, link):
    dict = {}
    dict['address'] = address
    dict['type'] = type
    dict['price'] = price
    dict['size'] = size
    dict['office'] = office
    dict['bedrooms'] = bedrooms
    dict['bathrooms'] = bathrooms
    dict['parking_lots'] = parking_lots
    dict['lt'] = lt
    dict['ln'] = ln
    dict['description'] = description
    dict['typeOfService'] = typeOfService
    dict['areas'] = areas
    dict['image'] = image
    dict['link'] = link
    

    return dict

def modify_input_for_multiple_files2(propertie_id, image):
    dict = {}
    dict['propertie_id'] = propertie_id
    dict['image'] = image
    

    return dict
