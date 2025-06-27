import requests

def fetch_data():
    
    try:
        url = "https://api.freeapi.ap/api/v1/public/quotes/quote/random"
        response = requests.get(url)
        result = response.json()
        if result['success']:
            author = result["data"]["author"]
            quote = result["data"]['content']
            print(f"{author} said: `{quote}`")
    
        else:
            print("Error")
    
    except Exception as e:
        print("Error:", e)  
          
    
fetch_data()
    