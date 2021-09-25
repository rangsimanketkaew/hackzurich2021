import sys
from check_item import check_json 

def main():

    code = "106506500000104403200000220622085000" 
    #code = "106506500000104403200000220622085001"

    data_file = 'products.json'
    item_list, scores = check_json(code, data_file)

    print(item_list)
    print("-----------------------------------")
    print("Env. scores: %s" % scores)

if __name__ == "__main__":
    main()
