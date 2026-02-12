Step 1: pip install Gitpython 
Step 2: import git 
repo_url="https://github.com/PhonePe/pulse.git" 
destination_path= r"D:/DS_Projects/PhonepeProjects" 
git.Repo.clone_from(repo_url, destination_path) 
print("Repository cloned Successfully") 
(or ) 
STEP 2: import git 
print(git.__version__) 
STEP 3: 
import os 
path = r"D:/DS_Projects/PhonepeProjects/pulse/data/aggregated/transaction/country/india/state" 
Agg_state_list = os.listdir(path) 
Agg_state_list 
Step 4: 
#Required libraries for the program 
import pandas as pd 
import json 
import os 
#direct Path to get the data as states 
path = "D:/DS_Projects/PhonepeProjects/pulse/data/aggregated/transaction/country/india/state/" 
Agg_state_list = os.listdir(path) 
Agg_state_list 
#Agg_state_list to get list of states in india 
clm={'State':[], 'Year':[],'Quarter':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]} 
#------ Data Frame 1 -aggregated_transacion------#
for i in Agg_state_list: 
    p_i=path+i+"/" 
    Agg_yr = os.listdir(p_i) 
    for j in Agg_yr: 
        p_j=p_i+j+"/" 
        Agg_yr_list=os.listdir(p_j) 
        for k in Agg_yr_list: 
            p_k=p_j+k 
            Data=open(p_k,'r') 
            D=json.load(Data) 
            for z in D['data']['transactionData']: 
              Name=z['name'] 
              count=z['paymentInstruments'][0]['count'] 
              amount=z['paymentInstruments'][0]['amount'] 
              clm['Transacion_type'].append(Name) 
              clm['Transacion_count'].append(count) 
              clm['Transacion_amount'].append(amount) 
              clm['State'].append(i) 
              clm['Year'].append(j) 
              clm['Quarter'].append(int(k.strip('.json'))) 
# Successfully created a dataframe 
aggregated_transacion = pd.DataFrame(clm)
#------ Data Frame 2 -aggregated_user------#
import pandas as pd 
import json 
import os 

path = "D:/DS_Projects/PhonepeProjects/pulse/data/aggregated/user/country/india/state/" 
Agg_state_list = os.listdir(path) 
 
clm = {'State': [], 'Year': [], 'Quarter': [], 'Brand': [] , 'User_count': [], 'Percentage': [], 'Registered_users': 
[] ,'App_opens': [] } 
 
for i in Agg_state_list:  # state 
    p_i = os.path.join(path, i) 
    Agg_yr = os.listdir(p_i) 
     
    for j in Agg_yr:  # year 
        p_j = os.path.join(p_i, j) 
        Agg_yr_list = os.listdir(p_j) 
         
        for k in Agg_yr_list:  # quarter file 
            p_k = os.path.join(p_j, k) 
             
            with open(p_k, 'r') as Data: 
                D = json.load(Data) 
                 
                registered = D['data']['aggregated']['registeredUsers'] 
                app_opens = D['data']['aggregated']['appOpens'] 
                devices = D['data'].get('usersByDevice') or [] 
 
            for z in devices: 
             brand = z['brand'] 
             count = z['count'] 
             percentage = z['percentage'] 
             clm['State'].append(i) 
             clm['Year'].append(j) 
             clm['Quarter'].append(int(k.strip('.json'))) 
             clm['Brand'].append(brand) 
             clm['User_count'].append(count) 
             clm['Percentage'].append(percentage) 
             clm['Registered_users'].append(registered) 
             clm['App_opens'].append(app_opens) 
aggregated_user = pd.DataFrame(clm) 
#------ Data Frame 3 -aggregated_insurance------#
import pandas as pd 
import json 
import os 
 
path = "D:/DS_Projects/PhonepeProjects/pulse/data/aggregated/insurance/country/india/state/" 
Agg_state_list = os.listdir(path) 
 
clm = {'State': [],'Year': [],'Quarter': [],'Insurance_type': [],'Insurance_count': [],'Insurance_amount': []} 
 
for i in Agg_state_list:  # state 
    p_i = os.path.join(path, i) 
    Agg_yr = os.listdir(p_i) 
     
    for j in Agg_yr:  # year 
        p_j = os.path.join(p_i, j) 
        Agg_yr_list = os.listdir(p_j)        
        for k in Agg_yr_list:  # quarter file 
            p_k = os.path.join(p_j, k) 
             
            with open(p_k, 'r') as Data: 
                D = json.load(Data) 
                 
                for z in D['data']['transactionData']: 
                    name = z['name'] 
                    count = z['paymentInstruments'][0]['count'] 
                    amount = z['paymentInstruments'][0]['amount'] 
                     
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Insurance_type'].append(name) 
                    clm['Insurance_count'].append(count) 
                    clm['Insurance_amount'].append(amount) 
aggregated_insurance = pd.DataFrame(clm) 
#------ Data Frame 4 -map_transaction------#
import pandas as pd 
import json 
import os 
 
