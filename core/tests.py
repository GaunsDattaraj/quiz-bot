from django.test import TestCase
from core.reply_factory import record_current_answer, get_next_question, generate_final_response
from core.constants import PYTHON_QUESTION_LIST

class QuizBotTestCase(TestCase):

    def setUp(self):
        self.session = {
            "current_question_id": None,
            "answers": {}
        }

    def test_record_current_answer_valid(self):
        self.session["current_question_id"] = 0
        answer = "test answer"
        success, error = record_current_answer(answer, 0, self.session)
        self.assertTrue(success)
        self.assertEqual(error, "")
        self.assertEqual(self.session["answers"][0], answer.lower())

    def test_record_current_answer_invalid(self):
        success, error = record_current_answer(None, 0, self.session)
        self.assertFalse(success)
        self.assertEqual(error, "Invalid answer format.")

    def test_record_current_answer_no_question(self):
        success, error = record_current_answer("answer", None, self.session)
        self.assertFalse(success)
        self.assertEqual(error, "No current question to answer.")

    def test_get_next_question_first(self):
        next_question, next_question_id = get_next_question(None)
        self.assertEqual(next_question, PYTHON_QUESTION_LIST[0]["question"])
        self.assertEqual(next_question_id, 0)

    def test_get_next_question_next(self):
        next_question, next_question_id = get_next_question(0)
        self.assertEqual(next_question, PYTHON_QUESTION_LIST[1]["question"])
        self.assertEqual(next_question_id, 1)

    def test_get_next_question_last(self):
        next_question, next_question_id = get_next_question(len(PYTHON_QUESTION_LIST) - 1)
        self.assertIsNone(next_question)
        self.assertIsNone(next_question_id)

    def test_generate_final_response(self):
        self.session["answers"] = {
            0: PYTHON_QUESTION_LIST[0]["answer"].lower(),
            1: "wrong answer"
        }
        response = generate_final_response(self.session)
        total_questions = len(PYTHON_QUESTION_LIST)
        correct_answers = 1
        score = (correct_answers / total_questions) * 100
        expected_response = f"You have completed the quiz. Your score is {score:.2f}%. You answered {correct_answers} out of {total_questions} questions correctly."
        self.assertEqual(response, expected_response)
