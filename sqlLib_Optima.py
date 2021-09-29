from sqlLib_Optima import hitung_progress_level, show_level_progress, sql_connection
import mysql.connector
import json
from datetime import datetime

def connect_to_sql():
    connect = mysql.connector.connect(host = "localhost", user = "root", database ="optima", password = "")
    return connect

def reg_mitra(im, nm, np, nt, e, p):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("INSERT INTO mitra(id_mitra, nama_mitra_nama_pic, no_telp, email, pass) VALUES (%s, %s, %s, %s, %s)", (im, nm, np, nt, e, p))
        database.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def log_mitra(im, nm):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT id_mitra from mitra where email = %s and pass = %s", (im, nm))
        a = direct.fetchone()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        a = None
    if a == None:
        return None
    else:
        return a[0]

def check_mitra(im):
    database = connect_to_sql()
    direct = database.cursor()
    direct.execute ("SELECT id_mitra from mitra where nama_mitra = %s")
    a = direct.fetchone()
    if a == None:
        return False
    else:
        return a[0]

def get_id_mitra():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT id_mitra from mitra WHERE nama_mitra = %s")
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []    
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult


def get_all_request ():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT nodin, pemohon, perihal, tanggal FROM permintaan")
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    for x in range(0, len(d)):
        d[x]['tanggal'] = str(d[x]['tanggal'])
    Jsonresult = json.dumps(d)
    return Jsonresult    

def get_request(im):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT nodin, pemohon, perihal, tanggal FROM permintaan WHERE perihal LIKE = %s",("%" + im + "%",))
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def insert_request (im, nm, np, nt):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("INSERT INTO permintaan (nodin, pemohon, perihal, tanggal) VALUES (%s, %s, %s, %s)", (im, nm, np, nt))
        database.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        

def check_nodin_request(im):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nodin FROM permintaan where nodin = %s", (im,))
        database.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
 

def insert_cb(im, nm, np, nt):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("INSERT INTO permintaan(nodin, nocb, perihal, tanggal) VALUES (%s, %s, %s, %s)", (im, nm, np, nt))
        database.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def insert_lpo(im, nm, np, nt, e):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("INSERT INTO lpo(nama_project, nodin, witel, paket, sto) VALUE (%s,%s,%s,%s,%s)", (im,nm, np, nt, e))
        database.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def check_nomorcb(im):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("INSERT INTO nomor cb FROM cb WHERE cb =%s) VALUES (%s,%s,%s,%s)", (im, ))
        z = direct.fetchone()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return False
    else:
        return True

def insert_center(im, nm, np, nt, e):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("INSERT INTO center(id_mitra, nama_project, nilai, tanggal, status) VALUES (%s,%s,%s,%s)", (im, nm, np, nt, e))
        database.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def check_insert_center(im, nm):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project, id_mitra FROM center WHERE nama_project = %s and id_mitra = %s", (im, nm))
        z = direct.fetchone()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
    if z == None:
        return False
    else:
        return True

