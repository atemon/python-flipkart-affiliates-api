Python wrapper for Flipkart affiliates API
==========================================

&copy; 2017 ATEMON Technology Consultants LLP<br>
License: MIT License (modified)<br>
Website: http://www.atemon.com</a><br>
Author: Varghese Chacko <varghese@atemon.com>

#### Install

    pip install Flipkart-AffiliatesAPI


#### Usage

    from atemon.flipkart import FlipkartApi

    flipkart_api = API(
        fk_affiliate_id=<Your Affiliate ID>,
        fk_affiliate_token=<Your Affiliate Token>,
    )

    products = {}

    for category_name in flipkart_api.get_category_names():
        product_list = []
        product_list.extend(flipkart_api.get_products_from_category(category_name))

        while flipkart_api.has_more_products():
            product_list.extend(flipkart_api.get_next_products())

        products.update({category_name: product_list})

### Example 1 - Get all products

    from atemon.flipkart import FlipkartApi

    flipkart_api = API(
        fk_affiliate_id=<Your Affiliate ID>,
        fk_affiliate_token=<Your Affiliate Token>,
    )
    products = {}
    categoty_name_list = flipkart_api.get_category_names()

    for category_name in categoty_name_list:

        product_list = []

        p = flipkart_api.get_products_from_category(category_name)
        product_list.extend(p)

        while flipkart_api.has_more_products():
            p_next = flipkart_api.get_next_products()
            product_list.extend(p_next)

        products.update({category_name: product_list})



### Example 2 - Get Delta

    from atemon.flipkart import FlipkartApi

    flipkart_api = API(
        fk_affiliate_id=<Your Affiliate ID>,
        fk_affiliate_token=<Your Affiliate Token>,
    )
    products = {}
    categoty_name_list = flipkart_api.get_category_names()

    for category_name in categoty_name_list:

        product_list = []

        p = flipkart_api.get_products_from_category(category_name, list_type='delta')
        product_list.extend(p)

        while flipkart_api.has_more_products():
            p_next = flipkart_api.get_next_products()  # Flipkart will take care of the delta if 'delta' is passed in get_products_from_category
            product_list.extend(p_next)

        products.update({category_name: product_list})



#### Example 2 - Get Top

    from atemon.flipkart import FlipkartApi

    flipkart_api = API(
        fk_affiliate_id=<Your Affiliate ID>,
        fk_affiliate_token=<Your Affiliate Token>,
    )
    products = {}
    categoty_name_list = flipkart_api.get_category_names()

    for category_name in categoty_name_list:

        product_list = []

        p = flipkart_api.get_products_from_category(category_name, list_type='top')
        product_list.extend(p)

        while flipkart_api.has_more_products():
            p_next = flipkart_api.get_next_products()  # Flipkart will take care of the top if 'top' is passed in get_products_from_category
            product_list.extend(p_next)

        products.update({category_name: product_list})

#### Example 4- Get items in stock or get all items.

By default, the package gets only items instocks. The patameter 'in_stock' for get_products_from_category should be set to false to get all products.

    from atemon.flipkart import FlipkartApi

    flipkart_api = API(
        fk_affiliate_id=<Your Affiliate ID>,
        fk_affiliate_token=<Your Affiliate Token>,
    )
    products = {}
    categoty_name_list = flipkart_api.get_category_names()

    for category_name in categoty_name_list:

        product_list = []

        p = flipkart_api.get_products_from_category(category_name, list_type='top', in_stock=False)
        product_list.extend(p)

        while flipkart_api.has_more_products():
            p_next = flipkart_api.get_next_products()  # Flipkart will take care of the top if 'top' is passed in get_products_from_category
            product_list.extend(p_next)

        products.update({category_name: product_list})


### API Classes

#### FlipkartApi
This class forms the core for connecting to flipkart affiliates API.

    from atemon.flipkart import FlipkartApi

    flipkart_api = FlipkartApi(
    	fk_affiliate_id=<Your Affiliate ID>,
        fk_affiliate_token=<Your Affiliate Token>,
        in_stock=[True],
        list_type=['get']
    )

<ul>
    <li>fk_affiliate_id - YourAffiliate ID.</li>
    <li>fk_affiliate_token - Your Affiliate Token.</li>
    <li>in_stock  - True/False
    	<ul>
    		<li>True - Show only prodcts in stock.</li>
    		<li>False - Show prodcts in stock and not in stock.</li>
   	</ul>
    </li>
    <li>list_type - Type of products listed.
        <ul>
    		<li>get -  Get all products.</li>
    		<li>delta - Get delta.</li>
    		<li>top - Get top products.</li>
   	</ul>
    </li>
</ul>

