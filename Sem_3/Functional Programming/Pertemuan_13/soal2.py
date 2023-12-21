from functools import reduce

list_data = [5,1,3,4,6,5,2,7,9,3,1,7,5,2,4]

hasil_filter = list(filter(lambda x: x > 4, list_data))
hasil_reduce = reduce(lambda x,y: x + y, hasil_filter)

print(f"list angka : {list_data}")
print(f"setelah difilter > 4 : {hasil_filter}")
print(f"setelah direduce menambahkan hasil filter : {hasil_reduce}")






