from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if reply.count('[') == 2 and 'Translation' in reply:
            return CheckResult.true()
        return CheckResult.false("Test failed. Try to print lists of translations in both stages or not to delete first word 'Translation' from it")

TranslatorTest('translator.translator').run_tests()