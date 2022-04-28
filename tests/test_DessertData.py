from unittest import TestCase
from DessertData import DessertData


class TestDessertData(TestCase):

    def setUp(self) -> None:
        self._tot_rows = 10
        data = []
        for i in range(self._tot_rows):
            data.append([0, i])
        self.test_data = DessertData(self._tot_rows, 0.0, data)


class TestInit(TestDessertData):

    def test_num_rows(self):
        for num_rows in range(1, 20):
            self.assertEqual(len(DessertData(num_rows).data()), num_rows)

    def test_noise_level(self):
        self.fail()


class TestSplit(TestDessertData):

    def test_split_objects(self):
        train_obj, test_obj = self.test_data.split(0.5)
        self.assertIsInstance(train_obj, DessertData)
        self.assertIsInstance(test_obj, DessertData)

    def test_split_one(self):
        """
        Test that 100% returns all the data
        """
        self.assertEqual(self.test_data.split(1.0)[0].data(), self.test_data.data())

    def test_split_rand(self):
        """
        Test that the number of rows is correct.
        """
        for row_num in range(0, self._tot_rows):
            percentage = row_num/self._tot_rows
            temp = self.test_data.split(percentage)[0]
            actual_data = self.test_data.split(percentage)[0].data()

            self.assertEqual(len(actual_data), row_num)
