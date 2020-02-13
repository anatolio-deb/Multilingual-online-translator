from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
	def generate(self):
		return [TestCase(stdin='3\n0\nhello'),]

	def check(self, reply, attach):
		with open('hello.txt') as file:
			output = file.read().lower()
			if 'spanish translation' in output and 'spanish example' in output and 'turkish example' in output:
				return CheckResult.true()
		return CheckResult.false('Test failed. Try to write all translations and examples into the output file and name it WORD.txt where WORD is word you want to translate.')

TranslatorTest('translator.translator').run_tests()