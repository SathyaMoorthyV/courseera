"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    "Description of the subroutine"
    return record[1]
    
def convert_coordinate(coordinate):
    "Description of the subroutine"
    return ( coordinate[0] , coordinate[1])

def compare_records(azara_record, rui_record):
    "Description of the subroutine"
    return azara_record[1] == rui_record[1][0]+rui_record[1][1]


def create_record(azara_record, rui_record):
    "Description of the subroutine"
    if    compare_records(azara_record, rui_record):
        new = azara_record + rui_record
        return new
    return 'not a match'
    
def clean_up(combined_record_group):
    "Description of the subroutine"
    endingvalue = ""
    for index, record in enumerate(combined_record_group):
        endingvalue =endingvalue+"('"+record[0]+"', '"+record[2]+"', ('"+record[3][0]+"', '"+record[3][1]+"'), '"+record[4]+"')\n"
    return endingvalue 