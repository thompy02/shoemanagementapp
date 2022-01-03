from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

##"https://stockx.com/air-jordan-5-retro-moonlight-2021"



ShoeLink = input("paste your shoe link here")

driver.get(ShoeLink)

LastSale = driver.find_element_by_xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[2]/div[2]/div[1]/p[2]')

print(LastSale.text + " Is the Price of the last shoe sold")

BuyPrice = driver.find_element_by_xpath('//*[@id="main-content"]/div/section[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div/dl/dd')

print(BuyPrice.text + " Is the current Price to buy")

##ShoeSku = 

##this just removes the dollar sign from the scraped price allowing you to convert to a float
SalePrice1 = LastSale.text.translate({ord("$"):None})
SalePrice2 = SalePrice1.translate({ord(","):None})

PriceFormula = 1.2

PriceAdjustment = (float(SalePrice2) * float(PriceFormula))
## price adjustment doesnt work for shoes above 1000 dollars it seems

print("$" + str(PriceAdjustment) + " This is what you should sell this for.")


## code to allow for this python script to interact with the SQL database 



