import psycopg2
from psycopg2 import Error
import pandas as pd
import json

class pg:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.database = db_name
        self.user = db_user
        self.password = db_password
        self.host = db_host
        self.port = db_port

    def query(self, query, output_as_pandas_df = True):
        error_msg = None
        records = None
        df = None
        conn = None
        try:

            # Connect to an existing database
            conn = psycopg2.connect(
                database = self.database,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port
            )

            conn.autocommit = True

            conn.autocommit = True

            # Create a cursor to perform database operations
            cursor = conn.cursor()

            # Executing a SQL query
            cursor.execute(query)

            for notice in conn.notices:
                print(notice)

            # Fetch result
            try:
                records = cursor.fetchall()
                colnames = [desc[0] for desc in cursor.description]
                    
            except:
                pass
            
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
            error_msg = str(error)
        finally:
            if (conn):
                cursor.close()
                conn.close()
                # print("PostgreSQL connection is closed")

                if records is not None:

                    if output_as_pandas_df:
                        df = pd.DataFrame(records)
                        df.columns = colnames

                        return df
                    else:
                        return {
                            "records" : records,
                            "colnames" : colnames 
                        }
                elif error_msg is not None:
                    return error_msg
                else:
                    return None
    ################################################################################
    ### EXAMPLE FOR insert
    # on_conflict = {
    #     "conflict_cols" : ['account_id','date','outlet_id'],
    #     "on_conflict_behaviour" : 'DO NOTHING', #OR "DO UPDATE SET"
    #     "on_conflict_change_cols" : ['index_json']
    # }
    def insert(self, table_name, json, on_conflict = None):

        colnames_sql = ','.join(list(json.keys()))
        values_sql = ""
        
        for i in range(0,len(json)):
            var_ = json[list(json.keys())[i]]

            curr_str = ""

            if type(var_) == int or type(var_) == float:
                curr_str = var_
            # elif isinstance(var_,dict):
            #     curr_str = json.dumps(var_)
            else:
                curr_str = "'" + var_ + "'"

            if values_sql == "":
                values_sql = curr_str
            else:
                values_sql += (", " + str(curr_str))

        insert_sql = f"""
INSERT INTO {table_name} ({colnames_sql})
VALUES ({values_sql})"""

        if on_conflict is not None and 'conflict_cols' in on_conflict.keys():
            conflict_cols = on_conflict['conflict_cols']
            conflict_cols_sql = ','.join(conflict_cols)

            on_conflict_behaviour_sql = 'DO NOTHING'
            on_conflict_change_cols_sql = ''
            if 'on_conflict_behaviour' in on_conflict.keys() and on_conflict['on_conflict_behaviour'] == 'DO UPDATE SET' and 'on_conflict_change_cols' in on_conflict.keys():
                on_conflict_behaviour_sql = 'DO UPDATE SET'

                for i in range(0,len(on_conflict['on_conflict_change_cols'])):
                    if i > 0:
                        on_conflict_change_cols_sql += """
    ,"""
                    else:
                        on_conflict_change_cols_sql += """    """
                    on_conflict_change_cols_sql += f"""{on_conflict['on_conflict_change_cols'][i]} = EXCLUDED.{on_conflict['on_conflict_change_cols'][i]}"""

            insert_sql += f"""
ON CONFLICT ({conflict_cols_sql}) {on_conflict_behaviour_sql}
{on_conflict_change_cols_sql}
            """
        
        return self.query(insert_sql)

    def insert_single(self, table_name, json, on_conflict = None, db_creds = None):

        ##### preparation
        # table_name = 'streamlit.logs'

        colnames = json.keys()
        colnames = list(colnames)

        val_prep = json
        query_str = f"INSERT INTO {table_name}("

        for i in range(0,len(colnames)):

            ### for query string
            val_ = colnames[i]
            if i > 0:
                val_ = ', ' + val_

            query_str += f"{val_}"

            #### for values
            if isinstance(val_,dict):
                val_prep[val_] = json.dumps(val_prep[val_])

        vals_label = ''
        if len(colnames) > 1:
            vals_label = '%s' + (', %s' * (len(colnames) -1))

        query_str += f") VALUES ({vals_label})"

        values = tuple(val_prep.values())

        ##### execute
        try:
            if db_creds is not None:
                conn = psycopg2.connect(
                    database = db_creds['database'],
                    user = db_creds['user'],
                    password = db_creds['password'],
                    host = db_creds['host'],
                    port = db_creds['port']
                )
            else:
                # Connect to an existing database
                conn = psycopg2.connect(
                    database = self.database,
                    user = self.user,
                    password = self.password,
                    host = self.host,
                    port = self.port
                )

            conn.autocommit = True

            # Create a cursor to perform database operations
            cursor = conn.cursor()

            # Executing a SQL query
            cursor.execute(query_str, values)

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
            error_msg = str(error)
            
        finally:
            if (conn):
                cursor.close()
                conn.close()