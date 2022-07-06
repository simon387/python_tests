from amazon.paapi import AmazonAPI

from amazonCred import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG

amazon = AmazonAPI(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG, 'US')

product = amazon.get_product('B07RH665FZ')
print(product.title)

# manca collegamento associate
# https://blog.ajbothe.com/querying-the-amazon-product-data-api-using-python
