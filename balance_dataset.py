import pandas as pd

dataset = pd.read_csv('to_do_data.csv')  # datasets which contain all the paths and names of images.

counts = dataset['path'].value_counts()  # count of the different categories.

# print(counts)  

median = counts.median()  # calculating the median for all counts.

total_sum = 0
higher_than_median_sum = 0
higher_than_median_count = 0 

for i in counts.iteritems():
    if i[1] > median:
        higher_than_median_count = higher_than_median_count + 1
        higher_than_median_sum = higher_than_median_sum + i[1]
    total_sum = total_sum + i[1]

# print(higher_than_median_count,total_sum,higher_than_median_sum,total_sum-higher_than_median_sum)

head = (1000000 - (total_sum-higher_than_median_sum))/higher_than_median_count  # the cap to which every category gets shortened.

# print(head)

new_df = dataset.groupby('path').head(int(head))  # Capping the rows.

new_counts =  new_df['path'].value_counts()

# for i in new_counts.iteritems():
    # print(i[0],'--',i[1])

new_df.to_csv('image_dataset.csv',index=False,columns=None)  # dumping new dataset into csv.