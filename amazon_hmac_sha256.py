import hmac
import hashlib
import base64

AMAZON_SECRET = 1234567890
MESSAGE = 'GET webservices.amazon.com/onca/xmlAWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&ItemId=0679722769&Operation=ItemLookup&ResponseGroup=Images%2CItemAttributes%2COffers%2CReviews&Service=AWSECommerceService&Timestamp=2014-08-18T12%3A00%3A00Z&Version=2013-08-01'

dig = hmac.new(b'AMAZON_SECRET', msg=MESSAGE, digestmod=hashlib.sha256).hexdigestdigest()
base64.b64encode(dig).decode()  