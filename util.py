import pickle
import json
import numpy as np

__Locality = None
__data_columns = None
__model = None

def get_estimated_price(Locality,Area,Bathroom,BHK):
    try:
        loc_index = __data_columns.index(Locality.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Area
    x[1] = Bathroom
    x[2] = BHK
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locality

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/delhi_realestate_price.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_Locality_names():
    return __Locality

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_Locality_names())
    print(get_estimated_price('dwarka',1000, 3, 3))
    print(get_estimated_price('dwarka', 1000, 2, 2))
   # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
   # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location