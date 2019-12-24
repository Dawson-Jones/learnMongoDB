import csv
from pymongo import MongoClient

# MongoDB的客户端
client = MongoClient("localhost", 27017)
db = client['tttt']
# collection 相当于 table
print('anus')
with open('./SETUP/permission.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    """
    OrderedDict([
    ('type', 'super_admin'), 
    ('user_mng', '1'), 
    ('line_mng', '1'), 
    ('gui_mng', '1'), 
    ('threshold_mng', '1'),
    ('shift_mng', '1'), 
    ('pic_upload', '1'), 
    ('update_time', '0')])
    """
    for i in reader:
        for key in i.keys():
            if i[key] == '0' or i[key] == '1':
                i[key] = int(i[key])
        # i['level_mng'] = int(i['level_mng'])
        # i['user_mng'] = int(i['user_mng'])
        # i['display_mode'] = int(i['display_mode'])
        # i['ai_module'] = int(i['ai_module'])
        # i['threshold'] = int(i['threshold'])
        # i['el_gui'] = int(i['el_gui'])
        # i['auto_manual'] = int(i['auto_manual'])
        # i['shift_mng'] = int(i['shift_mng'])
        # i['pic_upload'] = int(i['pic_upload'])
        try:
            AD = db.permission.find_one({"type": i["type"]})
            if AD:
                db.permission.replace_one({"type": i["type"]}, i)
            else:
                db.permission.insert_one(i)
        except BaseException:
            pass

with open('./SETUP/user.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for i in reader:
        i['activate'] = int(1)
        try:
            AD = db.user.find_one({"user_name": i["user_name"], 'activate': 1})
            if AD:
                db.user.replace_one({"user_name": i["user_name"], 'activate': 1}, i)
            else:
                db.user.insert_one(i)
        except BaseException:
            pass

with open('./SETUP/el_config.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for i in reader:
        i['cell_amount'] = int(i['cell_amount'])
        i['display_mode'] = int(i['display_mode'])
        i['cr_module'] = int(i['cr_module'])
        i['cs_module'] = int(i['cs_module'])
        i['mr_module'] = int(i['mr_module'])
        i['bc_module'] = int(i['bc_module'])
        i['br_module'] = int(i['br_module'])
        i['bb_module'] = int(i['bb_module'])
        i['update_time'] = int(i['update_time'])

        if 'threshold_switch' in i.keys():
            i['threshold_switch'] = int(i['threshold_switch'])
        else:
            i['threshold_switch'] = 0
        # if old_thresh:
        try:
            i['thresholds'] = i['thresholds'].replace("’", "'")
            i['thresholds'] = i['thresholds'].replace("‘", "'")
            i['thresholds']['cr']['corner_detection'] = int(i['thresholds']['cr']['corner_detection'])
        except BaseException:
            pass
        try:
            i['thresholds'] = eval(i['thresholds'])
            i['thresholds']["update_time"] = 0
            list_set = []
            cell = i['cell_amount'] / 6
            for x in range(6):
                for y in range(int(cell)):
                    list_set.append([x, y])
            for z in range(1, 6):
                i['thresholds']['cr']['cell_set'][z]['set'] = []
                i['thresholds']['cs']['cell_set'][z]['set'] = []
            i['thresholds']['cr']['cell_set'][0]['set'] = list_set
            i['thresholds']['cs']['cell_set'][0]['set'] = list_set

        except BaseException:
            pass
        import json

        with open('anus.json') as anus:
            test = json.load(anus)
            i['thresholds'] = test['thresholds']

        from pprint import pprint

        pprint(i)
        # except BaseException:
        # pass
        try:
            AD = db.el_config.find_one({"el_no": i["el_no"]})
            if AD:
                db.el_config.replace_one({"el_no": i["el_no"]}, i)
            else:
                db.el_config.insert_one(i)
        except BaseException:
            pass

with open('./SETUP/el_string.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for i in reader:
        i['cell_amount'] = int(i['cell_amount'])
        try:
            AD = db.el_string.find_one({"string_line": i["string_line"]})
            if AD:
                db.el_string.replace_one({"string_line": i["string_line"]}, i)
            else:
                db.el_string.insert_one(i)
        except BaseException:
            pass

with open('./SETUP/gui_config.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for i in reader:
        # print(i['gui_no'])
        i['auto_time'] = int(i['auto_time'])
        i['manual_time'] = int(i['manual_time'])
        i['el_limit'] = int(i['el_limit'])
        try:
            AD = db.gui_setting.find_one({"gui_no": i["gui_no"]})
            if AD:
                db.gui_setting.replace_one({"gui_no": i["gui_no"]}, i)
            else:
                db.gui_setting.insert_one(i)
        except BaseException:
            pass
