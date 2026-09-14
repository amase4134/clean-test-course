from api.controllers import Tax

def test_SimpleTax():
  #Arrange
  subtotal = 15
  deliveryFee = 3.50
  #Act
  tax = Tax.calculate(subtotal, deliveryFee)
  #Assert
  assert tax == 1.53

def test_ComplexTax():
  #Arrange
  subtotal = 11.5
  deliveryFee = 5
  #Act
  tax = Tax.calculate(subtotal, deliveryFee)
  #Assert
  assert tax == 1.36

def test_ZeroTax():
  #Arrange
  subtotal = 0
  deliveryFee = 0
  #Act
  tax = Tax.calculate(subtotal, deliveryFee)
  #Assert
  assert tax == 0
