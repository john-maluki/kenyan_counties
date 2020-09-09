from read import ReadKenyanCounties

def get_counties():
    """This functions return all kenya counties in list"""
    counties = ReadKenyanCounties('kenya_counties.txt') \
        .read_all_counties()
    return counties

def get_county_number():
    """Return number of counties in kenya"""
    return len(get_counties())

