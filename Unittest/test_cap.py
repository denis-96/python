import unittest
import cap


class TestCap(unittest.TestCase):

    def test1(self):
        self.assertEqual(cap.cap_text('python'), 'Python')
        self.assertEqual(cap.cap_text('denis'), 'Denis')
        self.assertEqual(cap.cap_text('mother'), 'Mother')
        self.assertEqual(cap.cap_text('cat'), 'Cat')

    def test2(self):
        self.assertEqual(cap.cap_text('i am working'), 'I Am Working')
        self.assertEqual(cap.cap_text('i am a computer programmer'), 'I Am A Computer Programmer')
        self.assertEqual(cap.cap_text('у меня есть кошка'), 'У Меня Есть Кошка')

    def test3(self):
        self.assertEqual(cap.cap_text("i'm a programmer"), "I'm A Programmer")
        self.assertEqual(cap.cap_text("i've a cat"), "I've A Cat")


if __name__ == '__main__':
    unittest.main()