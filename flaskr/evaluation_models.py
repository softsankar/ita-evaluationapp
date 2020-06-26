class EvalForm:

    def __init__(self, return_ind, branch, student_id, first_name, middle_name,last_name,
                 email, birth_date, mobile_no, parent_fname, parent_lname,
                 grade, rlevel, wLevel, sLevel, comments):
        self.return_ind = return_ind
        self.branch = branch
        self.student_id = student_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.birth_date = birth_date
        self.mobile_no = mobile_no
        self.parent_fname = parent_fname
        self.parent_lname = parent_lname
        self.grade = grade
        self.read_level = rlevel
        self.write_level = wLevel
        self.speak_level = sLevel
        self.comments = comments

    def fullname(self):
        return '{}'.format(self.name)



class EvalResult:

    def __init__(self, student_id,first_name,last_name,recommended_grade,test_req):
        self.student_id = student_id
        self.eval_grade = recommended_grade
        self.test_required = test_req
        self.first_name = first_name
        self.last_name = last_name


class Skill:

    def __init__(self, grade_level, age, skills, grammar, reading, writing, oral, project):
        self.grade_level = grade_level
        self.age = age
        self.skills = skills
        self.grammar = grammar
        self.reading = reading
        self.writing = writing
        self.oral = oral
        self.project = project
