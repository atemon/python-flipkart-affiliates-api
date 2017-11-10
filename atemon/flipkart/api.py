"""Flipkart affiliate API."""
import requests
import json

from.exceptions import ProductNotLoadedException
# import pdb


class FlipkartApi(object):
    """API."""

    def __init__(self, fk_affiliate_id, fk_affiliate_token, in_stock=True, list_type='get', **kwargs):
        """Init method."""
        self.Fk_Affiliate_Token = fk_affiliate_token
        self.Fk_Affiliate_Id = fk_affiliate_id
        self.profile_url = 'https://affiliate-api.flipkart.net/affiliate/api/%s.json' % (fk_affiliate_id)
        self.header = {
            'Fk-Affiliate-Token': self.Fk_Affiliate_Token,
            'Fk-Affiliate-Id': self.Fk_Affiliate_Id,
        }
        self.category_content = None
        self.category_dict = []
        self.category_names = []
        self.products_dict = None
        self.products_list = None
        self.next_url = None
        self.in_stock = in_stock
        self.list_type = list_type

    def _call_api(self, url):
        """Load data from API."""
        r = requests.get(url, params={}, headers=self.header)
        return r.json()

    def load_products_category_list(self):
        """Get products category list."""
        self.category_content = self._call_api(self.profile_url)
        return self.category_content

    def load_products_dict(self, url):
        """Load list of products using URL."""
        if url:
            self.products_dict = self._call_api(url)
        else:
            self.products_dict = {}
        self.current_product_url = url

        return self.products_dict

    def has_more_products(self):
        """Check for more products."""
        if self.products_dict.get('nextUrl'):
            return True
        else:
            return False

    def get_product_list_dict(self, url):
        """Get list of products from Flipkart."""
        self.load_products_dict(url)
        return self.products_dict.get('productInfoList', {})

    def get_product_next_url(self, in_stock=True):
        """Get list of products from Flipkart."""
        try:
            next_url = self.products_dict.get('nextUrl')
            if self.in_stock:
                next_url += "&inStock=true"
            if next_url != self.current_product_url and str(next_url).lower != 'null':
                return next_url
            else:
                None
        except AttributeError:
            raise ProductNotLoadedException(message="Products are not loaded yet. Please load the first list of products to get next url.")

    def get_products_category_dict(self):
        """Return category list as python dict."""
        if self.category_content is None:
            self.load_products_category_list()
        self.category_dict = self.category_content.get('apiGroups').get('affiliate').get('apiListings')
        return self.category_dict

    def get_category_names(self):
        """Get all category names."""
        if self.category_dict is None:
            self.get_products_category_dict()
        if type(self.category_dict) is dict:
            self.category_names = self.category_dict.keys()
            return self.category_names
        else:
            return []

    def get_category_url(self, category_name, list_type="get", in_stock=True):
        """
        Get category list.

        url_type : get   - Get all products
                   delta - Get delta
                   top   - Get top products
        """
        if self.list_type == 'delta':
            list_type = "deltaGet"
        else:
            list_type = self.list_type

        url = self.category_dict.get(category_name).get("availableVariants").get("v1.1.0").get(list_type)

        if self.in_stock:
            url += "&inStock=true"
        return url

    def _get_products(self):
        """Get products as a list or Product objects."""
        products_list = []
        for product in self.get_product_list_dict(self.new_url):
            products_list.append(Product(product))
        return products_list

    def get_products_from_category(self, category_name, list_type='get', in_stock=True):
        """Get list of products for given category."""
        self.in_stock = in_stock
        self.list_type = list_type
        self.new_url = self.get_category_url(category_name)
        return self._get_products()

    def get_next_products(self):
        """Get next set of products."""
        self.new_url = self.get_product_next_url()
        return self._get_products()



