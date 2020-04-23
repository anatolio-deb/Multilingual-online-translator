from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(args=['english', 'all', 'brrrrrrrrrrr'])]

    def check(self, reply, attach):
        if "internet connection" in reply.lower():
            return CheckResult.true()
        if 'unable' in reply.lower():
            return CheckResult.true()
        return CheckResult.false('You did not hand exception with imagine word. If translator cannot translate word, you should show it\nOr You did not hand exception with internet connection')

TranslatorTest('translator.translator').run_tests()