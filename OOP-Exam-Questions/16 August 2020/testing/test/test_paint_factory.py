from project.factory.paint_factory import PaintFactory
from project.factory.factory import Factory
from unittest import TestCase, main


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.paint_factory1 = PaintFactory("paintjoy", 10)

    def test_correct_initialisation(self):
        self.assertEqual("paintjoy", self.paint_factory1.name)
        self.assertEqual(10, self.paint_factory1.capacity)
        self.assertEqual({}, self.paint_factory1.ingredients)
        self.assertEqual({}, self.paint_factory1.products)
        self.assertEqual(["white", "yellow", "blue", "green", "red"],
                         self.paint_factory1.valid_ingredients)

    # getattr gets the value of the "products" attribute of the class (type(...))
    # isinstance then checks it the attr is defined as property
    def test_if_products_property_defined(self):
        self.assertEqual(True,
                         isinstance(getattr(type(self.paint_factory1),
                                            "products"), property))

    def test_if_products_property_sets_correctly(self):
        # no ingredients
        self.paint_factory1.ingredients = {}
        self.assertEqual({}, self.paint_factory1.products)

        #after ingredients are set
        self.paint_factory1.ingredients = {"green": 3, "blue": 7}
        self.assertEqual({"green": 3, "blue": 7}, self.paint_factory1.products)

    def test_if_paint_factory_inherits_from_factory(self):
        self.assertTrue(issubclass(PaintFactory, Factory))

    def test_if_all_parent_attributes_are_inherited(self):
        self.assertTrue(hasattr(self.paint_factory1, "name"))
        self.assertTrue(hasattr(self.paint_factory1, "capacity"))
        self.assertTrue(hasattr(self.paint_factory1, "ingredients"))
        self.assertTrue(hasattr(self.paint_factory1, "products"))
        self.assertTrue(hasattr(self.paint_factory1, "add_ingredient"))
        self.assertTrue(hasattr(self.paint_factory1, "remove_ingredient"))

    def test_remove_ingredient_method_doc_string_overridden(self):
        doc_str_remove = self.paint_factory1.remove_ingredient.__doc__
        self.assertEqual(None, doc_str_remove)

    def test_add_ingredient_method_doc_string_overridden(self):
        doc_str_remove = self.paint_factory1.add_ingredient.__doc__
        self.assertEqual(None, doc_str_remove)

    def test_if_abstract_attributes_are_overridden(self):
        paintclass = PaintFactory.__dict__["add_ingredient"]
        self.assertFalse(paintclass is Factory.add_ingredient)
        paintclass = PaintFactory.__dict__["remove_ingredient"]
        self.assertFalse(paintclass is Factory.remove_ingredient)

    def test_if_non_abstract_attributes_are_directly_inherited(self):
        paintclass = Factory.__dict__["can_add"]
        self.assertTrue(paintclass is PaintFactory.can_add)
        paintclass = Factory.__dict__["__repr__"]
        self.assertTrue(paintclass is PaintFactory.__repr__)

    def test_add_ingredient_non_valid_product_type_raises_type_error(self):
        with self.assertRaises(TypeError) as te:
            self.paint_factory1.add_ingredient("magenta", 2)
        self.assertEqual("Ingredient of type magenta not allowed"
                         " in PaintFactory", str(te.exception))

    def test_can_add_returns_correct_value(self):
        # no capacity left
        self.paint_factory1.ingredients = {"green": 3, "blue": 7}
        self.assertEqual(False, self.paint_factory1.can_add(1))

        # capacity left
        self.paint_factory1.ingredients = {"green": 3, "blue": 6}
        self.assertEqual(True, self.paint_factory1.can_add(1))

    def test_add_ingredient_when_capacity_and_product_not_in_ingredients(self):
        # no ingredients
        self.paint_factory1.ingredients = {}
        self.paint_factory1.add_ingredient("yellow", 1)
        self.assertEqual({"yellow": 1},
                         self.paint_factory1.ingredients)
        self.assertEqual({"yellow": 1},
                         self.paint_factory1.products)

        # add when ingredients
        self.paint_factory1.ingredients = {"green": 3, "blue": 5}
        self.paint_factory1.add_ingredient("yellow", 1)
        self.assertEqual({"green": 3, "blue": 5, "yellow": 1},
                         self.paint_factory1.ingredients)
        self.assertEqual({"green": 3, "blue": 5, "yellow": 1},
                         self.paint_factory1.products)

        # add one more
        self.paint_factory1.add_ingredient("red", 1)
        self.assertEqual({"green": 3, "blue": 5, "yellow": 1, "red": 1},
                         self.paint_factory1.ingredients)
        self.assertEqual({"green": 3, "blue": 5, "yellow": 1, "red": 1},
                         self.paint_factory1.products)

    def test_add_ingredient_when_enough_capacity_and_product_in_ingredients(self):
        self.paint_factory1.ingredients = {"green": 3, "blue": 5}
        self.paint_factory1.add_ingredient("green", 2)
        self.assertEqual({"green": 5, "blue": 5},
                         self.paint_factory1.ingredients)
        self.assertEqual({"green": 5, "blue": 5},
                         self.paint_factory1.products)

    def test_add_ingredient_when_no_capacity_and_product_in_ingredients(self):
        self.paint_factory1.capacity = 3
        self.paint_factory1.ingredients = {"green": 2, "blue": 1}
        with self.assertRaises(ValueError) as ve:
            self.paint_factory1.add_ingredient("green", 1)
        self.assertEqual("Not enough space in factory", str(ve.exception))
        self.assertEqual({"green": 2, "blue": 1},
                         self.paint_factory1.ingredients)
        self.assertEqual({"green": 2, "blue": 1},
                         self.paint_factory1.products)

    def test_add_ingredient_when_no_capacity_and_product_not_in_ingredients(self):
        self.paint_factory1.capacity = 3
        self.paint_factory1.ingredients = {"green": 2, "blue": 1}
        with self.assertRaises(ValueError) as ve:
            self.paint_factory1.add_ingredient("red", 1)
        self.assertEqual("Not enough space in factory", str(ve.exception))
        self.assertEqual({"green": 2, "blue": 1},
                         self.paint_factory1.ingredients)
        self.assertEqual({"green": 2, "blue": 1},
                         self.paint_factory1.products)

    def test_remove_ingredient_raises_key_error_for_non_valid_ingredient(self):
        with self.assertRaises(KeyError) as ke:
            self.paint_factory1.remove_ingredient("magenta", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))
        self.assertEqual({}, self.paint_factory1.ingredients)

    def test_remove_ingredient_raises_value_error_for_ingredient_quantity_below_zero(self):
        self.paint_factory1.ingredients = {"green": 2, "blue": 1}
        with self.assertRaises(ValueError) as ve:
            self.paint_factory1.remove_ingredient("green", 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))
        self.assertEqual({"green": 2, "blue": 1}, self.paint_factory1.ingredients)
        self.assertEqual({"green": 2, "blue": 1}, self.paint_factory1.products)

    def test_remove_ingredient_correctly_removes_ingredient(self):
        self.paint_factory1.ingredients = {"green": 2, "blue": 1}
        result1 = self.paint_factory1.remove_ingredient("green", 2)
        self.assertEqual(None, result1)
        self.assertEqual({"green": 0, "blue": 1}, self.paint_factory1.ingredients)
        self.assertEqual({"green": 0, "blue": 1}, self.paint_factory1.products)

        # remove one more
        result2 = self.paint_factory1.remove_ingredient("blue", 1)
        self.assertEqual(None, result2)
        self.assertEqual({"green": 0, "blue": 0}, self.paint_factory1.ingredients)
        self.assertEqual({"green": 0, "blue": 0}, self.paint_factory1.products)

    def test_repr_returns_correct_info(self):
        # no ingredients
        expected1 = "Factory name: paintjoy with capacity 10.\n"
        self.assertEqual(expected1, repr(self.paint_factory1))

        # with ingredients
        self.paint_factory1.ingredients = {"green": 3, "blue": 5, "red": 2}
        expected2 = "Factory name: paintjoy with capacity 10.\n" \
                    "green: 3\nblue: 5\nred: 2\n"
        self.assertEqual(expected2, repr(self.paint_factory1))


if __name__ == "__main__":
    main()
