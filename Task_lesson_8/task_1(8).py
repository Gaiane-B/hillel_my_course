# Function connect two tuples into one dict

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def tuples_into_dict(key_element, value_element):
    result = dict(zip(key_element, value_element))
    return result
