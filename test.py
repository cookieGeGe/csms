def dict_deal(dict_data):
    temp = {}
    for key, value in dict_data.items():
        if isinstance(value, dict):
            temp[key.lower()] = dict_deal(value)
        elif isinstance(value, list):
            temp[key.lower()] = deal_list(value)
        else:
            temp[key.lower()] = value
    return temp


def deal_list(data_list):
    temp = []
    for i, item in enumerate(data_list):
        if isinstance(item, dict):
            item = dict_deal(item)
        elif isinstance(item, list):
            item = deal_list(item)
        else:
            item = item
        temp.append(item)
    return temp


if __name__ == '__main__':
    dict_data = {
        'A': 'a',
        'B': ['a', {
            'C': 12
        }],
        'D': {
            "E": 'e',
            "F": [1, 2,{
                "G":123
            }]
        }
    }
    list_data = [dict_data] * 3
    print(dict_deal(dict_data))
    print(deal_list(list_data))
