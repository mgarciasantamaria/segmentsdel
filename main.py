#!/usr/bin/env python
#_*_ codig: utf8 _*_
import datetime, psycopg2
from dateutil.relativedelta import relativedelta
from Modules.Constants import *
from Modules.functions import *

if Flag_Status('r'):
    psql_db=psycopg2.connect(db_data_connect)
    psql_cursor=psql_db.cursor()
    date_now=datetime.datetime.now()
    date=date_now-relativedelta(days=15)
    date_sql=str(datetime.datetime.strftime(date, "%Y-%m-%d"))
    psql_cursor.execute(f"DELETE FROM new_segmentos WHERE datetime LIKE'%{date_sql}%';")
    text_mail=psql_cursor.statusmessage
    psql_db.commit()
    psql_cursor.close()
    psql_db.close()
    Send_Mail(text_mail, 'cdnbytes summary')
else:
    Send_Mail('etltoolbox application failure not recognized', 'etltoolbox application failure not recognized')