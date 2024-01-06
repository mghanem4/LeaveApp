import pyodbc

# Source: https://datatofish.com/how-to-connect-python-to-ms-access-database-using-pyodbc/
# This piece of code accesses a MS Access Database. It is used instead of creating a SQL database for simplicity.


def fetch_creds() -> list[tuple]:
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\mgahm\OneDrive\Desktop\app\login_creds.accdb;')
    cursor = conn.cursor()
    cursor.execute('select * from creds')
    usernames= [()]
    for row in cursor.fetchall():
        usernames.append((row[1],row[2]))
        
    conn.close()
    return usernames

# Function which checks if the username and password are stored in the DB
# Returns True if the username and password are stored in the DB
# Returns False if the username and password are not stored in the DB

def creds_checker(username : str, password : str) -> bool:
    creds_list=fetch_creds()
    if (username, password) in creds_list:
        return True
    else:
        return False

def form_insert(name:str,email:str,reason:str, start_dt, end_date,leave_type:str,total_hours):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\mgahm\OneDrive\Desktop\app\login_creds.accdb;')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Form (first_last_name,user_email,reason,start_dte,end_dte,leave_type,total_hours) VALUES (?,?,?,?,?,?,?)",
    (name,email,reason,start_dt,end_date,leave_type,total_hours))
    conn.commit()
    conn.close()

def form_fetch():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\mgahm\OneDrive\Desktop\app\login_creds.accdb;')
    cursor = conn.cursor()
    cursor.execute('select * from Form')
    form_list= [()]
    for row in cursor.fetchall():
        form_list.append((row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        
    conn.close()
    return form_list



if __name__ == "__main__":
    fetch_creds()
    form_fetch()