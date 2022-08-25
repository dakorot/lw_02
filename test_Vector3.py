from unittest import TestCase
from Vector3 import Vector3


class TestVector3(TestCase):

    def test_equals(self):
        self.assertTrue(Vector3(0, 0, 0) == Vector3(0, 0, 0))

    def test_wrong_type(self):
        self.assertRaises(TypeError, lambda: Vector3(0, '0', 0))

    def test_get_coords_zero_vector(self):
        expected = (0, 0, 0)
        actual = Vector3(0, 0, 0).get_coords()
        self.assertEqual(actual, expected)

    def test_get_coords_different_coords(self):
        expected = (1, 2, 3)
        actual = Vector3(1, 2, 3).get_coords()
        self.assertEqual(actual, expected)

    def test_get_coords_negative_coord(self):
        expected = (-100, 0, 100)
        actual = Vector3(-100, 0, 100).get_coords()
        self.assertEqual(actual, expected)

    def test_to_str_zero_vector(self):
        expected = "(0, 0, 0)"
        actual = Vector3(0, 0, 0).__str__()
        self.assertEqual(actual, expected)

    def test_to_str_different_coords(self):
        expected = "(1, 2, 3)"
        actual = Vector3(1, 2, 3).__str__()
        self.assertEqual(actual, expected)

    def test_to_str_negative_coord(self):
        expected = "(-100, 0, 100)"
        actual = Vector3(-100, 0, 100).__str__()
        self.assertEqual(actual, expected)

    def test_addition_zero_vectors(self):
        expected = Vector3(0, 0, 0)
        actual = Vector3(0, 0, 0) + Vector3(0, 0, 0)
        self.assertEqual(actual, expected)

    def test_addition_negative_vectors(self):
        expected = Vector3(0, 0, 0)
        actual = Vector3(-1, 0, 1) + Vector3(1, 0, -1)
        self.assertEqual(actual, expected)

    def test_addition_different_vectors(self):
        expected = Vector3(-25, 38, 171)
        actual = Vector3(5, 10, 15) + Vector3(-30, 28, 156)
        self.assertEqual(actual, expected)

    def test_addition_vector_with_zero_vector(self):
        expected = Vector3(-30, 28, 156)
        actual = Vector3(-30, 28, 156) + Vector3(0, 0, 0)
        self.assertEqual(actual, expected)

    def test_subtraction_zero_vectors(self):
        expected = Vector3(0, 0, 0)
        actual = Vector3(0, 0, 0) - Vector3(0, 0, 0)
        self.assertEqual(actual, expected)

    def test_subtraction_equal_vectors(self):
        expected = Vector3(0, 0, 0)
        actual = Vector3(-23, 94, 45) - Vector3(-23, 94, 45)
        self.assertEqual(actual, expected)

    def test_subtraction_different_vectors(self):
        expected = Vector3(35, -18, -141)
        actual = Vector3(5, 10, 15) - Vector3(-30, 28, 156)
        self.assertEqual(actual, expected)

    def test_subtraction_vector_with_zero_vector(self):
        expected = Vector3(-30, 28, 156)
        actual = Vector3(-30, 28, 156) - Vector3(0, 0, 0)
        self.assertEqual(actual, expected)

    def test_dot_product_zero_vectors(self):
        expected = 0
        actual = Vector3(0, 0, 0) * Vector3(0, 0, 0)
        self.assertEqual(actual, expected)

    def test_dot_product_equal_vectors(self):
        expected = 11390
        actual = Vector3(-23, 94, 45) * Vector3(-23, 94, 45)
        self.assertEqual(actual, expected)

    def test_dot_product_different_vectors(self):
        expected = 2470
        actual = Vector3(5, 10, 15) * Vector3(-30, 28, 156)
        self.assertEqual(actual, expected)

    def test_dot_product_vector_with_zero_vector(self):
        expected = 0
        actual = Vector3(-30, 28, 156) * Vector3(0, 0, 0)
        self.assertEqual(actual, expected)

    def test_dot_product_perpendicular_vectors(self):
        expected = 0
        actual = Vector3(5, 0, 0) * Vector3(0, 5, 0)
        self.assertEqual(actual, expected)
