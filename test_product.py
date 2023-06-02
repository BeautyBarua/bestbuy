from products import Product
import pytest


def test_create_product():
    product = Product("Test Product", price=10, quantity=5)
    assert product.name == "Test Product"
    assert product.price == 10
    assert product.quantity == 5
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    with pytest.raises(Exception):
        Product("", price=-10, quantity=5)


def test_product_reaches_zero_quantity():
    product = Product("Test Product", price=10, quantity=1)
    assert product.is_active() is True
    product.purchase(1)
    assert product.quantity == 0
    assert product.is_active() is True


def test_product_purchase():
    product = Product("Test Product", price=10, quantity=5)
    assert product.purchase(2) == 20
    assert product.quantity == 3


def test_product_purchase_exceeds_quantity():
    product = Product("Test Product", price=10, quantity=5)
    with pytest.raises(Exception):
        product.purchase(10)
