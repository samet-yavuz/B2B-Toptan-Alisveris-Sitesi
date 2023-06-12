import xml.etree.ElementTree as ET
tree = ET.parse('users.xml')
root = tree.getroot()
list = []
for str in root:
    list.append(dict(user=str[0].text,password=str[1].text))


def login(user_id, password):
    permission = False
    for i in list:
        if i['user'] == user_id and i['password'] == password:
            permission = True
    return permission



