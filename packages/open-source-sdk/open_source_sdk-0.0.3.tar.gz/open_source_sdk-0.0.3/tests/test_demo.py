import unittest


class DemoTest(unittest.TestCase):
    show = True

    def test_example_1(self) -> None:
        """Test example"""
        print("Test")

        print("Test again")


if __name__ == "__main__":
    unittest.main()
