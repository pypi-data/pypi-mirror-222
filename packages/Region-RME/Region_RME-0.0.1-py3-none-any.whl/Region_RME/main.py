import pymssql
import requests
import pandas as pd
import time
import getpass
import datetime

# Database connection
server = 'KFICWPNXDBSP01'
database = 'PlanX'
username = 'PowerBI_user'
password = r'PowerBI\User@Hossam@HQ1611'
cnxn = pymssql.connect(server=server, database=database, user=username, password=password)

def fetch_data(Region, userID, cnxn, token): 
    cursor = cnxn.cursor()
    cursor.execute(f"SELECT * FROM sta.PowerBI_Users WHERE User_ID = '{userID}' AND Region_Name = '{Region}'")
    row = cursor.fetchone()
    if row:
        row = dict(zip([column[0] for column in cursor.description], row))
    else:
        return pd.DataFrame({'Permission': ['you don’t have permission to execute the API calls']})

    max_api_calls = row['Max_API_Calls']
    cursor.execute(f"SELECT * FROM sta.PowerBI_Calls WHERE User_ID = '{userID}' AND Region_Name = '{Region}' AND Call_DateTime > DATEADD(day, -1, GETDATE())")
    rows = cursor.fetchall()
    if rows:
        rows = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
        total_calls = sum([row['No_Of_Calls'] for row in rows])
        if total_calls >= max_api_calls:
            return pd.DataFrame({'Permission': ['You are already exceeding your daily Calls, please try tomorrow or contact hossam.ibrahim@hlag.com']})
            
    api_url = f'https://planx.hlag.com/public/PlanX_CL_Scheme/query/testing2?year=\"2023\"&Currency=\"USD\"&Region={Region}&Layer 2=\"HL\"&CL Scheme Hierarchy=\"030\"&CL Scheme Type=\"020\"'
    headers = {'Authorization': f'Bearer {token}','Client-ID': 'API_User',}
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    temp_df = pd.DataFrame(data['data'], columns=['Month', 'Version', 'Layer Level 3','Currency', 'CL Scheme', 'Relation', 'REP CL Scheme'])
    no_of_calls = 1
    if not temp_df.empty:
        call_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(f"INSERT INTO sta.PowerBI_Calls (Region_Name, User_ID, Query_url, Call_DateTime, No_Of_Calls) VALUES ('{Region}', '{userID}', '{api_url}', '{call_date}', {no_of_calls})")
        cnxn.commit()
    return temp_df

def main():
    # Database connection
    server = 'KFICWPNXDBSP01'
    database = 'PlanX'
    username = 'PowerBI_user'
    password = r'PowerBI\User@Hossam@HQ1611'
    cnxn = pymssql.connect(server=server, database=database, user=username, password=password)

    auth_url = 'https://planx.hlag.com/identity/connect/token'
    auth_data = {'client_id': 'API_User','client_secret': 'abcd','grant_type': 'client_credentials','scope': 'public-api',}
    auth_data_str = '&'.join(f'{k}={v}' for k, v in auth_data.items())
    auth_response = requests.post(auth_url, data=auth_data_str)
    auth_response.raise_for_status()
    token = auth_response.json()['access_token']

    Regions = ['RME']
    df = pd.DataFrame()
    userID = getpass.getuser()
    for Region in Regions:
        temp_df = fetch_data(Region, userID, cnxn, token)  
        if temp_df is not None:
            df = pd.concat([df, temp_df])
    cnxn.close()
    return df

def Get_Region_Data():
    df = main()  # Call 'main' function and get 'df'
    return df
#    print(df) # or just df in Jupyter notebooks

