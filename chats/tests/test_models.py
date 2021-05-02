from django.test import TestCase
from chats.models import Scenario, Tarot

# Create your tests here.

class ScenarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Scenario.objects.create(
            input_message='오늘의 썸 연애운', 
            output_message='설레지만 애매하고 답답한 우리 사이...\n/images/1\n오늘의 썸 연애운을 타로 카드로 확인해보자',
            next_question='먼저 풀리피의 썸상대를 뭐라고 부르면 좋은지 말해줘')

    def test_input_message_label(self):
        scenario = Scenario.objects.get(id=1)
        field_label = scenario._meta.get_field('input_message').verbose_name
        self.assertEqual(field_label, 'input message')
    
    def test_output_message_label(self):
        scenario = Scenario.objects.get(id=1)
        field_label = scenario._meta.get_field('output_message').verbose_name
        self.assertEqual(field_label, 'output message')
    
    def test_next_question_label(self):
        scenario = Scenario.objects.get(id=1)
        field_label = scenario._meta.get_field('next_question').verbose_name
        self.assertEqual(field_label, 'next question')

    def test_input_message_max_length(self):
        scenario = Scenario.objects.get(id=1)
        max_length = scenario._meta.get_field('input_message').max_length
        self.assertEquals(max_length, 255)
    
    def test_next_question_max_length(self):
        scenario = Scenario.objects.get(id=1)
        max_length = scenario._meta.get_field('next_question').max_length
        self.assertEquals(max_length, 255)

class TarotModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tarot.objects.create(
            card_number=1, 
            card_image='R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==',
            explanation='오.. 농작물을 바라보고 사람이 서있어\n/images/emoticon/2\n나는 고백을 추천한다')

    def test_card_number_label(self):
        tarot = Tarot.objects.get(id=1)
        field_label = tarot._meta.get_field('card_number').verbose_name
        self.assertEqual(field_label, 'card number')
    
    def test_card_image_label(self):
        tarot = Tarot.objects.get(id=1)
        field_label = tarot._meta.get_field('card_image').verbose_name
        self.assertEqual(field_label, 'card image')
    
    def test_explanation_label(self):
        tarot = Tarot.objects.get(id=1)
        field_label = tarot._meta.get_field('explanation').verbose_name
        self.assertEqual(field_label, 'explanation')

    def test_object_name_is_card_number(self):
        tarot = Tarot.objects.get(id=1)
        expected_object_name = f'{tarot.card_number}'
        self.assertEquals(expected_object_name, str(tarot))
