import json
from jsoncomment import JsonComment


def disease():
    dis = []

    with open('disease.json', encoding='utf-8') as data_file:
        parser = JsonComment(json)
        data = parser.load(data_file)

    for a in range(0, len(data['child'])):
        if len(data['child'][a]['child']) != 0:
            for b in range(0, len(data['child'][a]['child'])):
                if len(data['child'][a]['child'][b]['child']) != 0:
                    for c in range(0, len(data['child'][a]['child'][b]['child'])):
                        if len(data['child'][a]['child'][b]['child'][c]['child']) != 0:
                            for d in range(0, len(data['child'][a]['child'][b]['child'][c]['child'])):
                                if len(data['child'][a]['child'][b]['child'][c]['child'][d]['child']) != 0:
                                    pass
                                else:
                                    dis.append(data['child'][a]['child'][b]['child'][c]['child'][d]['name'])
                        else:
                            dis.append(data['child'][a]['child'][b]['child'][c]['name'])
                else:
                    dis.append(data['child'][a]['child'][b]['name'])
        else:
            dis.append(data['child'][a]['name'])

    return dis
