import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(10, 15, 20, 25, 30)

    def test_init(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 15)
        self.assertEqual(self.r1.x, 20)
        self.assertEqual(self.r1.y, 25)
        self.assertEqual(self.r1.id, 30)

    def test_area(self):
        self.assertEqual(self.r1.area(), 150)

    def test_str(self):
        self.assertEqual(str(self.r1), "[Rectangle] (30) 20/25 - 10/15")

    def test_update(self):
        self.r1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)

    def test_to_dictionary(self):
        self.assertEqual(self.r1.to_dictionary(),
                        {'id': 30, 'width': 10, 'height': 15, 'x': 20, 'y': 25})


class TestBase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base(1)

    def test_init(self):
        self.assertEqual(self.b1.id, 1)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{'id': 12}])

    def test_create(self):
        r1 = Rectangle(3, 5, 1, id=89)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, id=70)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_input), str(list_rectangles_output))


if __name__ == '__main__':
    unittest.main()
