from django.test import TestCase
from .models import *
from users.models import Teacher, Student

class CollegeModelTest(TestCase):
    def setUp(self):
        self.college = College.objects.create(name="Vels University")
        self.teacher = Teacher.objects.create(name="Haries", email="hari@example.com")
        self.program = Program.objects.create(college=self.college, name="computer science", semester=1, year=1)

    def test_create_subject_sets_college_from_program(self):
        subject = Subject.objects.create(
            img='some_path',
            title="Data Structures",
            description="Introduction to Data Structures",
            program=self.program,
            teacher=self.teacher,
        )
        # Check that subject's college is the same as the program's college
        self.assertEqual(subject.college, self.program.college)

    def test_create_chapter_sets_college_from_subject(self):
        subject = Subject.objects.create(
            img='some_path',
            title="Algorithms",
            description="Introduction to Algorithms",
            program=self.program,
            teacher=self.teacher,
        )
        chapter = Chapter.objects.create(
            name="Sorting Algorithms",
            description="Different types of sorting algorithms",
            subject=subject,
        )
        # Check that chapter's college is the same as the subject's college
        self.assertEqual(chapter.college, subject.college)

    def test_program_str_representation(self):
        self.assertEqual(str(self.program), f"Computer Science - {self.college} - Semester 1")

    def test_subject_str_representation(self):
        subject = Subject.objects.create(
            img='some_path',
            title="Operating Systems",
            program=self.program,
            teacher=self.teacher
        )
        self.assertEqual(str(subject), "Operating Systems")

    def test_chapter_str_representation(self):

        subject = Subject.objects.create(
            img='some_path',
            title="Databases",
            program=self.program,
            teacher=self.teacher
        )
        chapter = Chapter.objects.create(
            name="SQL Queries",
            subject=subject
        )
        self.assertEqual(str(chapter), f"SQL Queries - {chapter.id}")


class ChapterItemModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Computer Science", semester=1, year=1)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Data Structures",
            program=self.program,
            teacher=self.teacher,
        )
        self.chapter = Chapter.objects.create(
            name="Introduction to Data Structures",
            subject=self.subject
        )

    def test_chapter_item_creation(self):
        """Test creating a ChapterItem object."""
        chapter_item = ChapterItem.objects.create(
            description="Stacks and Queues",
            chapter=self.chapter
        )
        self.assertEqual(chapter_item.description, "Stacks and Queues")
        self.assertEqual(str(chapter_item), f"{self.chapter.name} - Item {chapter_item.description} - {chapter_item.id}")

class SubjectProgressModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Computer Science", semester=1, year=1)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Operating Systems",
            program=self.program,
            teacher=self.teacher,
        )
        self.student = Student.objects.create(name="Jane Smith", email="jane@example.com")

    def test_subject_progress(self):
        """Test subject progress logic."""
        progress = SubjectProgress.objects.create(
            subject=self.subject,
            student=self.student,
            progress=100
        )
        self.assertTrue(progress.completed)
        self.assertEqual(str(progress), f"{self.student.name} - {self.subject.title} Progress")


class ChapterQuizModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Mechanical Engineering", semester=2, year=1)
        self.teacher = Teacher.objects.create(name="Dr. John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Thermodynamics",
            program=self.program,
            teacher=self.teacher,
        )
        self.chapter = Chapter.objects.create(
            name="Thermodynamics Basics",
            subject=self.subject
        )

    def test_chapter_quiz_creation(self):
        """Test creating a ChapterQuiz object."""
        quiz = ChapterQuiz.objects.create(
            chapter=self.chapter,
            question="What is the first law of thermodynamics?",
            choice_a="Energy can be created",
            choice_b="Energy cannot be destroyed",
            choice_c="Energy cannot be transferred",
            choice_d="Energy is always constant",
            correct_answer="B"
        )
        self.assertEqual(str(quiz), f"{self.chapter.name} - Quiz {quiz.id}")
        self.assertTrue(quiz.active)


class StudentChapterQuizAnswerModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Civil Engineering", semester=3, year=2)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Fluid Mechanics",
            program=self.program,
            teacher=self.teacher,
        )
        self.chapter = Chapter.objects.create(
            name="Hydraulics",
            subject=self.subject
        )
        self.quiz = ChapterQuiz.objects.create(
            chapter=self.chapter,
            question="What is Bernoulli's principle?",
            choice_a="Relates pressure to velocity",
            choice_b="Relates pressure to gravity",
            choice_c="Relates energy to flow",
            choice_d="None of the above",
            correct_answer="A"
        )
        self.student = Student.objects.create(name="Mark Brown", email="mark@example.com")

    def test_student_quiz_answer(self):
        """Test student's quiz answer."""
        answer = StudentChapterQuizAnswer.objects.create(
            chapterquiz=self.quiz,
            chapter=self.chapter,
            student=self.student,
            selected_answer="A"
        )
        self.assertTrue(answer.is_correct)
        answer.selected_answer = "B"
        answer.save()
        self.assertFalse(answer.is_correct)


class StudentChapterQuizProgressPercentModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Electrical Engineering", semester=4, year=2)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Circuits",
            program=self.program,
            teacher=self.teacher,
        )
        self.chapter = Chapter.objects.create(
            name="Basic Circuit Theory",
            subject=self.subject
        )
        self.student = Student.objects.create(name="Lucy White", email="lucy@example.com")

        # Create quizzes
        for i in range(5):
            ChapterQuiz.objects.create(
                chapter=self.chapter,
                question=f"Question {i+1}",
                choice_a="A",
                choice_b="B",
                choice_c="C",
                choice_d="D",
                correct_answer="A"
            )

    def test_calculate_pass_percentage(self):
        """Test calculating quiz pass percentage."""
        # Answer quizzes, 3 correct and 2 incorrect
        correct_quizzes = ChapterQuiz.objects.filter(chapter=self.chapter)[:3]
        wrong_quizzes = ChapterQuiz.objects.filter(chapter=self.chapter)[3:]

        for quiz in correct_quizzes:
            StudentChapterQuizAnswer.objects.create(
                chapterquiz=quiz,
                chapter=self.chapter,
                student=self.student,
                selected_answer="A",
                is_correct=True
            )

        for quiz in wrong_quizzes:
            StudentChapterQuizAnswer.objects.create(
                chapterquiz=quiz,
                chapter=self.chapter,
                student=self.student,
                selected_answer="B",
                is_correct=False
            )

        progress = StudentChapterQuizProgressPercent.objects.create(
            chapter=self.chapter,
            student=self.student,
            progress=0
        )
        pass_percentage = progress.calculate_pass_percentage()
        self.assertEqual(pass_percentage, 60.0)  # 3 correct out of 5 is 60%


class StudentChapterQuizAttendedModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Aeronautical Engineering", semester=2, year=1)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Flight Mechanics",
            program=self.program,
            teacher=self.teacher,
        )
        self.chapter = Chapter.objects.create(
            name="Lift and Drag",
            subject=self.subject
        )
        self.student = Student.objects.create(name="Jake Green", email="jake@example.com")

    def test_student_attended_quiz(self):
        """Test student's quiz attendance."""
        attendance = StudentChapterQuizAttended.objects.create(
            chapter=self.chapter,
            student=self.student,
            attended=True,
            blocked=False
        )
        self.assertTrue(attendance.attended)
        self.assertFalse(attendance.blocked)
        self.assertEqual(str(attendance), f"{self.student.name} - {self.chapter.name}")



class SubjectQuestionModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Information Technology", semester=1, year=1)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Computer Networks",
            program=self.program,
            teacher=self.teacher,
        )
        self.student = Student.objects.create(name="Alice", email="alice@example.com")

    def test_subject_question_creation(self):
        """Test creating a SubjectQuestion object."""
        subject_question = SubjectQuestion.objects.create(
            subject=self.subject,
            student=self.student,
            title="What is TCP?",
            question="Could you explain what TCP is and how it works in networking?"
        )
        self.assertEqual(subject_question.title, "What is TCP?")
        self.assertEqual(str(subject_question), f"{self.student.name} - {self.subject.title} - Question {subject_question.id}")


class QuestionAnswersModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Information Technology", semester=2, year=1)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Operating Systems",
            program=self.program,
            teacher=self.teacher,
        )
        self.student = Student.objects.create(name="Bob", email="bob@example.com")
        self.question = SubjectQuestion.objects.create(
            subject=self.subject,
            student=self.student,
            title="What is a process?",
            question="Could you explain what a process is in operating systems?"
        )

    def test_question_answer_creation(self):
        """Test creating a QuestionAnswers object."""
        answer = QuestionAnswers.objects.create(
            subjectquestion=self.question,
            student=self.student,
            answer="A process is a program in execution."
        )
        self.assertEqual(answer.answer, "A process is a program in execution.")
        self.assertEqual(str(answer), f"Answer to {self.question}")


class SubjectNotesModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Computer Science", semester=1, year=1)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Data Structures",
            program=self.program,
            teacher=self.teacher,
        )
        self.student = Student.objects.create(name="Charlie", email="charlie@example.com")

    def test_subject_notes_creation(self):
        """Test creating a SubjectNotes object."""
        notes = SubjectNotes.objects.create(
            subject=self.subject,
            student=self.student,
            title="Notes on Stacks",
            notes="Stacks are abstract data types that follow the LIFO principle."
        )
        self.assertEqual(notes.title, "Notes on Stacks")
        self.assertEqual(str(notes.title), "Notes on Stacks")



class TeacherSubjectSessionModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Mathematics", semester=1, year=1)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Linear Algebra",
            program=self.program,
            teacher=self.teacher,
        )
        self.chapter = Chapter.objects.create(
            name="Matrices",
            subject=self.subject
        )
        self.chapter_item = ChapterItem.objects.create(
            description="Matrix Operations",
            chapter=self.chapter
        )

    def test_teacher_subject_session_creation(self):
        """Test creating a TeacherSubjectSession object and that subject and chapter are set correctly."""
        session = TeacherSubjectSession.objects.create(
            teacher=self.teacher,
            chapteritem=self.chapter_item,
            TTBC="Matrix Inverses",
            starttime=time(9, 0),
            endtime=time(10, 0),
            date=date(2024, 10, 1)
        )
        self.assertEqual(session.subject, self.subject)
        self.assertEqual(session.chapter, self.chapter)
        self.assertEqual(session.time_duration, "09:00:00 - 10:00:00")
        self.assertEqual(str(session), f"{self.teacher.name} - {self.chapteritem.description} - {session.date}")


class TeacherDateSessionCompleteModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.teacher = Teacher.objects.create(name="Jane Smith", email="jane@example.com")

    def test_teacher_date_session_complete(self):
        """Test creating a TeacherDateSessionComplete object."""
        session_complete = TeacherDateSessionComplete.objects.create(
            teacher=self.teacher,
            date=date(2024, 10, 1),
            completed=True
        )
        self.assertTrue(session_complete.completed)
        self.assertEqual(session_complete.date, date(2024, 10, 1))
        self.assertEqual(str(session_complete), f"{self.teacher.name} - {session_complete.date}")


class TeacherAddOnSessionModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.teacher = Teacher.objects.create(name="Mark Brown", email="mark@example.com")

    def test_teacher_add_on_session_creation(self):
        """Test creating a TeacherAddOnSession object and ensuring time_duration is calculated correctly."""
        add_on_session = TeacherAddOnSession.objects.create(
            teacher=self.teacher,
            TTBC="Advanced Calculus",
            starttime=time(14, 0),
            endtime=time(15, 30),
            date=date(2024, 10, 1)
        )
        self.assertEqual(add_on_session.time_duration, "14:00:00 - 15:30:00")
        self.assertEqual(add_on_session.action, "Pending")
        self.assertFalse(add_on_session.reported)
        self.assertFalse(add_on_session.finished)
        self.assertEqual(str(add_on_session), f"{self.teacher.name} - {add_on_session.date}")




class StudentAttendanceModelTest(TestCase):
    def setUp(self):
        """Set up objects to use in tests."""
        self.college = College.objects.create(name="Vels University")
        self.program = Program.objects.create(college=self.college, name="Physics", semester=1, year=1)
        self.teacher = Teacher.objects.create(name="John Doe", email="john@example.com")
        self.student = Student.objects.create(name="Alice", email="alice@example.com")
        self.subject = Subject.objects.create(
            img='some_path',
            title="Quantum Mechanics",
            program=self.program,
            teacher=self.teacher,
        )
        self.chapter = Chapter.objects.create(
            name="Quantum Theories",
            subject=self.subject
        )
        self.chapter_item = ChapterItem.objects.create(
            description="Introduction to Quantum Theories",
            chapter=self.chapter
        )
        self.session = TeacherSubjectSession.objects.create(
            teacher=self.teacher,
            chapteritem=self.chapter_item,
            TTBC="Basic quantum concepts",
            starttime="09:00",
            endtime="10:00",
            date=date(2024, 10, 1)
        )

    def test_student_attendance_creation(self):
        """Test creating a StudentAttendance object with default values."""
        attendance = StudentAttendance.objects.create(
            student=self.student,
            date=date(2024, 10, 1),
            session=self.session,
            teacher=self.teacher,
        )
        self.assertTrue(attendance.present)
        self.assertEqual(attendance.student, self.student)
        self.assertEqual(attendance.session, self.session)
        self.assertEqual(attendance.teacher, self.teacher)
        self.assertIsNone(attendance.review)
        self.assertIsNone(attendance.review_text)

    def test_student_attendance_with_review(self):
        """Test creating a StudentAttendance object with a review."""
        attendance = StudentAttendance.objects.create(
            student=self.student,
            date=date(2024, 10, 2),
            session=self.session,
            teacher=self.teacher,
            review='1',  # Very Good
            review_text="Excellent class!"
        )
        self.assertEqual(attendance.review, '1')
        self.assertEqual(attendance.review_text, "Excellent class!")
        self.assertTrue(attendance.present)

    def test_student_absence(self):
        """Test marking a student as absent."""
        attendance = StudentAttendance.objects.create(
            student=self.student,
            date=date(2024, 10, 3),
            session=self.session,
            teacher=self.teacher,
            present=False
        )
        self.assertFalse(attendance.present)
        self.assertEqual(attendance.date, date(2024, 10, 3))

    def test_review_choices(self):
        """Test that the review choices are correct."""
        attendance = StudentAttendance.objects.create(
            student=self.student,
            date=date(2024, 10, 4),
            session=self.session,
            teacher=self.teacher,
            review='2',  # Good
            review_text="Good session, learned a lot."
        )
        self.assertEqual(attendance.review, '2')
        self.assertEqual(attendance.review_text, "Good session, learned a lot.")