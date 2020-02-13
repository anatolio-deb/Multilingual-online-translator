from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(args=['english', 'french', 'hello'])]

    def check(self, reply, attach):
        if 'french translations' in reply.lower() and 'french examples' in reply.lower():
            return CheckResult.true()
        return CheckResult.false("Test failed. Maybe threre is a mistake in command line args or in output.\n\
         if args==['english', 'french', 'hello'], you should print 'french translations', 'french examples' and so on")

TranslatorTest('translator.translator').run_tests()