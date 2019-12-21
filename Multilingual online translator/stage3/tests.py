from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if reply.replace("\n", "") == '''Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:Type the word you want to translate:You chose «fr» as a language to translate «hello».
200 OK

Fr Translations:
bonjour
allô
ohé
coucou
salut

Fr Examples:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.
Goodbye England and hello the Netherlands...:
Au revoir l'Angleterre et bonjour les Pays-Bas...
Yes, hello. Jackson speaking.:
Oui, allô, Jackson à l'appareil.
Hello, hello, hello, hello.:
Allô, allô, allô, allô.
And began appearing hello kitty games online.:
Et a commencé à apparaître bonjour Kitty jeux en ligne.

'''.replace("\n", ""):
            return CheckResult.true()
        return CheckResult.false()

TranslatorTest('translator.translator').run_tests()