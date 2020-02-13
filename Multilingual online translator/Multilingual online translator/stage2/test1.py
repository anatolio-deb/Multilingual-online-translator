from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if '200 OK' in reply:
            return CheckResult.true()
        return CheckResult.false("Test failed. There isn't internet connection identificator.")

TranslatorTest('translator.translator').run_tests()