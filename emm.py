import csv

# open file
with open('AQI.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    max_pp = 200
    max_city = ''
    # read file row by row
    for row in reader:
        
        
        if row [2] != "AQI":
            if int(row[2]) < max_pp:
                max_pp = int(row[2])
                max_city = row [0]
                
        else:
            
            pass
                
    print( max_city + "空氣最好,"  + "AQI是" + str(max_pp))