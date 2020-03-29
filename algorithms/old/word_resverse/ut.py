import unittest
from res_words import words_reverse


class TestDemo(unittest.TestCase):

    def test_words(self):
        demo = words_reverse("This is a test")
        print demo
#         # result = unittest.TestResult()
        self.assertEqual(demo, "sihT si a tset")
        demo = words_reverse(",....")
        self.assertEqual(demo, ",....")

        demo = words_reverse("Test")
        self.assertEqual(demo, "tseT")

        demo = words_reverse("aaa fv ...fh,.,,")
        self.assertEqual(demo, "aaa vf ...hf,.,,")

#         # self.assertIsNone(result._stdout_buffer)
#         # self.assertIsNone(result._stderr_buffer)
#
# #
# # class TestDemo(unittest):
# #     def test_words(self):
# #
# #         print ""
#
#
if __name__ == '__main__':
    # demo = TestDemo
    # demo.test_words()
    unittest.main()
