from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from django.test import TestCase
from django.test import RequestFactory
from django.conf import settings
from rest_framework import status
import jwt
from unittest.mock import patch
from authentication.models import Student
from myapp.models import Subject as SubjectModel
from myappl.serializers import SubjectSerializer
from django.contrib.auth.models import User


# Assuming the authenticate function is in a module named 'authentication'
from authentication.views import authenticate

class AuthenticateFunctionTest(TestCase):
    def setUp(self):
        
        self.factory = RequestFactory()
        self.valid_token_payload = {
            'user_id': 1,
            'username': 'testuser',
        }
        self.invalid_token = "invalid.token.here"
        self.valid_token = jwt.encode(self.valid_token_payload, settings.SECRET_KEY, algorithm="HS256")

    def test_missing_token(self):
        request = self.factory.get('/some-url/')
        response = authenticate(request)
        
        self.assertEqual(response['message'], "jwt token is missing...")
        self.assertEqual(response['status'], status.HTTP_401_UNAUTHORIZED)

    def test_wrong_scheme(self):
        request = self.factory.get('/some-url/', HTTP_AUTHORIZATION=f'Token {self.valid_token}')
        response = authenticate(request)
        
        self.assertEqual(response['message'], "Wrong Scheme....")
        self.assertEqual(response['status'], status.HTTP_400_BAD_REQUEST)

    def test_invalid_token(self):
        request = self.factory.get('/some-url/', HTTP_AUTHORIZATION=f'Bearer {self.invalid_token}')
        
        with patch('jwt.decode', side_effect=jwt.InvalidTokenError):
            response = authenticate(request)
        
        self.assertEqual(response['message'], "Invalid Token")
        self.assertEqual(response['status'], status.HTTP_401_UNAUTHORIZED)

    def test_valid_token(self):

        request = self.factory.get('/some-url/', HTTP_AUTHORIZATION=f'Bearer {self.valid_token}')
        
        with patch('jwt.decode', return_value=self.valid_token_payload):
            response = authenticate(request)
        
        self.assertEqual(response, self.valid_token_payload)

c
class SubjectAPIViewTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.student = Student.objects.create(student_id=1, program_id=101)
        self.subject1 = SubjectModel.objects.create(subject_id=1, subject_name="Math", program_id=101)
        self.subject2 = SubjectModel.objects.create(subject_id=2, subject_name="Science", program_id=101)
        
        self.valid_token_payload = {
            'user_id': self.student.student_id
        }
        self.invalid_token = "invalid.token.here"
        self.valid_token = jwt.encode(self.valid_token_payload, settings.SECRET_KEY, algorithm="HS256")

    def test_get_subjects_with_valid_token(self):
        # Mock the valid token and simulate the request
        with patch('jwt.decode', return_value=self.valid_token_payload):
            response = self.client.get(
                reverse('subject-list'),  # Assuming your url name is 'subject-list'
                HTTP_AUTHORIZATION=f'Bearer {self.valid_token}'
            )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        subjects = SubjectModel.objects.filter(program_id=self.student.program_id)
        serializer = SubjectSerializer(subjects, many=True, context={'student': self.student})
        self.assertEqual(response.data['subjects'], serializer.data)

    def test_get_subjects_with_invalid_token(self):
        with patch('jwt.decode', side_effect=jwt.InvalidTokenError):
            response = self.client.get(
                reverse('subject-list'),  # Assuming your url name is 'subject-list'
                HTTP_AUTHORIZATION=f'Bearer {self.invalid_token}'
            )
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], "Invalid Token")

    def test_get_subjects_with_missing_token(self):
        response = self.client.get(reverse('subject-list'))
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], "jwt token is missing...")

    def test_get_subjects_student_not_found(self):
        invalid_student_payload = {
            'user_id': 99999  # A non-existent student ID
        }
        invalid_student_token = jwt.encode(invalid_student_payload, settings.SECRET_KEY, algorithm="HS256")
        
        with patch('jwt.decode', return_value=invalid_student_payload):
            response = self.client.get(
                reverse('subject-list'),  # Assuming your url name is 'subject-list'
                HTTP_AUTHORIZATION=f'Bearer {invalid_student_token}'
            )
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], "Student not found")

class SubjectDetailViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.subject = Subject.objects.create(subject_id=1, subject_name="Math")
        self.chapter1 = Chapter.objects.create(chapter_id=1, chapter_name="Algebra", subject_id=self.subject.subject_id)
        self.chapter2 = Chapter.objects.create(chapter_id=2, chapter_name="Geometry", subject_id=self.subject.subject_id)

        self.valid_token_payload = {
            'user_id': 1
        }
        self.invalid_token = "invalid.token.here"
        self.valid_token = jwt.encode(self.valid_token_payload, settings.SECRET_KEY, algorithm="HS256")

    def test_get_subject_chapters_with_valid_token(self):
        
        with patch('jwt.decode', return_value=self.valid_token_payload):
            response = self.client.get(
                reverse('subject-detail', args=[self.subject.subject_id]),  # Assuming URL name is 'subject-detail'
                HTTP_AUTHORIZATION=f'Bearer {self.valid_token}'
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        chapters = Chapter.objects.filter(subject_id=self.subject.subject_id).order_by('updated')
        serializer = ChapterSerializer(chapters, many=True)

        self.assertEqual(response.data, serializer.data)

    def test_get_subject_chapters_with_invalid_token(self):
        
        with patch('jwt.decode', side_effect=jwt.InvalidTokenError):
            response = self.client.get(
                reverse('subject-detail', args=[self.subject.subject_id]),
                HTTP_AUTHORIZATION=f'Bearer {self.invalid_token}'
            )

        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], "Invalid Token")

    def test_get_subject_chapters_with_missing_token(self):
        
        response = self.client.get(reverse('subject-detail', args=[self.subject.subject_id]))

        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], "jwt token is missing...")

    def test_get_subject_chapters_not_found(self):
        
        non_existent_subject_id = 999
        with patch('jwt.decode', return_value=self.valid_token_payload):
            response = self.client.get(
                reverse('subject-detail', args=[non_existent_subject_id]),
                HTTP_AUTHORIZATION=f'Bearer {self.valid_token}'
            )

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, []) 

class ChapterItemDetailViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        
        self.chapter_item = ChapterItem.objects.create(id=1,title="chapter 1 Item",content = "This is a chapter item content.")

        self.valid_token_payload= {
            'user_id': 1
        }
        self.invalid_token = "invalid.token.here"
        self.valid_token = jwt.encode(self.valid_token_payload,settings.SECRET_KEY,algorithm="HS256")

    def test_get_chapter_item_with_valid_token(self):
        with patch('jwt.decode',return_value=self.valid_token_payload):
            response = self.client.get(
                reverse('chapter-item-detail',args=[self.chapter_item.id]),
                HTTP_AUTHORIZATION = f'Bearer {self.valid_token}'
            )
            self.assertEqual(response.status_code,status.HTTP_200_OK)

            serializer = CustomChapterItemSerializer(self.chapter_item)

            self.assertEqual(response.data['chapteritems'],serializer.data)

    def test_get_chapter_item_with_invalid_token(self):

        with patch('jwt.decode',side_effect=jwt.InvalidTokenError):
            response = self.client.get(
                reverse('chapter-item-detail',args=[self.chapter_item.id]),
                HTTP_AUTHORIZATION = f'Bearer {self.invalid_token}'
            )

            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(response.data['message'],"Invalid Token")

    def test_get_chapter_item_with_missing_token(self):

        response = self.client.get(reverse('chapter-item-detail',args=self.chapter_item.id))

        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'],"jwt token is missing...")

    def test_get_chapter_item_not_found(self):
        non_existent_chapter_item_id =999
        with patch('jwt.decode',return_value=self.valid_token_payload):
            response = self.client.get(
                reverse('chapter-item-detail',args=[non_existent_chapter_item_id]),
                HTTP_AUTHORIZATION=F'Bearer {self.valid_token}'
            )
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'],"Chapter item not found")

class PasswordResetViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(user_id=1, username='testuser', password='oldpassword')
        
        self.valid_token_payload = {
            'user_id': self.user.user_id
        }
        self.invalid_token = "invalid.token.here"
        self.valid_token = jwt.encode(self.valid_token_payload, settings.SECRET_KEY, algorithm="HS256")

    def test_password_reset_with_valid_token_and_correct_password(self):
        with patch('jwt.decode', return_value=self.valid_token_payload):
            response = self.client.post(
                reverse('password-reset'),  
                data={
                    'currentPassword': 'oldpassword',
                    'newPassword': 'newpassword123'
                },
                HTTP_AUTHORIZATION=f'Bearer {self.valid_token}'
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Passwoed has been changed')

        self.user.refresh_from_db() 
        self.assertTrue(self.user.check_password('newpassword123'))

    def test_password_reset_with_invalid_token(self):
        with patch('jwt.decode', side_effect=jwt.InvalidTokenError):
            response = self.client.post(
                reverse('password-reset'),
                data={
                    'currentPassword': 'oldpassword',
                    'newPassword': 'newpassword123'
                },
                HTTP_AUTHORIZATION=f'Bearer {self.invalid_token}'
            )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], 'Invalid Token')

    def test_password_reset_with_missing_token(self):
        response = self.client.post(
            reverse('password-reset'),
            data={
                'currentPassword': 'oldpassword',
                'newPassword': 'newpassword123'
            }
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], 'jwt token is missing...')

    def test_password_reset_with_incorrect_current_password(self):
        with patch('jwt.decode', return_value=self.valid_token_payload):
            response = self.client.post(
                reverse('password-reset'),
                data={
                    'currentPassword': 'wrongpassword',
                    'newPassword': 'newpassword123'
                },
                HTTP_AUTHORIZATION=f'Bearer {self.valid_token}'
            )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], 'Current password is incorrect...')

    def test_password_reset_user_not_found(self):
        invalid_user_payload = {
            'user_id': 999  
        }
        invalid_user_token = jwt.encode(invalid_user_payload, settings.SECRET_KEY, algorithm="HS256")

        with patch('jwt.decode', return_value=invalid_user_payload):
            response = self.client.post(
                reverse('password-reset'),
                data={
                    'currentPassword': 'oldpassword',
                    'newPassword': 'newpassword123'
                },
                HTTP_AUTHORIZATION=f'Bearer {invalid_user_token}'
            )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], "This user doesn't exist...")


    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        self.chapter_id = 1

        self.quiz_1 = ChapterQuiz.objects.create(chapter_id=self.chapter_id, active=True)
        self.quiz_2 = ChapterQuiz.objects.create(chapter_id=self.chapter_id, active=True)
        self.inactive_quiz = ChapterQuiz.objects.create(chapter_id=self.chapter_id, active=False)

        self.valid_token = 'valid_token_here'

    @patch('your_app.views.AuthenticateView')
    def test_quiz_ids_with_valid_authentication(self, mock_authenticate_view):

        mock_authenticate_view.return_value = {'user_id': self.user.id}

        url = reverse('quiz-id-view', args=[self.chapter_id])  # Assuming your URL is named 'quiz-id-view'
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.valid_token}')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('chapterquizid', response.data)
        self.assertEqual(len(response.data['chapterquizid']), 2)  # Only active quizzes should be included

    @patch('your_app.views.AuthenticateView')
    def test_quiz_ids_with_invalid_authentication(self, mock_authenticate_view):

        mock_authenticate_view.return_value = {'message': 'Invalid token', 'status': status.HTTP_401_UNAUTHORIZED}

        url = reverse('quiz-id-view', args=[self.chapter_id])
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer invalid_token')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], 'Invalid token')

    @patch('your_app.views.AuthenticateView')
    def test_quiz_ids_with_no_active_quizzes(self, mock_authenticate_view):

        mock_authenticate_view.return_value = {'user_id': self.user.id}

        ChapterQuiz.objects.filter(chapter_id=self.chapter_id).update(active=False)

        url = reverse('quiz-id-view', args=[self.chapter_id])
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.valid_token}')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['chapterquizid'], [])

    @patch('your_app.views.AuthenticateView')
    def test_quiz_ids_for_nonexistent_chapter(self, mock_authenticate_view):

        mock_authenticate_view.return_value = {'user_id': self.user.id}

        url = reverse('quiz-id-view', args=[999])
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.valid_token}')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['chapterquizid'], [])



