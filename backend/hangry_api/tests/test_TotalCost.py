from api.controllers import Total
from django_mock_queries.query import MockSet, MockModel

def test_SimpleTotal():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  deliveryFee = 3.50
  #Act
  total = Total.calculate(order, deliveryFee)
  #Assert
  assert total == 20.03

def test_ComplexTotal():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2, item=MockModel(price=3.5)))
  order.add(MockModel(quantity=1, item=MockModel(price=4.5)))
  deliveryFee = 5
  #Act
  total = Total.calculate(order, deliveryFee)
  #Assert
  assert total == 17.86

def test_TotalWithHighDelivery():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  deliveryFee = 7.50
  #Act
  total = Total.calculate(order, deliveryFee)
  #Assert
  assert total == 24.36

def test_ZeroTotal():
  #Arrange
  order = MockSet()
  deliveryFee = 0
  #Act
  total = Total.calculate(order, deliveryFee)
  #Assert
  assert total == 0