path = "D:/DS_Projects/PhonepeProjects/pulse/data/map/transaction/hover/country/india/state/" 
Map_state_list = os.listdir(path)  
clm = { 
    'State': [], 
    'Year': [], 
    'Quarter': [], 
    'Hover_name': [], 
    'Transaction_count': [], 
    'Transaction_amount': [] 
}  
for i in Map_state_list:   # state folder 
    p_i = os.path.join(path, i) 
    Map_yr = os.listdir(p_i) 
     
    for j in Map_yr:       # year 
        p_j = os.path.join(p_i, j) 
        Map_yr_list = os.listdir(p_j) 
         
        for k in Map_yr_list:   # quarter file 
            p_k = os.path.join(p_j, k) 
             
            with open(p_k, 'r') as Data: 
                D = json.load(Data) 
                 
                hover_list = D['data'].get('hoverDataList', []) or [] 
                 
                for z in hover_list: 
                    name = z['name'] 
                    count = z['metric'][0]['count']
                    amount = z['metric'][0]['amount']   
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Hover_name'].append(name) 
                    clm['Transaction_count'].append(count) 
                    clm['Transaction_amount'].append(amount) 
 
map_transaction = pd.DataFrame(clm)

#------ Data Frame 5 -map_user------#

import pandas as pd 
import json 
import os 
 
path = "D:/DS_Projects/PhonepeProjects/pulse/data/map/user/hover/country/india/state/" 
Map_state_list = os.listdir(path) 
 
clm = { 
    'State': [], 
    'Year': [], 
    'Quarter': [], 
    'Hover_name': [], 
    'Registered_users': [], 
    'App_opens': [] 
} 
for i in Map_state_list:   # state folder 
    p_i = os.path.join(path, i) 
    Map_yr = os.listdir(p_i) 
     
    for j in Map_yr:       # year 
        p_j = os.path.join(p_i, j) 
        Map_yr_list = os.listdir(p_j) 
         
        for k in Map_yr_list:   # quarter file 
            p_k = os.path.join(p_j, k) 
             
            with open(p_k, 'r') as Data: 
                D = json.load(Data) 
                 
                hover_dict = D['data'].get('hoverData', {}) or {} 
                 
                for name, values in hover_dict.items(): 
                    registered = values['registeredUsers'] 
                    app_opens = values['appOpens'] 
                     
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Hover_name'].append(name) 
                    clm['Registered_users'].append(registered) 
                    clm['App_opens'].append(app_opens) 
 
map_user = pd.DataFrame(clm) 

#------ Data Frame 6 -map_insurance------#
import pandas as pd 
import json 
import os 
 
path = "D:/DS_Projects/PhonepeProjects/pulse/data/map/insurance/hover/country/india/state/" 
Map_state_list = os.listdir(path) 
 
clm = { 
    'State': [], 
    'Year': [], 
    'Quarter': [], 
    'Hover_name': [], 
    'Insurance_count': [], 
    'Insurance_amount': [] 
} 
 
for i in Map_state_list:   # state folder 
    p_i = os.path.join(path, i) 
    Map_yr = os.listdir(p_i) 
     
    for j in Map_yr:       # year 
        p_j = os.path.join(p_i, j) 
        Map_yr_list = os.listdir(p_j) 
         
        for k in Map_yr_list:   # quarter file 
            p_k = os.path.join(p_j, k)  
            with open(p_k, 'r') as Data: 
                D = json.load(Data) 
                 
                hover_list = D['data'].get('hoverDataList', []) or [] 
                 
                for z in hover_list: 
                    name = z['name'] 
                    count = z['metric'][0]['count'] 
                    amount = z['metric'][0]['amount'] 
                     
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Hover_name'].append(name) 
                    clm['Insurance_count'].append(count) 
                    clm['Insurance_amount'].append(amount) 
 
map_insurance = pd.DataFrame(clm)

#------ Data Frame 7 -top_state_transaction------#

import pandas as pd 
import json 
import os 
 
path = "D:/DS_Projects/PhonepeProjects/pulse/data/top/transaction/country/india/state/" 
state_list = os.listdir(path)  
clm = { 
    'State': [], 
    'Year': [], 
    'Quarter': [], 
    'Level': [], 
    'Entity_name': [], 
    'Transaction_count': [], 
    'Transaction_amount': [] 
} 
 
for i in state_list:  # state 
    p_i = os.path.join(path, i) 
     
    for j in os.listdir(p_i):  # year 
        p_j = os.path.join(p_i, j) 
         
        for k in os.listdir(p_j):  # quarter file 
            p_k = os.path.join(p_j, k) 
             
            with open(p_k, 'r') as Data: 
                D = json.load(Data) 
                 
                for z in D['data'].get('districts', []): 
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Level'].append('District') 
                    clm['Entity_name'].append(z['entityName']) 
                    clm['Transaction_count'].append(z['metric']['count']) 
                    clm['Transaction_amount'].append(z['metric']['amount']) 
 
