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