from datetime import datetime

def find_age(birth_date, as_of_date):
    dob = as_of_date.split("-")
    dob_cutoff_dt = datetime(int(dob[0]), int(dob[1]), int(dob[2]))
    bd = birth_date.split("-")
    birth_dt = datetime(int(bd[0]), int(bd[1]), int(bd[2]))
    age = round(((dob_cutoff_dt - birth_dt)).days / 365, 0)
    return age
