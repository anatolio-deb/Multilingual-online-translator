from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='3\n4\nhello'),]

    def check(self, reply, attach):
        if reply.replace("\n", "") == '''Hello, you're welcome to translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type number of your language: Type number of language you want to traslate on: Type word you want to translate: 
Spanish Translations:
hola
buenos días
qué tal
saludo
buen día
Spanish Examples:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.
He didn't introduce us, so hello.:
No nos presentó, así que hola.
Well, hello, Prince Charming.:
Vaya, hola, Príncipe Azul.
In addition, fast delivery. hello Laura.:
Además, la entrega rápida. hola Laura.
L: Well, hello, my dear secretary.:
A: Bien, hola, mi querida secretaria.

'''.replace("\n", ""):
            return CheckResult.true()
        return CheckResult.false()

TranslatorTest('translator.translator').run_tests()