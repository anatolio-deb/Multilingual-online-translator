from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(args=['english', 'korean', 'hello']),
                TestCase(args=['english', 'all', 'brrrrrrrrrrr'])]

    def check(self, reply, attach):
        if reply.replace("\n", "").strip() == "Sorry, the program doesn't support korean!" :
            return CheckResult.true()
        if reply.replace("\n", "").strip() == "Something wrong with your internet connection":
            return CheckResult.true()
        if reply.replace("\n", "").strip() == "Sorry, unable to find brrrrrrrrrrr":
            return CheckResult.true()
        return CheckResult.false()

TranslatorTest('translator.translator').run_tests()