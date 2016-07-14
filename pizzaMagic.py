import requests
import json

Order = '{"Address":{"Street":"5760 HASTINGS ST","City":"BURNABY","Region":"BRITISH COLUMBIA","PostalCode":"V5B1R6","Type":"House","StreetNumber":"5760","StreetName":"HASTINGS ST","UnitNumber":"Apartment 23"},"Coupons":[{"Code":"3203","Qty":1,"ID":3}],"CustomerID":"","Email":"himanshugarg.garg8@gmail.com","Extension":"","LanguageCode":"en","OrderChannel":"OLO","OrderID":"","OrderMethod":"Web","OrderTaker":null,"Payments":[],"Products":[{"Code":"P12IPAZA","Qty":1,"ID":2,"Instructions":"","isNew":false,"Options":{"C":{"1/1":"1"},"P":{"2/2":"1"},"D":{"1/1":"1"},"O":{"1/2":"1"},"X":{"1/1":"1"}}}],"SourceOrganizationURI":"order.dominos.ca","StoreID":"10080","Tags":{},"Version":"1.0","NoCombine":true,"Partners":{}}'


uri= "https://order.dominos.ca/power/place-order"
headers= {
            'Referer':'https://order.dominos.ca/en/pages/order/',
            'Content-Type': 'application/json'
        }


r = requests.post(uri, data=Order, headers=headers)
print(r.content)

	
