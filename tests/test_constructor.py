import pytest
from page_objects.constructor_page import ConstructorPage


@pytest.mark.usefixtures("init_driver")
class TestConstructorFunctionality:

    def test_constructor_navigation(self, browser):
        page = ConstructorPage(browser)
        page.open(self)

    def test_add_ingredient_to_order(self, browser):
        page = ConstructorPage(browser)
        page.open(self)
        page.add_ingredient_to_order("Флюоресцентная булка R2-D3")
        assert page.get_ingredient_counter("Флюоресцентная булка R2-D3") == 1

    def test_place_order(self):
        page = ConstructorPage(self, browser)
        page.open(self)
        page.add_ingredient_to_order("Флюоресцентная булка R2-D3")
        confirmation_message = page.place_order()
        assert "Ваш заказ начали готовить" in confirmation_message