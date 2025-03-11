#import pack
from fastapi import FastAPI, Header, HTTPException
import pandas as pd


secret = "kontolbapaklu"

#memvuat instance/object
app = FastAPI()

# endpoint -> aturan request dari 
# endpoint untuk menampilkan halaman
@app.get('/')
def getHome():
    #read data
    df = pd.read_csv('data.csv')

    # mengembalikan data ke client (response)
    return{
        "data" : df.to_dict(orient='records')
    }

@app.get('/data/{filter}')
def getData(filter:str):
    #read data
    df = pd.read_csv('data.csv')

    # filter dataframe
    result = df[df.name == filter]
    # result = df.query(f"name == '{filter}'")
    return result.to_dict(orient='records')

#endpoint untuk menghapus data hasil
@app.delete('/data/{filter}')
def deleteData(filter: str, api_key=Header(None)):
    if api_key is not None and api_key == secret :
        #read data
        df = pd.read_csv('data.csv')

        # filter dataframe
        result = df[df.name != filter]
        # result = df.query(f"name == '{filter}'")

        result.to_csv('data.csv', index=False)

        return result.to_dict(orient='records')
    else :
        raise HTTPException(400, "Password Salah! Coba lagi")
        
    

