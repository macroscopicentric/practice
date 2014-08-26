#Unfunctional

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

# height_total = 0
# height_count = 0
# for person in people:
#     if 'height' in person:
#         height_total += person['height']
#         height_count += 1

# if height_count > 0:
#     average_height = height_total / height_count

#     print average_height
#     # => 120

#Functional
filtered_people = filter(lambda x: 'height' in x, people)
#Simpler and more pythonic alternative for finding total height:
# total_height_alt = sum([person['height'] for person in people])
height_average = reduce(lambda a, x: a + x,
    [person['height'] for person in filtered_people]) / len(filtered_people)
print height_average

#Better solution based on Mary's:
total_height_list = map(lambda x: x['height'], filter(lambda x: 'height' in x,
    people))
height_average = reduce(lambda a, x: a + x, total_height_list) / len(total_height_list)
print height_average