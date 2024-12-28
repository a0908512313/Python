def swap(data, x, y):
  temp = data[x]
  data[x] = data[y]
  data[y] = temp


def one_bubble(data,end_index):
  for j in range(end_index):
    if data[j] > data[j+1]:
      swap(data, j, j+1)


data = [4,1,3,5,2]
data_count = len(data)


for i in range (data_count - 1):
  one_bubble(data, data_count - 1 - i)
  print("第",i + 1,"回合結果:",data)
  

print("排序結果:",data)