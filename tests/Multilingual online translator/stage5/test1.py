from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='3\n0\nhello')]

    def check(self, reply, attach):

        if 'arabic translations' in reply.lower() and 'arabic examples' in reply.lower() and 'russian examples' in reply.lower() and 'russian examples' in reply.lower():
            return CheckResult.true()
        return CheckResult.false('Try to print translations and examples of all languages you can. Try to print "Arabic Translations" or "Arabic Examples" and other languages should be printed in this style')
TranslatorTest('translator.translator').run_tests()