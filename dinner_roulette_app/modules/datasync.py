"""handles the adding and pulling from datastore"""
import csv
import random
from modules.logger import logging
DINNER_FILE = "dinnerlist.csv"
all_dinners = []

class Dinner:
    def __init__(self, dinner_name, difficulty="Unknown", req_time="Unknown", tags=None):
        self.dinner_name = dinner_name
        #self.user = user
        self.difficulty = difficulty
        self.req_time = req_time 
        self.tags = tags
    def __str__(self):
        return f"[{self.dinner_name} : dificulty is {self.difficulty}, required time is {self.req_time}, tags :{self.tags}]"
    def __repr__(self):
        return f"[{self.dinner_name} : dificulty is {self.difficulty}, required time is {self.req_time}, tags :{self.tags}]"

def initiallize_all_stored_dinners():
    with open(DINNER_FILE, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            tagging = row["tags"].split(" - ") if row["tags"] else ""
            all_dinners.append(Dinner(row["name"],row["difficulty"],row["time"], tagging))
            line_count += 1
        print(f'Processed {line_count} lines.')
        print(f"new list = {all_dinners}")

def add_dinner(dinner_name, difficulty="Unknown", req_time="Unknown", tags=None):
    #add dinner
    all_dinners.append(Dinner(dinner_name, difficulty, req_time, tags))
    print("ALL DINNERS:")
    print(all_dinners)
    # back everything up
    with open(DINNER_FILE, mode='w') as csv_file:
        fieldnames = ['name', 'difficulty', 'time', 'tags']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in all_dinners:
            tags = " - ".join(item.tags)
            writer.writerow({'name':item.dinner_name, 'difficulty':item.difficulty, 'time':item.req_time, 'tags':tags })
    return {'name':dinner_name, 'difficulty':difficulty, 'time':req_time, 'tags':tags }

def get_random_dinner():
    return all_dinners[random.randrange(0, len(all_dinners))]

initiallize_all_stored_dinners()
