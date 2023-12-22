my_arrays = []
my_set = set()
def get_next_number(arrays, seed_num):
    for array in arrays:
        if seed_num >= array[1] and seed_num <= array[1] + array[2]:
            amount_to_increase = seed_num - array[1]
            return array[0] + amount_to_increase
    return seed_num

with open('input.txt', 'r') as file:
    content = file.read()

split_by_category = content.split("\n\n")

for line in split_by_category:
    array_of_numbers = []
    words = line.split("\n")
    for word in words:
        nums = word.split(" ")
        smaller_array = []
        for num in nums:
            if num.isdigit():
                smaller_array.append(int(num))
        if smaller_array:
            array_of_numbers.append(smaller_array)
    my_arrays.append(array_of_numbers)

seeds = my_arrays[0][0]
seed_to_soil_map = my_arrays[1]
soil_to_fertilizer_map = my_arrays[2]
fertilizer_to_water_map = my_arrays[3]
water_to_light_map = my_arrays[4]
light_to_temperature_map = my_arrays[5]
temperature_to_humidity_map = my_arrays[6]
humidity_to_location_map = my_arrays[7]


print(my_set)
final_location = -1

for x in range(len(my_set)):
    location = get_next_number(seed_to_soil_map, my_set[x])
    location = get_next_number(soil_to_fertilizer_map, location)
    location = get_next_number(fertilizer_to_water_map, location)
    location = get_next_number(water_to_light_map, location)
    location = get_next_number(light_to_temperature_map, location)
    location = get_next_number(temperature_to_humidity_map, location)
    location = get_next_number(humidity_to_location_map, location)

    if final_location == -1:
        final_location = location
    elif (location < final_location):
        final_location = location

print(final_location)