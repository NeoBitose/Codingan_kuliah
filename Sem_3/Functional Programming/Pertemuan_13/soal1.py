from functools import reduce

list_data = ["william", "kurniawan", "dandy", "alif"]

hasil_sort = sorted(list_data)
hasil_reduce = reduce(lambda x,y: x + "_" + y, hasil_sort)

print(f"list nama : {list_data}")
print(f"setelah diurutkan  : {hasil_sort}")
print(f"digabung dengan reduce : {hasil_reduce}")





