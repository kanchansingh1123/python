import connexion
import six

from swagger_server.models.beer_order import BeerOrder  # noqa: E501
from swagger_server import util


def v1_customers_customer_id_orders_post(customer_id, body=None):  # noqa: E501
    """v1_customers_customer_id_orders_post

    Place Order # noqa: E501

    :param customer_id: Customer Id
    :type customer_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BeerOrder.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
