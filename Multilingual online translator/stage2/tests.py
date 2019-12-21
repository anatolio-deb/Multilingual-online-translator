from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if reply.replace("\n", "") == '''Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:Type the word you want to translate:You chose «fr» as a language to translate «hello».
200 OK
['Translation', 'bonjour', 'allô', 'ohé', 'coucou', 'salut', 'hello', 'bonsoir', "quelqu'un", 'bien le bonjour', 'Oh', 'Enchanté', 'saluer', 'ça', 'salue', 'Oui']
['Translation', 'bonjour', 'allô', 'ohé', 'coucou', 'salut', 'hello', 'bonsoir', "quelqu'un", 'bien le bonjour', 'Oh', 'Enchanté', 'saluer', 'ça', 'salue', 'Oui', 'Well, hello, freedom fighters.', 'Et bien, bonjour combattants de la liberté.', '', '', 'Goodbye England and hello the Netherlands...', "Au revoir l'Angleterre et bonjour les Pays-Bas...", '', '', 'Yes, hello. Jackson speaking.', "Oui, allô, Jackson à l'appareil.", '', '', 'Hello, hello, hello, hello.', 'Allô, allô, allô, allô.', '', '', 'And began appearing hello kitty games online.', 'Et a commencé à apparaître bonjour Kitty jeux en ligne.', '', '', 'Tell him hello... and congratulations.', 'Je lui dis bonjour et je le félicite.', '', '', 'A special hello to everyone from YouTube Bibi.', 'Un bonjour spécial à tout le monde de la chaîne de beauté YouTube de bibi.', '', '', 'Yes, hello, Mr Teodoresco.', 'Oui, bonjour, M. Teodoresco.', '', '', 'Well hello, Milan and Eve.', 'Eh bien bonjour, Milan et Eve.', '', '', 'Well hello, welcome to the Tree House pond.', "Alors bonjour, bienvenue à l'étang de la Maison de l'arbre.", '', '', 'pink hello kitty seat 2,3 - Auto Outlet', 'rose bonjour 2,3 siège de minou - Auto Outlet', '', '', 'hello world PL/SQL procedure successfully completed. SQL', 'bonjour procédure monde PL / SQL terminée avec succès. SQL', '', '', '"Maido-san" means something like "hello" in Kanazawa dialect.', 'Maido-sans veut dire quelque chose comme bonjour dans le dialecte de Kanazawa.', '', '', 'So anyway, hello and goodbye.', 'Donc voilà, bonjour et au revoir.', '', '', 'You can hardly hear him saying hello.', "On l'entend à peine dire bonjour.", '', '', "Yes, hello. I'd like to blackmail the Prime Minister.", "Oui, bonjour, j'aimerais faire chanter le premier Ministre.", '', '', 'Well, please tell her hello for us.', 'Bien, dites lui bonjour de notre part.', '', '', 'Homie, I think someone is saying hello.', "Homer, je crois qu'on te dit bonjour.", '', '', 'Well, hello, Susan and welcome.', 'Bien, bonjour Susan et bienvenue.', '', '', 'Normally, one says "hello" only once.', 'Normalement, on dit bonjour une fois.', '', '']
'''.replace("\n", ""):
            return CheckResult.true()
        return CheckResult.false()

TranslatorTest('translator.translator').run_tests()