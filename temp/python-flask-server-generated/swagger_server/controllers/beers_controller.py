import connexion
import six

from swagger_server.models.beer import Beer  # noqa: E501
from swagger_server.models.beer_paged_list import BeerPagedList  # noqa: E501
from swagger_server import util


def delete_beer_v1(beer_id):  # noqa: E501
    """Delete Beer by Id

    Delete a beer resource by its ID value. # noqa: E501

    :param beer_id: Beer Id
    :type beer_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_beer_by_id_v1(beer_id):  # noqa: E501
    """Get Beer by ID

    Get a single beer by its ID value. # noqa: E501

    :param beer_id: Beer Id
    :type beer_id: 

    :rtype: Beer
    """
    return 'do some magic!'


def list_beers_v1(page_number=None, page_size=None):  # noqa: E501
    """List Beers

    List all beers in system. # noqa: E501

    :param page_number: Page Number
    :type page_number: int
    :param page_size: Page Size
    :type page_size: int

    :rtype: BeerPagedList
    """
    return 'do some magic!'


def update_beer_by_id_v1(body, beer_id):  # noqa: E501
    """Update Beer by ID

    Update a beer by its ID value. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param beer_id: Beer Id
    :type beer_id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = Beer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v1_beers_post(body):  # noqa: E501
    """New Beer

    Create a new Beer Object # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Beer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
