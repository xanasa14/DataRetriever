from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from MongoConn import col


Path= "/Users/xaviernavarro/Documents/seleniumChromeDrive/chromedriver"

names = [  "Donald Trump","Dwayne Johnson", "Mark Twain", "Henry Ford", "Humphrey Bogart",
          "Billie Holiday", "Elvis Presley", "Ernest Hemingway", "Marilyn Monroe",
          "John F Kennedy", "Bob Dylan","Muhammad Ali","Martin Luther King, Jr.",
          "Neil Armstrong", "Jimi Hendrix", "Billie Jean King", "Bill Gates", "Oprah Winfrey",
        "Monica Lewinsky", "Michael Jackson", "Britney Spears", "Johnny Depp",
           "Sarah Palin", "Barack Obama",
    "Abraham Lincoln", "George Washington", "Thomas Jefferson", "Samuel Adams"

]
'''
    'Apache Corporation','Apartment Investment & Management','Apple Inc.','Applied Materials Inc.', 'Aptiv PLC','Archer-Daniels-Midland Co',
  'Arista Networks','Arthur J. Gallagher & Co.', 'Assurant', 'AT&T Inc.','Atmos Energy','Autodesk Inc.','Automatic Data Processing','AutoZone Inc','AvalonBay Communities',
 'Avery Dennison Corp', 'Baker Hughes Co','Ball Corp','Bank of America Corp', 'Baxter International Inc.','Becton Dickinson', 'Berkshire Hathaway','Best Buy Co. Inc.','Bio-Rad Laboratories','Biogen Inc.',
 'BlackRock', 'Boeing Company', 'Booking Holdings Inc', 'BorgWarner','Boston Properties','Boston Scientific',
 'Bristol-Myers Squibb', 'Broadcom Inc.','Broadridge Financial Solutions', 'Brown-Forman Corp.','C. H. Robinson Worldwide','Cabot Oil & Gas', 'Cadence Design Systems', 'Campbell Soup','Capital One Financial', 'Cardinal Health Inc.',
 'Carmax Inc','Carnival Corp.','Carrier Global','Caterpillar Inc.','Cboe Global Markets','CBRE Group', 'CDW','Celanese','Centene Corporation',
 'CenterPoint Energy','CenturyLink Inc','Cerner','CF Industries Holdings Inc','Charles Schwab Corporation',

 'Charter Communications','Chevron Corp.','Chipotle Mexican Grill', 'Chubb Limited','Church & Dwight', 'CIGNA Corp.', 'Cincinnati Financial', 'Cintas Corporation','Cisco Systems','Citigroup Inc.',
 'Citizens Financial Group','Citrix Systems','CME Group Inc.','CMS Energy','Coca-Cola Company','Cognizant Technology Solutions',
 'Colgate-Palmolive', 'Comcast Corp.', 'Comerica Inc.','Conagra Brands','Concho Resources', 'ConocoPhillips','Consolidated Edison',
 'Constellation Brands','Copart Inc','Corning Inc.','Corteva', 'Costco Wholesale Corp.', 'Coty Inc','Crown Castle International Corp.', 'CSX Corp.', 'Cummins Inc.','CVS Health', 'D. R. Horton',
 'Danaher Corp.', 'Darden Restaurants','DaVita Inc.', 'Deere & Co.','Delta Air Lines Inc.','Dentsply Sirona','Devon Energy', 'DexCom','Diamondback Energy', 'Digital Realty Trust Inc','Discover Financial Services', 'Discovery Inc. (Class A)',
 'Discovery Inc. (Class C)', 'Dish Network', 'Dollar General', 'Dollar Tree', 'Dominion Energy', "Domino's Pizza",'Dover Corporation', 'Dow Inc.','DTE Energy Co.','Duke Energy','Duke Realty Corp',
 'DuPont de Nemours Inc','DXC Technology','E*Trade','Eastman Chemical','Eaton Corporation','eBay Inc.','Ecolab Inc.', "Edison Int'l",'Edwards Lifesciences','Electronic Arts',
 'Emerson Electric Company','Entergy Corp.','EOG Resources','Equifax Inc.','Equinix','Equity Residential','Essex Property Trust Inc.', 'Estee Lauder Companies','Everest Re Group Ltd.','Evergy','Eversource Energy',
 'Exelon Corp.','Expedia Group', 'Expeditors','Extra Space Storage','Exxon Mobil Corp.','F5 Networks','Facebook Inc.', 'Fastenal Co','Federal Realty Investment Trust',
 'FedEx Corporation','Fidelity National Information Services', 'Fifth Third Bancorp','First Republic Bank', 'FirstEnergy Corp', 'Fiserv Inc', 'FleetCor Technologies Inc', 'FLIR Systems',
 'Flowserve Corporation', 'FMC Corporation','Ford Motor Company', 'Fortinet','Fortive Corp', 'Fortune Brands Home & Security','Fox Corporation','Franklin Resources','Freeport-McMoRan Inc.','Gap Inc.','Garmin Ltd.','Gartner Inc','General Dynamics','General Electric',
 'General Mills','General Motors','Genuine Parts','Gilead Sciences','Global Payments Inc.','Globe Life Inc.','Goldman Sachs Group','Grainger (W.W.) Inc.',
 'H&R Block','Halliburton Co.','Hanesbrands Inc','Hartford Financial Svc.Gp.','Hasbro Inc.','HCA Healthcare', 'Healthpeak Properties', 'Henry Schein','Hess Corporation', 'Hewlett Packard Enterprise','Hilton Worldwide Holdings Inc','HollyFrontier Corp','Hologic',
 'Home Depot',"Honeywell Int'l Inc.",'Hormel Foods Corp.','Host Hotels & Resorts', 'Howmet Aerospace','HP Inc.','Humana Inc.','Huntington Bancshares','Huntington Ingalls Industries',
 'IDEX Corporation', 'IDEXX Laboratories','IHS Markit Ltd.','Illinois Tool Works','Illumina Inc', 'Incyte', 'Ingersoll Rand', 'Intel Corp.', 'International Paper',
 'Interpublic Group','Intuit Inc.', 'Intuitive Surgical Inc.','Invesco Ltd.','IPG Photonics Corp.','IQVIA Holdings Inc.','Iron Mountain Incorporated','J. B. Hunt Transport Services', 'Jack Henry & Associates',
'Jacobs Engineering Group','JM Smucker','Johnson & Johnson','Johnson Controls International',
 'JPMorgan Chase & Co.','Juniper Networks', 'Kansas City Southern', 'Kellogg Co.', 'KeyCorp', 'Keysight Technologies','Kimberly-Clark',
 'Kimco Realty', 'Kinder Morgan', 'KLA Corporation', "Kohl's Corp.",'Kraft Heinz Co', 'Kroger Co.','L Brands Inc.', 'L3Harris Technologies', 'Laboratory Corp. of America Holding','Lam Research',
 'Lamb Weston Holdings Inc', 'Las Vegas Sands', 'Leggett & Platt', 'Leidos Holdings', 'Lennar Corp.', 'Lilly (Eli) & Co.', 'Lincoln National', 'Linde plc', 'Live Nation Entertainment', 'LKQ Corporation', 'Lockheed Martin Corp.', 'Loews Corp.',
 "Lowe's Cos.", 'LyondellBasell','M&T Bank Corp.','Marathon Oil Corp.','Marathon Petroleum', 'MarketAxess',"Marriott Int'l.", 'Marsh & McLennan',
 'Martin Marietta Materials','Masco Corp.','Mastercard Inc.', 'Maxim Integrated Products Inc', 'McCormick & Co.', "McDonald's Corp.", 'McKesson Corp.', 'Medtronic plc',
 'Merck & Co.', 'MetLife Inc.','Mettler Toledo', 'MGM Resorts International','Microchip Technology', 'Micron Technology',
 'Microsoft Corp.', 'Mid-America Apartments', 'Mohawk Industries', 'Molson Coors Beverage Company', 'Mondelez International', 'Monster Beverage', "Moody's Corp", 'Morgan Stanley', 'Motorola Solutions Inc.',
 'MSCI Inc', 'Mylan N.V.', 'Nasdaq Inc.', 'National Oilwell Varco Inc.', 'NetApp', 'Netflix Inc.', 'Newell Brands','Newmont Corporation', 'News Corp. Class A',
 'News Corp. Class B', 'NextEra Energy','Nielsen Holdings', 'Nike Inc.','NiSource Inc.','Noble Energy', 'Norfolk Southern Corp.','Northern Trust Corp.','Northrop Grumman',
 'NortonLifeLock','Norwegian Cruise Line Holdings','NRG Energy', 'Nucor Corp.', 'Nvidia Corporation', 'NVR Inc.', "O'Reilly Automotive", 'Occidental Petroleum','Old Dominion Freight Line',
 'Omnicom Group', 'ONEOK','Oracle Corp.', 'Otis Worldwide', 'PACCAR Inc.','Packaging Corporation of America', 'Parker-Hannifin', 'Paychex Inc.', 'Paycom','PayPal', 'Pentair plc',
 "People's United Financial",'PepsiCo Inc.', 'PerkinElmer','Perrigo', 'Pfizer Inc.', 'Philip Morris International',
 'Phillips 66','Pinnacle West Capital', 'Pioneer Natural Resources', 'PNC Financial Services', 'PPG Industries','PPL Corp.', 'Principal Financial Group', 'Procter & Gamble','Progressive Corp.', 'Prologis', 'Prudential Financial', 'Public Service Enterprise Group (PSEG)','Public Storage','PulteGroup','PVH Corp.', 'Qorvo', 'QUALCOMM Inc.',

'Quanta Services Inc.', 'Quest Diagnostics', 'Ralph Lauren Corporation', 'Raymond James Financial Inc.','Raytheon Technologies', 'Realty Income Corporation','Regency Centers Corporation', 'Regeneron Pharmaceuticals',
 'Regions Financial Corp.', 'Republic Services Inc', 'ResMed', 'Robert Half International', 'Rockwell Automation Inc.', 'Rollins Inc.',
 'Roper Technologies', 'Ross Stores', 'Royal Caribbean Group', 'S&P Global Inc.', 'Salesforce.com', 'SBA Communications', 'Schlumberger Ltd.', 'Seagate Technology', 'Sealed Air', 'Sempra Energy', 'ServiceNow', 'Sherwin-Williams',
 'Simon Property Group Inc', 'Skyworks Solutions', 'SL Green Realty','Snap-on', 'Southern Company',
 'Southwest Airlines', 'Stanley Black & Decker', 'Starbucks Corp.', 'State Street Corp.', 'STERIS plc', 'Stryker Corp.','SVB Financial',
  'Synchrony Financial', 'Synopsys Inc.', 'Sysco Corp.', 'T-Mobile US','T. Rowe Price Group', 'Take-Two Interactive','Tapestry Inc.','Target Corp.','TE Connectivity Ltd.', 'TechnipFMC', 'Teledyne Technologies', 'Teleflex', 'Texas Instruments', 'Textron Inc.','The Bank of New York Mellon','The Clorox Company', 'The Cooper Companies', 'The Hershey Company', 'The Mosaic Company','The Travelers Companies Inc.','The Walt Disney Company',
 'Thermo Fisher Scientific', 'Tiffany & Co.', 'TJX Companies Inc.', 'Tractor Supply Company', 'Trane Technologies plc', 'TransDigm Group','Truist Financial', 'Twitter Inc.', 'Tyler Technologies',
 'Tyson Foods', 'U.S. Bancorp', 'UDR Inc.', 'Ulta Beauty', 'Union Pacific Corp', 'United Airlines Holdings','United Health Group Inc.',
 'United Parcel Service', 'United Rentals Inc.','Universal Health Services','Unum Group', 'Valero Energy','Varian Medical Systems', 'Ventas Inc', 'Verisign Inc.', 'Verisk Analytics', 'Verizon Communications',
 'Vertex Pharmaceuticals Inc','VF Corporation', 'ViacomCBS','Visa Inc.', 'Vornado Realty Trust',
 'Vulcan Materials', 'W. R. Berkley Corporation', 'Wabtec Corporation', 'Walgreens Boots Alliance', 'Walmart','Waste Management Inc.',
 'Waters Corporation','WEC Energy Group','Wells Fargo', 'Welltower Inc.', 'West Pharmaceutical Services', 'Western Digital', 'Western Union Co', 'WestRock', 'Weyerhaeuser', 'Whirlpool Corp.', 'Williams Companies', 'Willis Towers Watson', 'Wynn Resorts Ltd', 'Xcel Energy Inc','Xerox','Xilinx', 'Xylem Inc.',
 'Yum! Brands Inc', 'Zebra Technologies', 'Zimmer Biomet Holdings','Zions Bancorp','Zoetis'

'''
goodCompanies = []

