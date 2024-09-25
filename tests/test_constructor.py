import allure
import pytest
from page_objects.constructor_page import ConstructorPage
from locators.locators import *
from locators.variables import *


@pytest.mark.usefixtures("init_driver")
class TestConstructorFunctionality:

    @allure.title("Navigate to constructor page")
    def test_constructor_navigation(self, init_driver):
        page = ConstructorPage(init_driver)
        page.open(BASE_URL)
        assert page.is_on_constructor_page()

    @allure.title("Add ingredient to order")
    def test_add_ingredient_to_order(self, init_driver):
        page = ConstructorPage(init_driver)
        page.open(BASE_URL)
        page.add_ingredient_to_order("Флюоресцентная булка R2-D3")
        assert page.get_ingredient_counter("Флюоресцентная булка R2-D3") == 1

    @allure.title("Place order")
    def test_place_order(self, init_driver):
        page = ConstructorPage(init_driver)
        page.open(BASE_URL)
        page.add_ingredient_to_order("Флюоресцентная булка R2-D3")
        confirmation_message = page.place_order()
        assert "Ваш заказ начали готовить" in confirmation_message
