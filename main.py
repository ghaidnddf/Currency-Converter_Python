import requests
from datetime import datetime
def get_rates(url):
    try:
        response= requests.get(url)
        if response.status_code == 200:
             data= response.json()
             rates= data.get("rates")
             return rates
    except Exception as e:
        print(f"Error :{e}")
    return None

url_input = input("type the url code here : ")
fetch= get_rates(url_input)


if fetch != None:
    print("✅ The URL is valid\n")
    print("Current Dollar's rate to the Euro is {}".format(fetch['USD']))
    moneyType= input("Type the target currency (e.g. USD, TRY):").upper()
    amount =None
    while amount is None :
       try:
        amount= float(input("type the amount type here : "))
       except ValueError:
          print("you have to enter a numeric value")
          continue
    if fetch.get(moneyType) != None:
        print("the exchange rate is valid\n")
        print("your money type is {} to the Euro".format(fetch[moneyType]))
        result=amount*fetch[moneyType]
        print("your amount to the Euro is {:.2f}".format(result))
        with open("history.txt", "a", encoding="utf-8") as file:
            now = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            file.write(" [ {} ] converted {} EUR to {:.2f} {} ".format(now,amount,result,moneyType))
    else:
        print("❌ Currency code not found.")
else:
    print("❌ Invalid URL or Connection Error")
#https://api.exchangerate-api.com/v4/latest/EUR