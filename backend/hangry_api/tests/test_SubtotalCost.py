from api.controllers import Subtotal
from django_mock_queries.query import MockSet, MockModel

def test_SimpleCost():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 15


def test_ComplexCost():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2, item=MockModel(price=3.5)))
  order.add(MockModel(quantity=1, item=MockModel(price=4.5)))
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 11.5

def test_EmptyOrder():
  #Arrange
  order = MockSet()
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 0

def test_SingleItem():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=3, item=MockModel(price=4.25)))
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 12.75
