class GetSubjectTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('get_subject')
        self.user_id = 1
        self.user = User.objects.create(user_id = 1)
        self.college = College.objects.create(id=1)
        self.program = Program.objects.create(id = 1,college=self.college)
        self.teacher = Teacher.objects.create(teacher_id=self.user_id,user=self.user)
        self.student = Student.objects.create(student_id=self.user_id,user=self.user,program=self.program)
        self.subject1 = Subject.objects.create(title='Maths',program=self.program,teacher=self.teacher)
        self.subject2 = Subject.objects.create(title='Science',program=self.program,teacher=self.teacher)

    @patch('api.views.authenticate')
    def test_invalid_token(self,mock_authenticate):
        mock_authenticate.return_value = {'message':'Invalid token','status':status.HTTP_401_UNAUTHORIZED}

        response = self.client.get(self.url)

        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'],'Invalid token')
    
    @patch('api.views.authenticate')
    def test_valid_request_with_subjects(self,mock_authenticate):
        mock_authenticate.return_value = {'user_id':self.user_id}

        response = self.client.get(self.url)

        subjects = Subject.objects.filter(program_id=self.student.program_id)

        serializer = SubjectSerializer(subjects,many=True,context = {'student':self.student})

        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.assertEqual(response.data['subjects'],serializer.data)



from django.test import TestCase
from django.contrib.auth import get_user_model
from api.models import College ,Student,Teacher,Program # Assuming you have a College model
from unittest.mock import patch

User = get_user_model()

#Testing user model
class UserModelTest(TestCase):
    
    def setUp(self):
        """Create a College instance for the ForeignKey reference."""
        self.college = College.objects.create(name="Test College")
    
    @patch('random.randint')
    def test_user_model_save(self, mock_randint):
        """
        Test that a new user is created, the user_id is generated correctly,
        and the password is hashed.
        """
        mock_randint.return_value = 12345  # Mock the random number generation

        # Create a new user
        user = User(
            name="MockStudent7",
            user_type="student",
            dob="2006-01-01",
            email="Mock@example.com",
            college=self.college,
            password="testpassword123"
        )
        user.save()

        # Test if the password is hashed
        self.assertNotEqual(user.password, "testpassword123")
        self.assertTrue(user.check_password("testpassword123"))

        # Test user_id generation
        expected_user_id = f"{self.college}-student-12345"
        self.assertEqual(user.user_id, expected_user_id)

        # Test if the string representation of the user is the user_id
        self.assertEqual(str(user), expected_user_id)
        
    def test_superuser_str_representation(self):
        """
        Test that the string representation returns the name for superusers.
        """
        superuser = User.objects.create_superuser(
            username="superuser",
            name="Admin User",
            email="admin@example.com",
            password="adminpassword123"
        )
        self.assertEqual(str(superuser), "Admin User")
        
    def test_non_superuser_str_representation(self):
        """
        Test that the string representation returns user_id for non-superusers.
        """
        user = User.objects.create(
            name="MockStudent7",
            user_type="student",
            email="Mock@example.com",
            college=self.college,
            password="testpassword123"
        )
        user.save()
        self.assertEqual(str(user), user.user_id)

    
# Testcase for Student and Teacher
class UserCreationSignalTest(TestCase):

    def setUp(self):
        """Set up initial data for the test."""
        # Create a College instance for the ForeignKey reference in User model
        self.college = College.objects.create(name="Test College")
        # Create a Program instance for the ForeignKey reference in Student model
        self.program = Program.objects.create(name="Test Program")
        
    @patch('random.randint')
    def test_student_model_creation_on_user_creation(self, mock_randint):
        """
        Test that a Student model is created when a User with user_type='student' is created.
        """
        mock_randint.return_value = 12345  # Mock the random number generation

        # Create a User with user_type='student'
        user = User.objects.create(
            name="John Doe",
            user_type="student",
            email="john.doe@example.com",
            college=self.college,
            password="testpassword123"
        )

        # Ensure that the Student model is created
        student = Student.objects.get(user=user)

        # Check that the student_id and name are correctly set
        expected_student_id = f"{user.user_id}"
        self.assertEqual(student.student_id, expected_student_id)
        self.assertEqual(student.name, user.username)

        # Check that the string representation is correct
        self.assertEqual(str(student), f"{student.name}-{student.student_id}")
    
    @patch('random.randint')
    def test_teacher_model_creation_on_user_creation(self, mock_randint):
        """
        Test that a Teacher model is created when a User with user_type='teacher' is created.
        """
        mock_randint.return_value = 54321  # Mock the random number generation

        # Create a User with user_type='teacher'
        user = User.objects.create(
            name="Jane Smith",
            user_type="teacher",
            email="jane.smith@example.com",
            college=self.college,
            password="testpassword456"
        )

        # Ensure that the Teacher model is created
        teacher = Teacher.objects.get(user=user)

        # Check that the teacher_id and name are correctly set
        expected_teacher_id = f"{user.user_id}"
        self.assertEqual(teacher.teacher_id, expected_teacher_id)
        self.assertEqual(teacher.name, user.username)

        # Check that the string representation is correct
        self.assertEqual(str(teacher), f"{teacher.name}-{teacher.teacher_id}")

    def test_no_student_teacher_creation_for_other_user_types(self):
        """
        Ensure that no Student or Teacher models are created for non-student and non-teacher users.
        """
        # Create a User with user_type='admin'
        user = User.objects.create(
            name="Admin User",
            user_type="admin",
            email="admin@example.com",
            college=self.college,
            password="adminpassword789"
        )

        # Ensure that no Student or Teacher models are created
        self.assertFalse(Student.objects.filter(user=user).exists())
        self.assertFalse(Teacher.objects.filter(user=user).exists())



list