top_state_transaction = pd.DataFrame(clm)

#------ Data Frame 8 -top_user------#
import pandas as pd 
import json 
import os 
 
path = "D:/DS_Projects/PhonepeProjects/pulse/data/top/user/country/india/state/" 
state_list = os.listdir(path) 
 
clm = { 
    'State': [], 
    'Year': [], 
    'Quarter': [], 
    'Level': [], 
    'Entity_name': [], 
    'Registered_users': [] 
} 
 
for i in state_list:   # state 
    p_i = os.path.join(path, i) 
     
    for j in os.listdir(p_i):   # year 
        p_j = os.path.join(p_i, j)
        for k in os.listdir(p_j):   # quarter file 
            p_k = os.path.join(p_j, k) 
             
            with open(p_k, 'r') as Data: 
                D = json.load(Data) 
                 
                # DISTRICTS 
                for z in D['data'].get('districts', []): 
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Level'].append('District') 
                    clm['Entity_name'].append(z['name']) 
                    clm['Registered_users'].append(z['registeredUsers']) 
                 
                # PINCODES 
                for z in D['data'].get('pincodes', []): 
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Level'].append('Pincode') 
                    clm['Entity_name'].append(z['name']) 
                    clm['Registered_users'].append(z['registeredUsers']) 
 
top_user = pd.DataFrame(clm)

#------ Data Frame 9 -top_insurance ------#
import pandas as pd  
import json 
import os 
 
path = "D:/DS_Projects/PhonepeProjects/pulse/data/top/insurance/country/india/state/" 
state_list = os.listdir(path) 
 
clm = { 
    'State': [], 
    'Year': [], 
    'Quarter': [], 
    'Level': [], 
    'Entity_name': [], 
    'Insurance_count': [], 
    'Insurance_amount': [] 
} 
 
for i in state_list:   # state 
    p_i = os.path.join(path, i) 
     
    for j in os.listdir(p_i):   # year 
        p_j = os.path.join(p_i, j) 
         
        for k in os.listdir(p_j):   # quarter file 
            p_k = os.path.join(p_j, k) 
             
            with open(p_k, 'r') as Data: 
                D = json.load(Data) 
                # DISTRICTS 
                for z in D['data'].get('districts', []): 
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Level'].append('District') 
                    clm['Entity_name'].append(z['entityName']) 
                    clm['Insurance_count'].append(z['metric']['count']) 
                    clm['Insurance_amount'].append(z['metric']['amount']) 
                 
                # PINCODES 
                for z in D['data'].get('pincodes', []): 
                    clm['State'].append(i) 
                    clm['Year'].append(j) 
                    clm['Quarter'].append(int(k.strip('.json'))) 
                    clm['Level'].append('Pincode') 
                    clm['Entity_name'].append(z['entityName']) 
                    clm['Insurance_count'].append(z['metric']['count']) 
                    clm['Insurance_amount'].append(z['metric']['amount']) 
 
top_insurance = pd.DataFrame(clm) 
#-----Run the code for checking -----#
aggregated_transacion 
aggregated_user 
aggregated_insurance 
map_transaction 
map_user 
map_insurance 
top_state_transaction 
top_user 
top_insurance
#------SQL connection:------#
import pandas as pd 
from sqlalchemy import create_engine 
USERNAME = "postgres" 
PASSWORD = "Malu%401811" 
HOST = "localhost" 
PORT = "5432" 
DB_NAME = "phonepe" 
engine = 
create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}") 
#-----CORRECT THE COLUMN NAME: ------#
 aggregated_transacion.columns = [c.lower() for c in aggregated_transacion.columns] 
aggregated_user.columns = [c.lower() for c in aggregated_user.columns] 
aggregated_insurance.columns = [c.lower() for c in aggregated_insurance.columns] 
map_transaction.columns = [c.lower() for c in map_transaction.columns] 
map_user.columns = [c.lower() for c in map_user.columns] 
map_insurance.columns = [c.lower() for c in map_insurance.columns] 
top_state_transaction.columns = [c.lower() for c in top_state_transaction.columns] 
top_user.columns = [c.lower() for c in top_user.columns] 
top_insurance.columns = [c.lower() for c in top_insurance.columns]

#-----Push python to SQL tables: ------#
aggregated_transacion.to_sql("aggregated_transacion", engine, if_exists="append", index=False) 
aggregated_user.to_sql("aggregated_user", engine, if_exists="append", index=False) 
aggregated_insurance.to_sql("aggregated_insurance", engine, if_exists="append", index=False) 
map_transaction.to_sql("map_transaction", engine, if_exists="append", index=False) 
map_user.to_sql("map_user", engine, if_exists="append", index=False) 
map_insurance.to_sql("map_insurance", engine, if_exists="append", index=False) 
top_state_transaction.to_sql("top_state_transaction", engine, if_exists="append", index=False) 
top_user.to_sql("top_user", engine, if_exists="append", index=False) 
top_insurance.to_sql("top_insurance", engine, if_exists="append", index=False)

