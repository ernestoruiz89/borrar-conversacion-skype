# -*- coding: cp1252 -*-
import sqlite3
import os

profile = os.environ.get('USERPROFILE')

confirm = raw_input("Si continuas Skype va a cerrarse, deberas abrirlo nuevamente. Continuar? SI/NO: ")
if confirm == "SI" or confirm == "Si" or confirm == "si" or confirm == "sI":
    os.system('taskkill /f /im Skype.exe')
    while True:
        try:
            usuario = raw_input("Mi usuario de skype: ")
            conn = sqlite3.connect(profile+'\\AppData\\Roaming\\Skype\\'+usuario+'\\main.db')
            c = conn.cursor()
            break
        except (RuntimeError,BaseException):
            print "No existe usuario en esta maquina, intente nuevamente..."

    while True:
        try:
            partner = raw_input("Usuario a eliminar: ")
            c.execute("SELECT DISTINCT convo_id FROM Messages WHERE dialog_partner = '"+partner+"';")
            result = c.fetchone()
            if result is None:
                error
            break
        except (RuntimeError,BaseException):
            print "No existe usuario en esta maquina, intente nuevamente..."

    confirm = raw_input("Esta seguro de eliminar permanentemente los mensajes de '"+partner+"'? SI/NO: ")

    if confirm == "SI" or confirm == "Si" or confirm == "si" or confirm == "sI":    
        if result is not None:
            convo_id = int(result[0])
            c.execute("DELETE FROM Messages where convo_id = {}".format(convo_id))
            deleted = int(conn.total_changes)
            print("Borrado: {} mensajes".format(deleted))
            c.execute("VACUUM;")
            print("Optimización de la base de datos realizada!!")
        conn.close()
        raw_input("Presione Enter para finalizar...")
    else:
        raw_input("No se borro nada. Presione Enter para finalizar...")
else:
    raw_input("Presione Enter para finalizar...")



