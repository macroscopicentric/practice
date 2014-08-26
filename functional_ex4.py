#Unfunctional:
bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

# def format_bands(bands):
#     for band in bands:
#         band['country'] = 'Canada'
#         band['name'] = band['name'].replace('.', '')
#         band['name'] = band['name'].title()

# format_bands(bands)

# print bands
# # => [{'name': 'Sunset Rubdown', 'active': False, 'country': 'Canada'},
# #     {'name': 'Women', 'active': False, 'country': 'Canada' },
# #     {'name': 'A Silver Mt Zion', 'active': True, 'country': 'Canada'}]

#Functional:

def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def set_canada_as_country(band):
    return assoc(band, 'country', "Canada")

def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))

def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())

def pipeline_each(band_data, to_do):
    if not to_do:
        return band_data
    else:
        return pipeline_each(map(to_do[0], band_data), to_do[1:])

#Mary's solution:
# def pipeline_each(data, fns):
#     return reduce(lambda a, x: map(x, a),
#                   fns,
#                   data)

print pipeline_each(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names])