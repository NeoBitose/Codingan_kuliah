from functools import reduce

list_data = ["william", "kurniawan", "dandy", "alif"]

hasil_map = list(map(lambda x: x.upper(), list_data))
hasil_reduce = reduce(lambda x,y: x + "_" + y, hasil_map)

print(f"list nama : {list_data}")
print(f"setelah diubah dengan map  : {hasil_map}")
print(f"digabung dengan reduce : {hasil_reduce}")



