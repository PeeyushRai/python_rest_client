import requests
import json

URL = "http://127.0.0.1:5000"
CREATE_PRODUCT_ENDPOINT = "/product"

product_data = {
  'name': 'test2',
  'brand_name': 'test_brand2',
  'barcode': 123444,
  'description': 'test description 2',
  'image_thumbnail_url': 'aa2',
  'image_hires_url': 'bb2'
}

json_data = json.dumps(product_data)

print("This is data")
print(product_data)

print ("This is json data")
print (json_data)

r = requests.post(url = URL+CREATE_PRODUCT_ENDPOINT, json = product_data)

response_text = r.text
#print ("Response text is ",response_text)



