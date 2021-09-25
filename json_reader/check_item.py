import sys
import json


def check_json(code, data_file):
    def read_data(data_file):
        with open(data_file, 'r') as f:
            data = json.load(f)

        return data

    def read_idx(code):
        str_code = str(code)
        l = int(len(str_code) / 12)
        idx_list = []

        for i in range(l):
            idx_list.append(str_code[i * 12:(i + 1) * 12])

        return idx_list

    def get_info(data, idx_list):

        item_list = []

        for idx in idx_list:
            info_all = [item for item in data if item['id'] == idx]

            # some ids is not presented in product list
            if info_all == []:
                return item_list

            info = info_all[0]

            item_list.append(info)

        return item_list

    def calcu_score(item_list):

        scores = sum([item["env_score"] for item in item_list])

        return scores

    # read cleaned json data
    data = read_data(data_file)

    # translate id of product from QR code
    idx_list = read_idx(code)

    # get item/product information from id
    item_list = get_info(data, idx_list)

    # calculate score
    scores = calcu_score(item_list)

    return item_list, scores
