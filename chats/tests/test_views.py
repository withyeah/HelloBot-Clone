import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from chats.models import Scenario, Tarot


class ScenarioViewSetTestCase(APITestCase):
    def setUp(self):
        self.scenario = Scenario.objects.create(
            input_message="오늘의 썸 연애운",
            output_message="설레지만 애매하고 답답한 우리 사이...\n/images/1\n오늘의 썸 연애운을 타로 카드로 확인해보자",
            next_question="먼저 풀리피의 썸상대를 뭐라고 부르면 좋은지 말해줘",
        )

    def test_scenario_create(self):
        response = self.client.post(
            reverse("scenario-list"),
            {
                "input_message": "풀리피 (이)라고 불러줘",
                "output_message": "풀리피구나 알겠어\n이제 마음을 차분하게 하고\n카드를 한 장 뽑아보자",
                "next_question": "/images/emoticon/1",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json.loads(response.content),
            {
                "id": 2,
                "input_message": "풀리피 (이)라고 불러줘",
                "output_message": "풀리피구나 알겠어\n이제 마음을 차분하게 하고\n카드를 한 장 뽑아보자",
                "next_question": "/images/emoticon/1",
            },
        )

    def test_scenario_list_retreive(self):
        response = self.client.get(reverse("scenario-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_scenario_detail_retrieve(self):
        response = self.client.get(reverse("scenario-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["input_message"], "오늘의 썸 연애운")

    def test_scenario_update(self):
        response = self.client.put(
            reverse("scenario-detail", kwargs={"pk": 1}),
            {
                "input_message": "오늘의 썸 연애운",
                "output_message": "에이스 펜 역방향 뽑았구나\n썸인데 좀처럼 너 맘대로 안돼서 스트레스 좀 받겠어",
                "next_question": "어떤 것 같아?",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {
                "id": 1,
                "input_message": "오늘의 썸 연애운",
                "output_message": "에이스 펜 역방향 뽑았구나\n썸인데 좀처럼 너 맘대로 안돼서 스트레스 좀 받겠어",
                "next_question": "어떤 것 같아?",
            },
        )

    def test_scenario_delete(self):
        response = self.client.delete(reverse("scenario-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TarotViewSetTestCase(APITestCase):
    def setUp(self):
        self.tarot = Tarot.objects.create(
            card_number=1,
            card_image="R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
            explanation="오.. 농작물을 바라보고 사람이 서있어\n/images/emoticon/2\n나는 고백을 추천한다",
        )

    def test_tarot_create(self):
        response = self.client.post(
            reverse("tarot-list"),
            {
                "card_number": 2,
                "card_image": "R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
                "explanation": "에이스 펜 역방향 뽑았구나\n/images/emoticon/3\n이 카드가 뒤집혔으니 데이트 비용에 관한 문제일 수 있겠다",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(
        #     json.loads(response.content),
        #     {
        #         "id": 2,
        #         "card_number": 2,
        #         "card_image": "R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
        #         "explanation": "에이스 펜 역방향 뽑았구나\n/images/emoticon/3\n이 카드가 뒤집혔으니 데이트 비용에 관한 문제일 수 있겠다",
        #     },
        # )

    def test_tarot_list_retreive(self):
        response = self.client.get(reverse("tarot-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tarot_detail_retrieve(self):
        response = self.client.get(reverse("tarot-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["card_number"], 1)

    def test_tarot_update(self):
        response = self.client.put(
            reverse("tarot-detail", kwargs={"pk": 1}),
            {
                "card_number": 2,
                "card_image": "R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
                "explanation": "에이스 펜 역방향 뽑았구나\n/images/emoticon/3\n이 카드가 뒤집혔으니 데이트 비용에 관한 문제일 수 있겠다",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(
        #     json.loads(response.content),
        #     {
        #         "card_number": 2,
        #         "card_image": "R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
        #         "explanation": "에이스 펜 역방향 뽑았구나\n/images/emoticon/3\n이 카드가 뒤집혔으니 데이트 비용에 관한 문제일 수 있겠다",
        #     },
        # )

    def test_tarot_delete(self):
        response = self.client.delete(reverse("tarot-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
