import firebase_admin
from firebase_admin import credentials, firestore, db
from selenium import webdriver
from selenium.webdriver.common.by import By
from MongoConn import col
Path= "/Users/xaviernavarro/Documents/seleniumChromeDrive/chromedriver"

cred = credentials.Certificate("/Users/xaviernavarro/PycharmProjects/SeleniumCelebrities/histcheck-b96d5-firebase-adminsdk-181vk-73f9e51ca7.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

user_ref = db.collection('Celebrities')

goodCompanies = []

companies = [

'3M Company', 'A.O. Smith Corp', 'Abbott Laboratories','AbbVie Inc.','ABIOMED Inc','Accenture plc','Activision Blizzard','Adobe Inc.','Advance Auto Parts','Advanced Micro Devices Inc',
 'AES Corp','AFLAC Inc','Agilent Technologies Inc','Air Products & Chemicals Inc','Akamai Technologies Inc','Alaska Air Group Inc', 'Albemarle Corp',

 ]

##Companies
CorpsPOB = []
placelessComapny = []
driver = webdriver.Chrome(Path)
for company in companies:
    driver.get("https://www.google.com/search?q=" + "where was " + company + " founded?")
    try:
        if (driver.find_element(By.CSS_SELECTOR, ".HwtpBd").text):
            place = driver.find_element(By.CSS_SELECTOR, ".HwtpBd").text
            place = str(place)
            place = ''.join([i for i in place if not i.isdigit()])
            if (place[0] == ' '):
                place = place.replace(' ', '')
            place = place.replace('January', '')
            place = place.replace('February', '')
            place = place.replace('March', '')
            place = place.replace('April', '')
            place = place.replace('May', '')
            place = place.replace('June', '')
            place = place.replace('July', '')
            place = place.replace('August', '')
            place = place.replace('September', '')
            place = place.replace('October', '')
            place = place.replace('November', '')
            place = place.replace('December', '')
            place = place.replace(', , ', '')
            place = place.replace(' , ', '')
            place = place.replace(' United States', '')

            if (place[0] == ','):
                place = place[2:]  # now t points to the new string 'll'
            if (len(place) > 0):
                print(place, company)
                goodCompanies.append(company)
                CorpsPOB.append(place)

                user_ref.add({
                    'name': str(company),
                    'POB': str(place)
                })
        else:
            print("not found")
    except:
        print(company + " had problems looking up for")
'''
data = {}
for i in range(len(POB)):
    data.setdefault(str(i), {})['name'] = names[i]
    data.setdefault(str(i), {})['POB'] = POB[i]

for i in data:
    print(data[i])
    rec_id1 = col.insert_one(data[i])

'''
dataCompanies = {}
for i in range(len(goodCompanies)):
    dataCompanies.setdefault(str(i), {})['name'] = goodCompanies[i]
    dataCompanies.setdefault(str(i), {})['POB'] = CorpsPOB[i]

