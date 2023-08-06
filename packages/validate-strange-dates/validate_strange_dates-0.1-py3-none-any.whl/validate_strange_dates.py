import datetime
def format_date_function(date_str):
    """
    Formatea una fecha dada en diferentes formatos a 'YYYY-MM-DD'.
    
    Argumentos:
    date_str (str o datetime.datetime): La fecha que se formateará.
    
    Devuelve:
    str: La fecha formateada como 'YYYY-MM-DD', o None si no se pudo formatear.
    """
    if isinstance(date_str, datetime.datetime):
        return date_str.strftime('%Y-%m-%d')
    else:
        try:
            date_replace = date_str.replace('/', '-')
            date = datetime.datetime.strptime(date_replace, '%m-%d-%Y')
        except ValueError:
            try:
                date_replace = date_str.replace('/', '-')
                date = datetime.datetime.strptime(date_replace, '%d-%m-%Y')
            except ValueError:
                try:
                    date_replace = date_str.replace('/', '-')
                    date = datetime.datetime.strptime(date_replace, '%Y-%m-%d')
                except ValueError:
                    return None
        format_date_final = date.strftime('%Y-%m-%d')
        date_inits_form = format_date_final.split()[0]
        anio, mes, dia = date_inits_form.split("-")
        dia = dia.zfill(2)
        mes = mes.zfill(2)
        final_date = f"{anio}-{mes}-{dia}"
        return final_date