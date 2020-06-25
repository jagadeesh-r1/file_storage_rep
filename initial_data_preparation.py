import csv
import os

csv_file = open('to_do_data.csv','w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['path','image_name'])

for a,b,c in os.walk('eBay'):  # change the marketplace accordingly.
	if len(c)>0:
		for i in c:
			csv_writer.writerow([a,i])  # writes path and names of the image files in the directory.

csv_file.close()

