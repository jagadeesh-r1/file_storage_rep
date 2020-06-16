import pandas as pd
import json
column_names = ['path','image_name']
dataset = pd.read_csv('done_data.csv',names=column_names)

print(dataset)

final_1 = pd.DataFrame(index=range((dataset.shape)[0]),columns=['num','path','cat'])
final_2 = pd.DataFrame(index=range((dataset.shape)[0]),columns=['num','path','cat'])


category_dict = dict()
sub_category_dict = dict()

for ind in dataset.index:
    path = dataset['path'][ind]
    # print(path)
    category = path.split('/')[2]
    sub_category = path.split('/')[3]

    if len(category.split('_'))>1:
        category_dict[category] = ''.join(w[0].upper() for w in category.split('_'))
        category = ''.join(w[0].upper() for w in category.split('_'))
    else:
        category = category
    if len(sub_category.split('_'))>1:
        sub_category_dict[sub_category] = ''.join(w[0].upper() for w in sub_category.split('_'))
        sub_category = ''.join(w[0].upper() for w in sub_category.split('_'))
    else:
        sub_category = sub_category

    final_1['num'][ind] = ''
    final_1['path'][ind] = path + '/' + dataset['image_name']
    final_1['cat'][ind] = category

    
    final_2['num'][ind] = ''
    final_2['path'][ind] = path + '/' + dataset['image_name']
    final_2['cat'][ind] = sub_category

final_1.to_csv('category_dataset.csv')
final_2.to_csv('sub_category_dataset.csv')

with open('cat_dict.json','w')as f:
    json.dump(category_dict,f,indent=4)

with open('sub_cat_dict.json','w')as f:
    json.dump(sub_category_dict,f,indent=4)