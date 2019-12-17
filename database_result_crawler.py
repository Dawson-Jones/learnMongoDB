# import os
# import sys
import csv
from pymongo import MongoClient

client = MongoClient("mongodb://root:123456@192.168.1.7:27017")
db = client['tttt']
collection = db['panel']

# current_path = os.path.split(sys.argv[0])[0]


def gen_csv():
    res = collection.find({}, {"_id": 0, "barcode": 1, "ap_result": 1, "status": 1})
    """
    {
        'status': [
            {'result': 'NG', 'by': 'AI'}, 
            {'result': 'NG', 'by': 'OP'}
        ],
        'ap_result': 'NG', 
        'barcode': '000000'
    }
    """
    if not res:
        return
    csv_data = [
        ["barcode", "op_res", "ap_res"]
    ]

    for per_res in res:
        filed = list()
        barcode = per_res.get("barcode")
        filed.append(barcode) if barcode is not None else filed.append("null")
        status = per_res.get("status")
        # if not status:
        #     return
        for i in status:
            if i.get("by") == "OP":
                filed.append(i.get("result"))
        ap_res = per_res.get("ap_result")
        filed.append(ap_res) if ap_res is not None else filed.append("null")
        csv_data.append(filed)
        with open("./res.csv", "w", newline='', encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)


if __name__ == '__main__':
    gen_csv()
