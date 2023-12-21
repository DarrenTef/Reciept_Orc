import json
import pickle
import requests

url = "https://ocr.asprise.com/api/v1/receipt"

def image_to_json(image_file, json_result_path):
    res = requests.post(url,
                        data = {
                            'api_key': 'TEST',
                            'recognizer': 'auto',
                            'ref_no': 'oct_python_123'
                        },
                        files = {
                            'file': open(image_file, 'rb')
                        })

    with open(json_result_path, "w") as f:
        json.dump(json.loads(res.text), f)

def receipt_processesor(file_path_json, file_path_result):
    with open(file_path_json, "r") as f:
        data = json.load(f)

    receipts = data['receipts'][0]
    items = receipts[0]['items']
    with open(file_path_result, "w") as f:
        for item in items:
            description = item['description']
            amount = item['amount']
            f.write((f"{description.ljust(30)} {str(amount).rjust(20)}\n"))



# subtotal = receipts[0]['subtotal']
# print(f"Your subtotal:{str(subtotal).rjust(20)}")
# print(f"Your purcahse at {data['receipts'][0]['merchant_name']}")