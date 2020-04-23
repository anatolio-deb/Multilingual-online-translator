from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if 'fr' in reply and 'en' in reply and 'hello' in reply:
            return CheckResult.true()
        return CheckResult.false('Test failed. Try to print both languages and word you want to translate.')

TranslatorTest('translator.translator').run_tests()