from unittest import TestCase

from data.Feature import Feature


class TestFeature(TestCase):
    """
    Define test data
    """
    def setUp(self) -> None:
        self.feature1 = Feature("first", {1: 1})
        self.feature2 = Feature("second", {2: 2})
        self.featureOne = Feature("First", {1: 0})


class TestHashFeature(TestFeature):
    """
    Test that Feature can be used as a key
    """
    def test_hash(self):
        test_dict = {self.feature1: 0}
        self.assertEqual(test_dict[self.feature1], 0)
        test_dict[self.feature2] = 1
        self.assertEqual(test_dict[self.feature2], 1)
        test_dict[self.featureOne] = 1
        self.assertEqual(test_dict[self.feature1], 1)


class TestEqFeature(TestFeature):
    """
    Test the equality of Features
    """
    def test_equality(self):
        self.assertEqual(self.feature1, self.featureOne)
        self.assertNotEqual(self.feature1, self.feature2)
        self.assertNotEqual(self.feature1, 1)
