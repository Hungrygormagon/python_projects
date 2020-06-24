class user:
    name = 'No Name Provided'
    email = ' ' 
    password = 'Need new Password'
    user_account = 0


class Teacher(User):
    department = 'History'
    is_coach = 'Yes'

class Student(user):
    gpa = '3.17'
    athelete = 'no'