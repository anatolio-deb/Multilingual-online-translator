from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
	def generate(self):
		return [TestCase(args=['english', 'korean', 'hello'])]

	def check(self, reply, attach):
		if 'support korean' in reply.lower():
			return CheckResult.true()
		if 'internet connection' in reply.lower():
			return CheckResult.true()

		return CheckResult.false('You did not correctly write that your program did not support korean or You did not hand exception with internet connection')


TranslatorTest('translator.translator').run_tests()