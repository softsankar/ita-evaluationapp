import sqlite3 as sql

from  datetime import  datetime

class EvalDB:

    def __init__(self, db_name):
        self.db_name = db_name

class EvalFormDB(EvalDB):
    def fetch_evaluation_form(self, evaluation_form):
        with sql.connect(self.db_name) as con:
            cur = con.cursor()
            identification = evaluation_form.student_id
            cur.execute("SELECT student_id FROM evaluation_applicant WHERE student_id=identification")
            myresult = cur.fetchall()
            myresult = list(myresult)
            con.commit()

    def add_evaluation_form(self, evaluation_form):
        self.fetch_evaluation_form(evaluation_form)
        if list is None:
            with sql.connect(self.db_name) as con:
                cur = con.cursor()
                ins_sql = "INSERT INTO evaluation_applicant(return_ind, branch, student_id, first_name, middle_name,last_name, \
                       email, birth_date,parent_fname,parent_lname, mobile_no, grade, read_level, write_level, \
                       speak_level, comments)  \
                       values (:return_ind, :branch, :student_id, :first_name, :middle_name,:last_name, :email, \
                      :birth_date, :parent_fname, :parent_lname,:mobile_no, :grade, :rlevel, :wLevel, :sLevel, \
                      :comments) "
                cur.execute(ins_sql,
                        {'return_ind':evaluation_form.return_ind,
                        'branch':evaluation_form.branch,
                        'student_id':evaluation_form.student_id,
                        'first_name':evaluation_form.first_name,
                        'middle_name': evaluation_form.middle_name,
                        'last_name': evaluation_form.last_name,
                        'email':evaluation_form.email,
                        'birth_date': evaluation_form.birth_date,
                        'mobile_no' : evaluation_form.mobile_no,
                        'parent_fname':evaluation_form.parent_fname,
                        'parent_lname':evaluation_form.parent_lname,
                        'grade':evaluation_form.grade,
                        'rlevel':evaluation_form.read_level,
                        'wLevel':evaluation_form.write_level,
                        'sLevel':evaluation_form.speak_level,
                        'comments': evaluation_form.comments
                        })
                con.commit()
                msg = "Record successfully added"
        else :
            raise TypeError("The student already exists")

class EvalResultDB(EvalDB):

    def delete_eval_result(self, student):
        with sql.connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute("DELETE from eval_result WHERE id = :id", {'id': student.id})
            con.commit()
            print('Successfully deleted')


    def add_eval_result(self, eval_result):
        with sql.connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO evaluation_result (student_id, eval_app_date,eval_grade,test_required) VALUES \
                (:student_id, :eval_date, :grade, :test_required)",
                {'student_id': eval_result.student_id,
                 'eval_date': datetime.now(), 'grade':eval_result.eval_grade,
                 'test_required': eval_result.test_required})
            con.commit()
            print('Successfully added')