def update_status_pada_center(im, nm, np, nt):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("UPDATE center SET tanggal=%s, status =%s WHERE nama_project = %s and id_mitra = %s", (im, nm, np, nt))
        database.commit()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def get_center(im, nm):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT ct.nama_project, sto, tanggal, status FROM center ct JOIN lpo lp ON ct.nama_project = lp.nama_project WHERE id_mitra = %s and status = %s", (im, nm))
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def check_project(im):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project FROM center WHERE nama_project = %s", (im, ))
        z = direct.fetchone()
    except (mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return False
    else:
        return True

def cek_project_lop(im, nm):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project FROM lpo WHERE nama_project = %s and nodin = %s", (im, nm))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return True
    else:
        return False

def get_project(im):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project, nodin, witel, paket, sto FROM lpo WHERE nama_project LIKE %s", ("%" + im + "%"))
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def get_project_belum_diserahkan():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project, nodin, witel, paket, sto FROM lpo WHERE nama_projet NOT IN (SELECT nama_project FROM center")
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def get_project_sudah_diserahkan():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project, nodin, witel, paket, sto FROM lpo WHERE nama_projet IN (SELECT nama_project FROM center")
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def get_nama_project():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project FROM lpo")
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def get_nama_mitra(im):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_mitra FROM mitra WHERE id_mitra = %s", (im))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
    if z == None:
        return None
    else:
        return z[0]

def get_cb(im):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nodin, nocb, perihal, tanggal FROM cb WHERE nocb = %s", (im, ))
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def check_id_mitra(im):    
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT id_mitra FROM mitra WHERE id_mitra=%s", (im))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def check_id_admin(ia):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT id_admin FROM data_admin WHERE id_admin=%s", (ia))
        z = direct.fetchone()
        z = None
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
    if z == None:
        return None
    else:
        return z[0]

def login_admin(ad,min):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT id FROM admin WHERE username=%s and pass=%s", (ad, min))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def check_user_admin(cek):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT username FROM admin WHERE username=%s", (cek, ))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return True
    else:
        return False

def check_email_admin(cek):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT email FROM admin WHERE email=%s", (cek, ))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return True
    else:
        return False

def reg_admin(z, y, x, w, v):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ( "INSERT INTO admin(id, username, pass, nohp, email VALUES (%s, %s, %s, %s, %s,)" (z,y,x,w,v))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def insert_progress(z, y, x, w, v, u, t, s):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("INSERT INTO progress (nama_project, id_mitra, level, bukti, keterangan, status, tanggal deskirpsi VALUES (%s, %s, %s, %s, %s, %s, %s,)", (z,y,x,w,v, u, t, s))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        

def get_keterangan():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT keterangan FROM progress WHERE nama_project=%s", )
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def update_status(z, y, x, w, v, u, t, s):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ( "UPDATE progress SET status = %s, bukti = %s., tanggal=%s, deskripsi=%s WHERE id _mitra and nama+project=%s and level =%s and keterangan = %s", (z, y, x, w, v, u, t, s))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None

def show_progress(z):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.excecute( "SELECT nama_project, nama_mitra, status, FROM progress ps JOIN mitra mt ON ps.id_mitra = mt.id_mitra WHERE status = %s", (z, ))
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def check_progress(z):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project, id_mitra FROM progress WHERE nama_project=%s and id_mitra=%s", (z))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def show_level_progress_percentage(z):
    d = show_level_progress()
    for i in range (len(d)):
        d[i]['persentase'] = hitung_progress_level(z,d[i]['level'])
    Jsonresult = json.dumps(d)
    return Jsonresult

def show_progress_desc(z, y):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.excecute( "SELECT nama_project, status FROM progress WHERE keterangan = %s and level = %s", (z, y, ))
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult

def check_level_progress_desc(nama_project, level, keterangan):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project, level, keterangan FROM progress WHERE nama_project=%s and level=%s and id_mitra=%s", (nama_project, level, keterangan))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def insert_progress_persiapan(z, y, x):
    level = "persiapan"
    keterangan = ["Survei Lokasi", "Perijinan", "Sitac"]
    status = "belum"
    bukti = "kosong"
    deskripsi = "kosong"
    for i in keterangan:
        check = check_level_progress_desc(z, y, x)
        if check == True:
            insert_progress(z, y, level, bukti, i, status, x, deskripsi)

def insert_progress_instalasi(z, y, x):
    level = "instalasi"
    keterangan = ["Material Delivery", "Penarikan Kabel", "Pemasangan ODP", "Penanaman Tiang", "Pemasangan ODC"]
    status = "belum"
    bukti = "kosong"
    deskripsi = "kosong"
    for i in keterangan:
        check = check_level_progress_desc(z, y, x)
        if check == True:
            insert_progress(z, y, level, bukti, i, status, x, deskripsi)

def insert_progress_go_live(z, y, x):
    level = "go live"
    keterangan = ["Main Core", "Redaman"]
    status = "belum"
    bukti = "kosong"
    deskripsi = "kosong"
    for i in keterangan:
        check = check_level_progress_desc(z, y, x)
        if check == True:
            insert_progress(z, y, level, bukti, i, status, x, deskripsi)

def check_selesai_progress_persiapan(x, y):
    database = connect_to_sql()
    direct = database.cursor()
    level = "persiapan"
    status = "selesai"
    direct.execute("SELECT COUNT(keterangan) FROM progress WHERE id_mitra = %s and nama_project = %s and level = %s and status = %s", (x, y, level, status))
    z = direct.fetchone()
    try:
        j = int(z[0])
        if j >= 2:
            return True
        else:
            return False
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def check_selesai_progress_instalasi(x, y):
    database = connect_to_sql()
    direct = database.cursor()
    level = "instalasi"
    status = "selesai"
    try:
        direct.execute("SELECT COUNT(keterangan) FROM progress WHERE id_mitra = %s and nama_project = %s and level = %s and status = %s", (x, y, level, status))
        z = direct.fetchone()
        j = int(z[0])
        if j >= 4:
            return True
        else:
            return False
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def check_selesai_progress_go_live(x, y):
    database = connect_to_sql()
    direct = database.cursor()
    level = "go live"
    status = "selesai"
    direct.execute("SELECT COUNT(keterangan) FROM progress WHERE id_mitra = %s and nama_project = %s and level = %s and status = %s", (x, y, level, status))
    try:
        z = direct.fetchone()
        j = int(z[0])
        if j >= 4:
            return True
        else:
            return False
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def count_progress(x, y):
    persiapan_check = check_selesai_progress_persiapan(x, y)
    instalasi_check = check_selesai_progress_instalasi(x, y)
    go_live_check = check_selesai_progress_go_live(x, y)
    try:
        if persiapan_check == True and instalasi_check == True and go_live_check == True:
            hasil = "100"
            return hasil
        elif persiapan_check == True and instalasi_check == True and go_live_check == False:
            hasil = "66.6"
            return hasil
        elif persiapan_check == True and instalasi_check == False and go_live_check == False:
            hasil = "33.3"
            return hasil
        else:
            hasil = "0"
            return hasil
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def count_progress_level(x, y):
    database = connect_to_sql()
    direct = database.cursor()
    status = "selesai"
    try:
        direct.execute ("SELECT COUNT(keterangan) FROM progress WHERE nama_project=%s and level = %s and status = %s", (x, y, status))
        z  = direct.fetchone()
        j = int(z[0])
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
    if y == "persiapan":
        percentage = float((j/2)*100)
        return str(percentage)
    elif y == "instalasi":
        percentage = float((j/4)*100)
        return str(percentage)
    elif y == "go live":
        percentage = float((j/1)*100)
        return str(percentage)   

def get_perihal():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT perihal FROM permintaan")
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult
    

def get_all_nodin():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nodin FROM permintaan")
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult
    

def get_filebukti(z, y, x):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT bukti FROM progress WHERE nama_project = %s and level = %s and status = %s", (z, y, x))
        d = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        d = None
    if d == None:
        return None
    else:
        return d
    

def input_target_rab(z, y, x, w):
    database = connect_to_sql()
    direct = database.cursor()
    try: 
        direct.execute ( "INSERT INTO rab (nama_project, id_mitra, biaya, tgl_target VALUES (%s, %s, %s, %s)", (z, y, x, w))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def check_get_rab(z, y):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT biaya FROM rab WHERE id_mitra =%s and nama_project = %s", (z,y))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def edit_rab(z, y, x):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("UPDATE rab SET biaya = %s WHERE nama_project = %s and id_mitra = %s", (z, y, x))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)

def get_progress_project():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT nama_project, status, nama_mitra, center.id_mitra FROM center INNER JOIN mitra ON center.id_mitra = mitra.id_mitra")
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult   
   
def search_get_progress_project(nama_project):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nama_project, status, nama_mitra, center.id_mitra FROM center INNER JOIN mitra ON center.id_mitra = mitra.id_mitra WHERE nama_project LIKE %s", ("%" + nama_project +"%",))
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = [] 
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult
    

def search_get_general_project(nama_project):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT v_lpocenter.nama_project, v_lpocenter.nodin, v_lpocenter.witel, v_lpocenter.paket, v_lpocenter.status, v_lpocenter.sto, mitra.nama_mitra, v_lpocenter.id_mitra FROM v_lpocenter LEFT JOIN mitra ON v_lpocenter.id_mitra = mitra.id_mitra WHERE v_lpocenter.nama_project LIKE %s", ("%" + nama_project + "%",))
        r = [x for x in direct]
        c = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        r = []
        c = []
    d = []
    for row in r:
        data ={}
        for p, val in zip(c, r):
            data[p] = val
        d.append(data)
    Jsonresult = json.dumps(d)
    return Jsonresult
    

def project_desc(nama_project, level, keterangan):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT deskripsi FROM progress WHERE nama_project = %s and level = %s and keterangan = %s", (nama_project, level, keterangan))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]
    

def get_tgl_project(status, nama_project, id_mitra):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT tanggal FROM center WHERE status=%s AND nama_project=%s AND id_mitra=%s", (status, nama_project, id_mitra))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def get_tgl_project_selesai (nama_project, id_mitra):
    status = "selesai"
    z = get_tgl_project(status, nama_project, id_mitra)
    return z

def get_tgl_target(nama_project, id_mitra):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT tgl_target FROM rab WHERE nama_project=%s AND id_mitra=%s", (nama_project, id_mitra))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]
    

def list_paket():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT paket FROM paket_dat")
        ro = [x for x in direct]
        co = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        ro = []
        co = []
    datas =[]
    for row in ro:
        data = {}
        for prop, val in zip(co, ro):
            data[prop] = val
        datas.append(data)
        dataJson = json.dumps(datas)
    return dataJson
    
def list_sto():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT sto FROM sto_dat")
        ro = [x for x in direct]
        co = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
    datas =[]
    for row in ro:
        data = {}
        for prop, val in zip(co, ro):
            data[prop] = val
        datas.append(data)
    dataJson = json.dumps(datas)
    return dataJson
         
def count_center_status_belum_project(id_mitra):
    database = connect_to_sql()
    direct = database.cursor()
    status = "belum"
    try:
        direct.execute("SELECT COUNT(nama_project) FROM center WHERE id_mitra=%s AND status = %s", (id_mitra, status))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def count_center_status_proses_project(id_mitra):
    database = connect_to_sql()
    direct = database.cursor()
    status = "proses"
    try:
        direct.execute("SELECT COUNT(nama_project) FROM center WHERE id_mitra=%s AND status = %s", (id_mitra, status))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def count_center_status_selesai_project(id_mitra):
    database = connect_to_sql()
    direct = database.cursor()
    status = "selesai"
    try:
        direct.execute("SELECT COUNT(nama_project) FROM center WHERE id_mitra=%s AND status = %s", (id_mitra, status))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        z = None
    if z == None:
        return None
    else:
        return z[0]

def get_all_mitra_with_status():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT id_mitra, nama_mitra FROM mitra")
        ro = [x for x in direct]
        co = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        ro = []
        co = []
    datas =[]
    for row in ro:
        data = {}
        for prop, val in zip(co, ro):
            data[prop] = val
        datas.append(data)
    dataJson = json.dumps(datas)

    for i in range (len(datas)):
        datas[i]['belum'] = count_center_status_belum_project(datas[i]['id_mitra'])
        datas[i]['proses'] = count_center_status_proses_project(datas[i]['id_mitra'])
        datas[i]['selesai'] = count_center_status_selesai_project(datas[i]['id_mitra'])

    datajson = json.dumps(datas)
    return datajson

def get_general_project_base_on_nodin(nodin):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("SELECT v_lpocenter.nama_project,v_lpocenter.nodin,v_lpocenter.witel,v_lpocenter.paket,v_lpocenter.status,v_lpocenter.sto,mitra.nama_mitra,v_lpocenter.id_mitra FROM v_lpocenter LEFT JOIN mitra on v_lpocenter.id_mitra = mitra.id_mitra WHERE v_lpocenter.nodin = %s", (nodin,))
        ro = [x for x in direct]
        co = [x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)
        ro = []
        co = []
    datas = []
    for row in ro:
        data = {}
        for prop, val in zip(co, ro):
            data[prop] = val
        datas.append(data)
    dataJson = json.dumps(datas)
    return dataJson

def update_permintaan (pemohon, perihal, tanggal, nodin):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("UPDATE permintaan SET pemohon = %s, perihal =%s, tanggal=%s WHERE nodin=%s", (pemohon, perihal, tanggal, nodin))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as e:
        print (e)

def cek_permintaan_in_lop(nodin):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nodin FROM v_lpocenter WHERE nodin=%s", (nodin,))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        z = None
    if z == None:
        return False
    else:
        return True

def get_detail_permintaan(nodin):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT nodin, pemohon, perihal, tanggal FROM permintaan WHERE nodin=%s", (nodin, ))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as e:
        print (e)
        z = None
    if z == None:
        return None
    else:
        return z

def update_lop(nama_project_new, witel, paket, sto, nama_project_old):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("UPDATE lpo SET nama_project=%s, witel=%s, paket=%s, sto=%s WHERE nama_project=%s", (nama_project_new, witel, paket, sto, nama_project_old))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)

