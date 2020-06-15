import csv
import os

csv_file = open('data.csv','w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['path','image_name'])

for a,b,c in os.walk('eBay'):
	if len(c)>0:
		for i in c:
			csv_writer.writerow([a,i])

csv_file.close()