companies = [

'3M Company', 'A.O. Smith Corp', 'Abbott Laboratories','AbbVie Inc.','ABIOMED Inc','Accenture plc','Activision Blizzard','Adobe Inc.','Advance Auto Parts','Advanced Micro Devices Inc',
 'AES Corp','AFLAC Inc','Agilent Technologies Inc','Air Products & Chemicals Inc','Akamai Technologies Inc','Alaska Air Group Inc', 'Albemarle Corp',





 ]

'''
'Alexandria Real Estate Equities','Alexion Pharmaceuticals','Align Technology','Allegion','Alliant Energy Corp', 'Allstate Corp','Alphabet Inc. (Class A)','Alphabet Inc. (Class C)','Altria Group Inc', 'Amazon.com Inc.','Amcor plc','Ameren Corp', 'American Airlines Group','American Electric Power',
 'American Express Co','American International Group', 'American Tower Corp.', 'American Water Works Company Inc','Ameriprise Financial', 'AmerisourceBergen Corp', 'AMETEK Inc.', 'Amgen Inc.', 'Amphenol Corp','Analog Devices Inc.',
 'ANSYS', 'Anthem','Aon plc',
'''

POB = []
#names
#driver = webdriver.Chrome(Path)
'''
for name in names:
    driver.get("https://www.google.com/search?q=" + "where was " +name + " born?")
    try:
        if(driver.find_element(By.CSS_SELECTOR, ".Z0LcW").text):
            place = driver.find_element(By.CSS_SELECTOR, ".Z0LcW").text
        elif(driver.find_element_by_class_name("FLP8od")):
            print("OK")
        else:
            print("not found")
    except:
        print(name + " had problems looking up for")
    print(place)
    POB.append(place)
'''
##Companies
CorpsPOB = []
placelessComapny=  []
driver = webdriver.Chrome(Path)
for company in companies:
    driver.get("https://www.google.com/search?q=" + "where was " + company + " founded?")
    try:
        if(driver.find_element(By.CSS_SELECTOR, ".HwtpBd").text):
            place = driver.find_element(By.CSS_SELECTOR, ".HwtpBd").text
            place = str (place)
            place = ''.join([i for i in place if not i.isdigit()])
            if (place[0] == ' '):
                place = place.replace(' ', '')
            place = place.replace('January','')
            place = place.replace('February','')
            place = place.replace('March','')
            place = place.replace('April','')
            place = place.replace('May','')
            place = place.replace('June','')
            place = place.replace('July','')
            place = place.replace('August','')
            place = place.replace('September','')
            place = place.replace('October','')
            place = place.replace('November','')
            place = place.replace('December','')
            place = place.replace(', , ', '')
            place = place.replace(' , ', '')
            place = place.replace(' United States', '')

            if (place[0] == ','):
                place = place[2:]  # now t points to the new string 'll'
            if (len(place) > 0):
                print(place, company)
                goodCompanies.append(company)
                CorpsPOB.append(place)

        else:
            print("not found")
    except:
        print(company + " had problems looking up for")

'''
size = len(names)
if(len(names) == len(POB)):
    print("same size", len(names))
else:
    print("it is not the same size")
    print(len(names))
    print(len(POB))
'''
size = len(companies)
if(len(goodCompanies) == len(CorpsPOB)):
    print("same size", len(companies))
else:
    print("it is not the same size")
    print(len(companies))
    print(len(CorpsPOB))




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



for i in dataCompanies:
    print(dataCompanies[i])

    rec_id1 = col.insert_one(dataCompanies[i])
