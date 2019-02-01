import requests
import sys
import argparse
import csv
import json
#from bs4 import BeautifulSoup



def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='config.json')
    return parser

parser = createParser()
namespace = parser.parse_args (sys.argv[1:])


with open(namespace.config) as config_file:
    config = json.load(config_file)


f = open(config['log_file'], 'w')

with open(config['read_data'], newline='') as csvfile:
    data = csv.reader(csvfile)
    i = 1
    for row in data:
        comm = 'http://{}:{}@{}/Image/channels/1/Focus'.format(row[1], row[2], row[0])
        r = requests.get(comm)
        if r.status_code == 200:
            #y = BeautifulSoup(r.text, features="xml")
            #print(y.prettify())
            #titles = y.find_all('FocusStyle')
            #for title in titles:
                #if title.get_text() != "AUTO":
            payload = '<?xml version="1.0" encoding="UTF-8"?> <Focus version="1.0" xmlns="http://www.hikvision.com/ver10/XMLSchema"><FocusStyle>AUTO</FocusStyle> </Focus>'

            r = requests.put(comm, data = payload)
            if r.status_code == 200 :
                print("row ", i, " updated.")
                f.write("row {} updated, ip : {} \n".format(i, row[0]))
            else:
                f.write("focus already  auto mod or focus unavailable on camera, row : {}, ip :  {} \n".format(i, row[0]))
                print("focus already  auto mod or focus unavailable on camera, row : ", i)
        else:
            f.write("row : {}, wrong ip/login/psw, ip : {} \n".format(i,row[0]))
            print("wrong ip/login/psw, row : ", i)
        i += 1
