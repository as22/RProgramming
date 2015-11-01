import urllib
import re
from bs4 import BeautifulSoup


all_codes = open('zipcode.txt', 'r')

for code in all_codes:

	code = code.strip()
	url = "http://www.zillow.com/homes/for_rent/"+str(code)+"_rb/"

	print url
	page_html = urllib.urlopen(url).read()
	soup = BeautifulSoup(page_html,"html.parser")
	print (soup.prettify())
	property_listings = soup.findAll("div",{"class":"property-listing-data"})

	if(len(property_listings)>0):

		data_file_name = str(code)+".txt"
		data_file = open(data_file_name,'w')
		data_file.write("address,bed,bath,sq_ft,built,lot\n")
	else:
		continue

	for listing in property_listings:
		sq_ft      = "NA,"
		locality   = "NA,"
		addr       = "NA,"
		zip	       = "NA,"
		bed_bath   = "NA,"
		built_year = "NA,"
		lot_size   = "NA,"
		price	   = "NA,"
		data       = "NA,"
		year 	   = "NA,"
		lot  	   = "NA,"
		bed 	   = "NA,"
		baths      = "NA,"
		lot        = "NA,"
		price      = "NA,"
		year       = "NA,"
		beds	   = "NA,"

		locality   = listing.find("span",{"itemprop":"addressLocality"})
		addr       = listing.find("span",{"itemprop":"streetAddress"})
		zip        = listing.find("span",{"itemprop":"postalCode"})
		bed_bath   = listing.find("span",{"class":"beds-baths-sqft"})
		built_year = listing.find("span",{"class":"built-year"})
		lot_size   = listing.find("span",{"class":"lot-size"})
		price      = listing.find("dt",{"class":"price-large zsg-h2 zsg-content_collapsed"})

		if addr:
			addr =  addr.text + " "
		else:
			addr = "NA,"
		if locality:
			locality =  locality.text + " "
		else:
			locality = "NA,"
		if zip:
			zip = zip.text + ","
		else:
			zip = "NA,"
		if bed_bath:
			beds   = re.search(r'(\d+\.*\d*)\s+bds',bed_bath.text)
			baths  = re.search(r'(\d+\.*\d*)\s+ba', bed_bath.text)
			sq_ft  = re.search(r'([\d|\,]+)\s+sqft',bed_bath.text)

			if beds:
				beds =  beds.group(1) + ","
			else:
				beds =  "NA,"
			if baths:
				baths = baths.group(1) + ","
			else:
				baths =  "NA,"
			if sq_ft:
				sq_ft = sq_ft.group(1)
				sq_ft = sq_ft.replace(',','')
				sq_ft = sq_ft + ","
			else: sq_ft =  "NA,"
	
		if built_year:
			year = re.search(r'Built\s+(\d+)',built_year.text)
			if year:
				year = year.group(1) + ","
			else:
				year= "NA,"
		if lot_size:
			lot  = re.search(r'([\d|\,]+)\s+sqft\s+lot',lot_size.text)
			if lot:
				lot = lot.group(1)
				lot = lot.replace(',','')
				lot = lot + ","
			else:
				lot = "NA,"

		if price:
			price = re.search(r'\$([\d|\,]+)\/mo',price.text)
			if price:
				price = price.group(1)
				price = price.replace(',','')
				price = price + ","
			else: price = "NA,"

		if listing:
			#data = addr + locality + zip + beds + baths + year +  sq_ft + lot + price
			print addr, locality, zip, beds,baths,year,sq_ft,lot,price
			#data_file.write(data.encode('utf-8'))
			#data_file.write(string)
			#data_file.write("\n")