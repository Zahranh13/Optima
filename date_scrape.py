from datetime import datetime
def convert_to_date_object(date_string):
    date_object = datetime.strptime(date_string, "%d-%m-%Y")
    thn = int(date_object.strftime('%Y'))
    bln = int(date_object.strftime('%m'))
    tgl = int(date_object.strftime('%d'))
    list = [tgl, bln, thn]
    return list