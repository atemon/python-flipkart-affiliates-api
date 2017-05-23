import json
from atemon.flipkart import FlipkartApi

fk = FlipkartApi('joel0250g', '049f9f9072f148f4acbf86f9c86303fa')

#profile = fk.get_products_category_list()

categories = fk.get_products_category_dict()

# print json.dumps(categories)

for category_name in fk.get_category_names():
    # if category_name in ['desktops']:
    #     continue
    # url = fk.get_category_url(category_name)
    #  print json.dumps(fk.get_products_from_category(category_name))
    print(fk.get_products_from_category(category_name, in_stock=False))
    print(fk.new_url, fk.current_product_url)
    while fk.has_more_products():
        print(fk.new_url, fk.current_product_url)
        print(fk.get_next_products())

    break