def update_data_center(nama_project_new, id_mitra, nama_project_old):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("UPDATE center SET nama_project=%s, id_mitra=%s, tanggal=now() WHERE nama_project=%s", (nama_project_new, id_mitra, nama_project_old))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as e:
        print (e)

def search_get_permintaan(value):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT 'nodin', 'pemohon', 'perihal', 'tanggal' FROM 'permintaan' WHERE concat ('nodin', 'pemohon', 'perihal', 'tanggal') LIKE %s", ("%" + value + "%",))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as e:
        print (e)
        ro = []
        co = []
    datas =[]
    for row in ro:
        data = {}
        for prop, val in zip(co, ro):
            data[prop] = val
        datas.append(data)
    for x in range(0,len(datas)):
        datas[x]['tanggal'] = str(datas[x]['tanggal'])
    dataJson = json.dumps(datas)
    return dataJson

def count_project_stat_belum(tahun):
    database = connect_to_sql()
    direct = database.cursor()
    status = "belum"
    try:
        direct.execute("SELECT COUNT(nama_project) FROM center WHERE YEAR(tanggal) = %s AND status=%s", (tahun, status))
        z = direct.fetchone()
    except (mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        z = None
    if z == None:
        return "0"
    else:
        return z[0]

def count_project_stat_proses(tahun):
    database = connect_to_sql()
    direct = database.cursor()
    status = "proses"
    try:
        direct.execute("SELECT COUNT(nama_project) FROM center WHERE YEAR(tanggal)=%s AND status=%s", (tahun, status))
        z = direct.fetchone()
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        z = None
    if z == None:
        return "0"
    else:
        return z[0]

def count_project_stat_selesai(tahun):
    database = connect_to_sql()
    direct = database.cursor()
    status = "selesai"
    try:
        direct.execute("SELECT COUNT(nama_project) FROM center WHERE YEAR(tanggal)=%s AND status=%s", (tahun, status))
        z = direct.fetchone()
    except(mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        z = None
    if z == None:
        return "0"
    else:
        return z[0]

def list_tahun_center():
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT YEAR(tanggal) as tahun FROM center")
        ro = [x for x in direct]
        co = [ x[0] for x in direct.description]
    except(mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        ro = []
        co = []
    datas = []
    for row in ro:
        data = {}
        for prop, val in zip(co, ro):
            data[prop] = val
        datas.append(data)
    dataJson = json.dumps(datas)
    return dataJson

def input_report_lokasi(np, lat, lng):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("INSERT INTO lokasi(nama_project,lat,lng) VALUES (%s,%s,%s)", (np, lat, lng))
        database.commit() 
        set = True
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        set = False
    if set == False:
        return False
    else:
        return True

def get_report_lokasi(nama_project):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute("SELECT lat, lng FROM lokasi WHERE nama_project = %s", (nama_project))
        z = direct.fetchone()
        database.commit()
        set = True
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        z = None
    if z == None:
        return False, None
    else:
        return True, z

def show_project_amount(im, np, tahun):
    database = connect_to_sql()
    direct = database.cursor()
    try:
        direct.execute ("INSERT INTO jumlah_projek(belum, proses, selesai) VALUES (%s,%s,%s)", (im, np, tahun))
        database.commit()
    except(mysql.connector.Error, mysql.connector.Warning) as error :
        print(error)