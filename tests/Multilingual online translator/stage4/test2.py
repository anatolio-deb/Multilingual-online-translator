from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='3\n4\nhello'),]

    def check(self, reply, attach):
        if 'spanish translations' in reply.lower() and 'hola' in reply.lower():
            return CheckResult.true()
        return CheckResult.false('Test failed. Try to print all of languages your translator can to translate')

TranslatorTest('translator.translator').run_tests()