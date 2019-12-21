from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(args=['english', 'french', 'hello']),
                TestCase(args=['english', 'all', 'hello'])]

    def check(self, reply, attach):
        if reply.replace("\n", "") == '''
French Translations:
bonjour
allô
ohé
coucou
salut
French Examples:
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

'''.replace("\n", "") or reply.replace("\n", "") == '''
Arabic Translations:
مرحبا
Arabic Example:
Well, hello, old-school racist.:
حسنا، مرحبا يا تلميذة المدرسة العنصريّة - الأمر يسري بدمهم!


German Translations:
hallo
German Example:
We agreedellen wolf is innocent. hello.:
Wir waren einverstanden damit, dass Wolf unschuldig ist. Hallo.


Spanish Translations:
hola
Spanish Example:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.


French Translations:
bonjour
French Example:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.


Hebrew Translations:
שלום
Hebrew Example:
Is "hello" too bland?:
האם "שלום" יותר מדי מנומס?


Japanese Translations:
こんにちは
Japanese Example:
The little boy said hello to me.:
小さな男の子が私にこんにちはと言った。


Dutch Translations:
dag
Dutch Example:
That was kind of our funny hello.:
Dat vond we een grappige begroeting.


Polish Translations:
cześć
Polish Example:
I guess it's... goodbye car insurance, hello city bus.:
I domyślam się, że to jest... do widzenia ubezpieczenie samochodu, cześć autobus miejski.


Portuguese Translations:
olá
Portuguese Example:
That was my last kiss hello.:
Pois eu garanto que aquele foi o meu último beijo de olá.


Romanian Translations:
salut
Romanian Example:
Well, hello, professor Culbertson.:
Ei bine, salut, profesor universitar Culbertson.


Russian Translations:
привет
Russian Example:
Why, hello, there, Admiral.:
А, Адмирал, привет, что здесь делаешь.


Turkish Translations:
selam
Turkish Example:
So now little Sabina says hello.:
Velhasıl minik Sabina size selam söylüyor.

'''.replace("\n", ""):
            return CheckResult.true()
        return CheckResult.false()

TranslatorTest('translator.translator').run_tests()