from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if reply == 'Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:Type the word you want to translate:You chose «fr» as a language to translate «hello».\n':
            return CheckResult.true()
        return CheckResult.false()

TranslatorTest('translator.translator').run_tests()