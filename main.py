from src.get_data import get_suicide_data

if __name__ == '__main__':
    suicide_2000 = get_suicide_data(year=2000)
    suicide_2005 = get_suicide_data(year=2005)
    suicide_2010 = get_suicide_data(year=2010)
    suicide_2015 = get_suicide_data(year=2015)
    suicide_2016 = get_suicide_data(year=2016)