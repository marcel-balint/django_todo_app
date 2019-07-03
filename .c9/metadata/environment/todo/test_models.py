{"filter":false,"title":"test_models.py","tooltip":"/todo/test_models.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":17,"column":34},"action":"insert","lines":["    ","from django.test import TestCase","from .models import Item","","","class TestItemModel(TestCase):","","    def test_done_defaults_to_False(self):","        item = Item(name=\"Create a Test\")","        item.save()","        self.assertEqual(item.name, \"Create a Test\")","        self.assertFalse(item.done)","    ","    def test_can_create_an_item_with_a_name_and_status(self):","        item = Item(name=\"Create a Test\", done=True)","        item.save()","        self.assertEqual(item.name, \"Create a Test\")","        self.assertTrue(item.done)"],"id":1}],[{"start":{"row":0,"column":4},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":0,"column":4},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1562163333636,"hash":"57ebc884fa82fa68010cdadbe42391c4134efa45"}