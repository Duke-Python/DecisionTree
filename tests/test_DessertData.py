import random
import unittest
from DessertData import DessertData


class TestDessertData(unittest.TestCase):

    def setUp(self) -> None:
        self._tot_rows = 10
        data = []
        for i in range(self._tot_rows):
            data.append([0, i])
        self.test_data = DessertData(self._tot_rows, 0.0, data)


class TestInit(TestDessertData):

    def test_neg_rows(self):
        self.assertRaises(ValueError, DessertData, -1)

    def test_num_rows(self):
        for num_rows in range(0, 20):
            with self.subTest(i=num_rows):
                self.assertEqual(len(DessertData(num_rows).data), num_rows)

    @unittest.skip("Noise level not implemented")
    def test_noise_level(self):
        self.fail()


class TestSplit(TestDessertData):

    def test_split_objects(self):
        """
        Test that split returns DessertData objects
        """
        train_obj, test_obj = self.test_data.split(random.random())
        self.assertIsInstance(train_obj, DessertData)
        self.assertIsInstance(test_obj, DessertData)

    def test_split_one(self):
        """
        Test that splitting 100% returns all data in training and empty in test
        """
        train_set, test_set = self.test_data.split(1.0)
        self.assertEqual(train_set.data, self.test_data.data)
        self.assertFalse(test_set.data)

    def test_split_rand(self):
        """
        Test that the number of rows is correct. Cannot test actual data since it's shuffled
        before splitting.
        """
        for row_num in range(0, self._tot_rows):
            with self.subTest(i=row_num):
                percentage = row_num/self._tot_rows
                train_set, test_set = self.test_data.split(percentage)

                self.assertEqual(len(train_set.data), row_num, "Train set wrong size")
                self.assertEqual(len(test_set.data), self._tot_rows-row_num, "Test set wrong size")