class Product(object):
    """Products."""

    def __init__(self, data):
        """Initialize."""
        self.data = data

    @property
    def title(self):
        """Product Title."""
        return self.data.get('productBaseInfoV1', {}).get('title', None)

    @property
    def selling_price(self):
        """Product selling price."""
        return Amount(self.data.get('productBaseInfoV1', {}).get('flipkartSellingPrice', None))

    @property
    def special_price(self):
        """Product special price."""
        return Amount(self.data.get('productBaseInfoV1', {}).get('flipkartSpecialPrice', None))

    @property
    def url(self):
        """Product URL."""
        return self.data.get('productBaseInfoV1', {}).get('productUrl', None)

    @property
    def product_family(self):
        """Product Family."""
        return self.data.get('productBaseInfoV1', {}).get('productFamily', None)

    @property
    def mrp(self):
        """Get MRP."""
        return Amount(self.data.get('productBaseInfoV1', {}).get('maximumRetailPrice', None))

    @property
    def description(self):
        """Product description."""
        return self.data.get('productBaseInfoV1', {}).get('productDescription', None)

    @property
    def cod(self):
        """Cod available."""
        return boolean(self.data.get('productBaseInfoV1', {}).get('codAvailable'))

    @property
    def emi(self):
        """EMI available."""
        return boolean(self.data.get('productBaseInfoV1', {}).get('emiAvailable', None))

    @property
    def offers(self):
        """Available offers."""
        return self.data.get('productBaseInfoV1', {}).get('offers', None)

    @property
    def discount_percentage(self):
        """Discount percentge."""
        return self.data.get('productBaseInfoV1', {}).get('discountPercentage', None)

    @property
    def brand(self):
        """Product brand."""
        return self.data.get('productBaseInfoV1', {}).get('productBrand', None)

    @property
    def instock(self):
        """Available instock."""
        return boolean(self.data.get('productBaseInfoV1', {}).get('inStock', None))

    @property
    def images(self):
        """Images."""
        return self.data.get('productBaseInfoV1', {}).get('imageUrls', None)

    @property
    def color(self):
        """Color."""
        return self.data.get('productBaseInfoV1', {}).get('attributes', {}).get('color', None)

    @property
    def size_unit(self):
        """Size Unit."""
        return self.data.get('productBaseInfoV1', {}).get('attributes', {}).get('sizeUnit', None)

    @property
    def storage(self):
        """storage."""
        return self.data.get('productBaseInfoV1', {}).get('storage', {}).get('storage', None)

    @property
    def display_size(self):
        """Display size."""
        return self.data.get('productBaseInfoV1', {}).get('storage', {}).get('displaySize', None)

    @property
    def size(self):
        """Size."""
        return self.data.get('productBaseInfoV1', {}).get('storage', {}).get('size', None)

    @property
    def id(self):
        """Product id."""
        return self.data.get('productBaseInfoV1', {}).get('productId', None)

    @property
    def category_path(self):
        """Category Path."""
        return self.data.get('productBaseInfoV1', {}).get('categoryPath', None)

    @property
    def image_urls(self):
        """Image URLs."""
        return self.data.get('productBaseInfoV1', {}).get('imageUrls', None)

    @property
    def seller_name(self):
        """Seller name."""
        return self.data.get('productShippingInfoV1', {}).get('sellerName', None)

    @property
    def seller_average_rating(self):
        """Seller Average Rating."""
        return self.data.get('productShippingInfoV1', {}).get('sellerAverageRating', None)

    @property
    def estimated_delivery_time(self):
        """Estimated Delivery Time."""
        return self.data.get('productShippingInfoV1', {}).get('estimatedDeliveryTime', None)

    @property
    def shipping_charges(self):
        """Shipping Charges."""
        return Amount(self.data.get('productShippingInfoV1', {}).get('shippingCharges', None))

    @property
    def seller_ratings_count(self):
        """Seller no of ratings."""
        return Amount(self.data.get('productShippingInfoV1', {}).get('sellerNoOfRatings', None))

    @property
    def seller_reviews_count(self):
        """Seller no of reviews."""
        return Amount(self.data.get('productShippingInfoV1', {}).get('sellerNoOfReviews', None))


class Amount(object):
    """Class to represent amount."""

    def __init__(self, data):
        """Initialize Amount."""
        self.currency = data.get("currency")
        self.amount = data.get("amount")


def boolean(truth):
    """Convert truth to boolean."""
    if str(truth).lower() in ['true', 'yes', '1', 'none']:
        return True
    else:
        return False
