import pytest
from page_objects.constructor_page import ConstructorPage


@pytest.mark.usefixtures("init_driver")
class TestConstructorFunctionality:

    def test_constructor_navigation(self):
        page = ConstructorPage(self.driver)
        page.open()
        page.click_constructor()
        assert "https://stellarburgers.nomoreparties.site/" in self.driver.current_url

    def test_add_ingredient_to_order(self):
        page = ConstructorPage(self.driver)
        page.open()
        page.add_ingredient_to_order("Флюоресцентная булка R2-D3")
        assert page.get_ingredient_counter("Флюоресцентная булка R2-D3") == 1
