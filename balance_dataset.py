import pandas as pd

# columns = ['class','image','category']

dataset = pd.read_csv('to_do_data.csv')

counts = dataset['path'].value_counts()

print(counts)

median = counts.median()

total_sum = 0
higher_than_median_sum = 0
higher_than_median_count = 0 
for i in counts.iteritems():
    if i[1] > median:
        higher_than_median_count = higher_than_median_count + 1
        higher_than_median_sum = higher_than_median_sum + i[1]
    total_sum = total_sum + i[1]

print(higher_than_median_count,total_sum,higher_than_median_sum,total_sum-higher_than_median_sum)

head = (1000000 - (total_sum-higher_than_median_sum))/higher_than_median_count

print(head)

new_df = dataset.groupby('path').head(int(head))
# 107735
new_counts =  new_df['path'].value_counts()

for i in new_counts.iteritems():
    print(i[0],'--',i[1])

new_df.to_csv('done_data.csv',index=False,columns=None)