from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(args=['english', 'all', 'hello'])]

    def check(self, reply, attach):
        if 'arabic translation' in reply.lower() and 'arabic example' in reply.lower() and 'russian translation' in reply.lower() and 'russian example' in reply.lower():
            return CheckResult.true()
        return CheckResult.false("Try to print translations and examples of all languages you can. Try to print 'Arabic Translations' or 'Arabic Examples' and other languages should be printed in this style.\n Also, your command line args should be ['english', 'all', 'hello']")

TranslatorTest('translator.translator').run_tests()
