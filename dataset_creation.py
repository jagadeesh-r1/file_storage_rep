import pandas as pd
import json
import csv

column_names = ['path','image_name']
dataset = pd.read_csv('image_dataset.csv',names=column_names)  # dataset containing paths and names of the images

level_0_csv_file = open('level_0_category_dataset.csv','w')  # level 0 category dataset
level_0_csv_writer = csv.writer(level_0_csv_file)

category_dict = dict()  # dictionaries which will house the acronyms of categories
sub_category_dict = dict()  # dictionaries which will house the acronyms of sub categories

for ind in dataset.index:
    path = dataset['path'][ind]
    category = path.split('/')[2]
    sub_category = path.split('/')[3]
    
    level_1_csv_file = open('{0}_dataset.csv'.format(category),'a+')
    level_1_csv_writer = csv.writer(level_1_csv_file)

    if len(category.split('_'))>1:
        acronym = ''
        for w in category.split('_'):
            if w!='':
                acronym = acronym + w[0].upper()
        category_dict[category] = acronym
        category = acronym
    else:
        category = category
    level_0_csv_writer.writerow(['','gs://crawling_testing/images/2020/5/'+path + '/' + dataset['image_name'][ind],category])

    if len(sub_category.split('_'))>1:
        acronym = ''
        for w in sub_category.split('_'):
            if w!='':
                acronym = acronym + w[0].upper()
        sub_category_dict[sub_category] = acronym
        sub_category = acronym
    else:
        sub_category = sub_category
    level_1_csv_writer.writerow(['',"gs://crawling_testing/images/2020/5/" + path + '/' + dataset['image_name'][ind],sub_category])
    level_1_csv_file.close()

level_0_csv_file.close()

with open('cat_acronym_dict.json','w')as f:
    json.dump(category_dict,f,indent=4)

with open('subcat_acronym_dict.json','w')as f:
   json.dump(sub_category_dict,f,indent=4)
