import connexion
import six

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_paged_list import CustomerPagedList  # noqa: E501
from swagger_server import util


def delete_customer_v1(customer_id):  # noqa: E501
    """Delete Customer By ID

    Delete a customer by its Id value. # noqa: E501

    :param customer_id: Customer Id
    :type customer_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_customer_by_id_v1(customer_id):  # noqa: E501
    """Get Customer By ID

    Get a single **Customer** by its Id value. # noqa: E501

    :param customer_id: Customer Id
    :type customer_id: 

    :rtype: Customer
    """
    return 'do some magic!'


def list_customers_v1(page_number=None, page_size=None):  # noqa: E501
    """List Customers

    Get a list of customers in the system # noqa: E501

    :param page_number: Page Number
    :type page_number: int
    :param page_size: Page Size
    :type page_size: int

    :rtype: CustomerPagedList
    """
    return 'do some magic!'


def v1_customers_customer_id_put(body, customer_id):  # noqa: E501
    """Update Customer

    Update customer by id. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param customer_id: Customer Id
    :type customer_id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v1_customers_post(body):  # noqa: E501
    """New Customer

    Create a new customer # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
