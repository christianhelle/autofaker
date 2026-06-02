import unittest

from autofaker.attributes import Attributes


class _Sample:
    integer = 1
    text = "hi"

    def method(self):
        return "method"


class AttributesTestCase(unittest.TestCase):
    def test_get_members_excludes_dunders_and_callables(self):
        attrs = Attributes(_Sample())
        members = attrs.get_members()
        self.assertIn("integer", members)
        self.assertIn("text", members)
        self.assertNotIn("method", members)
        for m in members:
            self.assertFalse(m.startswith("__"))

    def test_get_attribute_returns_value(self):
        attrs = Attributes(_Sample())
        self.assertEqual(attrs.get_attribute("text"), "hi")

    def test_get_typename_returns_type_name(self):
        attrs = Attributes(_Sample())
        self.assertEqual(attrs.get_typename("text"), "str")
        self.assertEqual(attrs.get_typename("integer"), "int")

    def test_set_value_updates_attribute(self):
        instance = _Sample()
        attrs = Attributes(instance)
        attrs.set_value("text", "bye")
        self.assertEqual(instance.text, "bye")


if __name__ == "__main__":
    unittest.main()
