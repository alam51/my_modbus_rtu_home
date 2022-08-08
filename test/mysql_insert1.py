import datetime
import traceback

import MySQLdb
import pandas as pd
import sqlalchemy

uri = "mysql://root:por1BABU@localhost/modbus_scada_db"
engine = sqlalchemy.create_engine(uri, echo=True)
table_name = 'analog_values'
t1 = datetime.datetime.now()
for i in range(10):
    try:
        df = pd.DataFrame({
            'date_time': [pd.to_datetime(datetime.datetime.now())],
            'bay_id': [1],
            'voltage': [230.124848],
            'I_R': [501.21145445],
            'I_Y': [501.21145445],
            'I_B': [501.21145445],
            'P_MW': [200.54454],
            'Q_MVA': [100.54454]
        })

        df.to_sql(table_name, con=uri, if_exists='append', index=False)
    except:
        traceback.print_exc()
print(datetime.datetime.now() - t1)
