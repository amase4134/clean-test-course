import pytest
from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel


def make_order(quantities):
  order = MockSet()
  for quantity in quantities:
    order.add(MockModel(quantity=quantity))
  return order


@pytest.mark.parametrize(
  "quantities,distance,expected",
  [
    ([5, 5, 5], 6, 7.50),
    ([2, 2, 2], 4, 5),
    ([3, 1], 2, 3.50),
    ([5, 5, 5], 4, 5),
    ([10], 6, 5),
    ([], 10, 3.50),
  ],
  ids=[
    "lots_of_items_far_distance",
    "middle_items_mid_distance",
    "few_items_short_distance",
    "lots_of_items_short_distance",
    "exactly_ten_items_far_distance",
    "empty_order_default_fee",
  ],
)
def test_delivery_cost(quantities, distance, expected):
  order = make_order(quantities)
  cost = Delivery.calculate(order, distance)
  assert cost == expected