#### Methods
<ul>
<li><b>flipkart_api.load_products_category_list()</b> - Load list of categories from Flipkart.</li>
<li><b>flipkart_api.load_products_dict()</b> - Load list of products from Flipkart and returns the response from flipkart as a dictionary.</li>
<li><b>flipkart_api.load_products_dict()</b> - Load list of products from Flipkart and returns the response from flipkart as a dictionaey.</li>
<li><b>flipkart_api.has_more_products()</b> - Returns if there are more products. It relies purely on 'nextUrl' returned by Flipkart. In some cases, fetchicing 'nextUrl' may return no results</li>
<li><b>flipkart_api.get_product_list_dict()</b> - Returns products as a list of dict.</li>
<li><b>flipkart_api.get_product_next_url()</b> - Returns next url to load products.</li>
<li><b>flipkart_api.get_products_category_dict()</b> - Returns list of categories(dict).</li>
<li><b>flipkart_api.get_category_names()</b> - Returns category names as a list.</li>
<li><b>flipkart_api.get_category_url(category_name=<Category Name>)</b> - Returns url to load products from given category.</li>
<li><b>flipkart_api.get_products_from_category(category_name=<Category Name>, list_type=['get'|'delta'|'top'], in_stock=[True|False])()</b> - Load first set of products for given category as Product object.</li>
<li><b>flipkart_api.get_next_products()</b> - Returns next page of products list.</li>
</ul>

#### Product
	from atemon.flipkart import Product

	data =   {
	    "productShippingInfoV1": {
	      "sellerName": "Suresh Kumar Singh",
	      "sellerAverageRating": 4.0,
	      "estimatedDeliveryTime": "",
	      "shippingCharges": {
		"currency": "INR",
		"amount": 0.0
	      },
	      "sellerNoOfRatings": 3524,
	      "sellerNoOfReviews": 206
	    },
	    "productBaseInfoV1": {
	      "productDescription": "",
	      "title": "HP 18-1310in All-in-One (AMD Zacate APU/ 2GB/ 500GB/ Win8)(Black, 379 mm x 476 mm, 6 kg, 46.99 Inch Screen)",
	      "flipkartSellingPrice": {
		"currency": "INR",
		"amount": 33400.0
	      },
	      "flipkartSpecialPrice": {
		"currency": "INR",
		"amount": 33400.0
	      },
	      "productFamily": [
		"AIODX286TJZAVUZ2"
	      ],
	      "offers": [
		"Get Rs2500 MMT Hotel Gift Card & Flight Offer",
		"No Cost EMI on Bajaj Finserv with cart value > Rs. 4499",
		"Extra 10% off* with HDFC Bank Credit Cards",
		"Get 30% Cashback* on Payments via PhonePe"
	      ],
	      "productUrl": "http://dl.flipkart.com/dl/hp-18-1310in-all-in-one-amd-zacate-apu-2gb-500gb-win8/p/itmdx288zhxpb8ge?pid=AIODX286TJZAVUZ2&affid=joel0250g",
	      "discountPercentage": 9.0,
	      "productBrand": "HP",
	      "inStock": false,
	      "attributes": {
		"color": "",
		"sizeUnit": "",
		"storage": "",
		"displaySize": "",
		"size": ""
	      },
	      "maximumRetailPrice": {
		"currency": "INR",
		"amount": 33400.0
	      },
	      "categoryPath": "Computers>Desktop PCs>All In One PCs",
	      "imageUrls": {
		"unknown": "http://img.fkcdn.com/image/allinone-desktop/u/z/2/hp-18-1310in-original-imadx2gjphmcpzgp.jpeg",
		"400x400": "http://img.fkcdn.com/image/allinone-desktop/u/z/2/hp-18-1310in-400x400-imadx2gjphmcpzgp.jpeg",
		"800x800": "http://img.fkcdn.com/image/allinone-desktop/u/z/2/hp-18-1310in-800x800-imadx2gjphmcpzgp.jpeg",
		"200x200": "http://img.fkcdn.com/image/allinone-desktop/u/z/2/hp-18-1310in-200x200-imadx2gjphmcpzgp.jpeg"
	      },
	      "codAvailable": true,
	      "productId": "AIODX286TJZAVUZ2"
	    },
	    "categorySpecificInfoV1": {
	      "specificationList": [
		{
		  "values": [
		    {
		      "value": [
		        "Keyboard, Mouse, Power Chord, User Manual, All In One Computer"
		      ],
		      "key": "In The Box"
		    }
		  ],
		  "key": "Sales Package"
		},
		{
		  "values": [
		    {
		      "value": [
		        "18-1310in"
		      ],
		      "key": "Model Name"
		    },
		    {
		      "value": [
		        "18"
		      ],
		      "key": "Series"
		    },
		    {
		      "value": [
		        "E9T76AA"
		      ],
		      "key": "Part Number"
		    },
		    {
		      "value": [
		        "Black"
		      ],
		      "key": "Colour"
		    },
		    {
		      "value": [
		        "HP"
		      ],
		      "key": "Brand"
		    }
		  ],
		  "key": "General"
		},
	      ],
	      "keySpecs": [
		"Windows 8",
		"AMD APU Quad Core A4",
		"HDD Capacity 500 GB",
		"RAM 2 GB DDR3",
		"46.99 cm Display"
	      ],
	      "lifeStyleInfo": {
		"idealFor": null,
		"neck": null,
		"sleeve": null
	      },
	      "detailedSpecs": [
		"Windows 8",
		"AMD APU Quad Core A4",
		"HDD Capacity 500 GB",
		"RAM 2 GB DDR3",
		"46.99 cm Display"
	      ],
	      "booksInfo": {
		"publisher": null,
		"language": null,
		"year": 0,
		"binding": null,
		"authors": [],
		"pages": null
	      }
	    }
	  }
	 p = Product(data)
## Contributors.

You are requested to report bugs and/or contribute to the package. We will try our best to keep track of any pull requests or bug reports. A mail with package name in subject line, sent to ```varghese@atemon.com```, will get quicker attention :)
