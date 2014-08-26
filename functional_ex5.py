bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def call(fn, key):
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))
    return apply_fn

def custom_pluck(list_of_keys):
    def pluck_helper(band):
        temp_dict = {}
        for key in list_of_keys:
            temp_dict = assoc(temp_dict, key, band[key])
        return temp_dict
    return pluck_helper

def pluck(list_of_keys):
    def pluck_helper(band):
        return reduce(lambda a, key: assoc(a, key, band[key]), list_of_keys, {})
    return pluck_helper












#Mary's code:
# def pluck(keys):
#     def pluck_fn(record):
#         return reduce(lambda a, x: assoc(a, x, record[x]),
#                       keys,
#                       {})
#     return pluck_fn

def pipeline_each(band_data, to_do):
    if not to_do:
        return band_data
    else:
        return pipeline_each(map(to_do[0], band_data), to_do[1:])

edited_bands = pipeline_each(bands, [call(lambda x: 'Canada', 'country'),
                                    call(lambda x: x.replace('.', ''), 'name'),
                                    call(str.title, 'name'),
                                    pluck(['name', 'country'])])
#Step one: for loop.
#Step two: mapping.
# finished_bands = map(lambda x: pluck(x, ['name', 'country']), edited_bands)

print edited_bands