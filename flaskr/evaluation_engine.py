
from flaskr.evaluation_models import EvalForm
from flaskr import dateutil as du

class EvaluationEngine:

    def __init__(self, cut_of_date):
        self.dob_as_of = cut_of_date

    def determine_grade(self,evaluation_form):
        age = du.find_age(evaluation_form.birth_date,self.dob_as_of)
        is_test_req = True
        evaluation_grade = ''
        if (age >= 3 and age < 4):
            evaluation_grade = 'Preschool-1'
            g_age = 3
            is_test_req = False
        elif (age >= 4 and age < 5):
            evaluation_grade = 'preschool-2'
            is_test_req = False
            g_age = 4
        if (age >= 5 and age < 6):
            evaluation_grade = 'Basic-1'
            is_test_req = False
            g_age = 5
        elif (age >= 6 and age < 7):
            evaluation_grade = 'Basic-2'
            g_age = 6
        elif (age >= 7 and age < 8):
            evaluation_grade = 'Grade-1'
            g_age = 7
        elif (age >= 8 and age < 9):
            evaluation_grade = 'Grade-2'
            g_age = 8
        elif (age >= 9 and age < 10):
            evaluation_grade = 'Grade-3'
            g_age = 9
        elif (age >= 10 and age < 11):
            evaluation_grade = 'Grade-4'
            g_age = 10
        elif (age >= 11 and age < 12):
            evaluation_grade = 'Grade-5'
            g_age = 11
        elif (age >= 12 and age < 13):
            evaluation_grade = 'Grade-6'
            g_age = 12
        elif (age >= 13):
            evaluation_grade = 'Grade-7'
            g_age = 13
        return evaluation_grade,g_age,is_test_req

if __name__ == "__main__":
    eng = EvaluationEngine("2020-09-01")
    evForm = EvalForm("no","San Ramon","20392","Sankar","","Natarajan","sankar.natarajan@catamilacademy.org",
                      "2013-07-10","9259637862","","2","2","2","")
    evGrade,test_req =  eng.determine_grade(evForm)
    print("Recommended Grade : {}, Test Required : {}".format(evGrade,test_req))