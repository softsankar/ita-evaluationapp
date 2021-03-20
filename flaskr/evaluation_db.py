import sqlite3 as sql
import app

from datetime import datetime
from evaluation_models import Skill


class EvalDB:

    def __init__(self, db_name):
        self.db_name = db_name


class EvalFormDB(EvalDB):
    ##def fetch_evaluation_form(self,evaluation_form):
    ##with sql.connect(self.db_name) as con:
    ##cur = con.cursor()
    ##cur.execute("SELECT * FROM evaluation_applicant WHERE student_id= :id",{'id':evaluation_form.student_id})
    ##result= cur.fetchall()
    ##if result >0 then "Already exist"
    ##else

    def add_evaluation_form(self, evaluation_form):
        ##myresult= self.fetch_evaluation_form(evaluation_form)
        try:
            ##if myresult is None:
            with sql.connect(self.db_name) as con:
                cur = con.cursor()
                ins_sql = 'INSERT INTO Evaluation_Applicant(return_ind, branch, student_id, first_name, middle_name,last_name, \
                           email, birth_date,parent_fname,parent_lname, mobile_no, grade, read_level, write_level, \
                           speak_level, comments)  \
                           values (:return_ind, :branch, :student_id, :first_name, :middle_name,:last_name, :email, \
                          :birth_date, :parent_fname, :parent_lname,:mobile_no, :grade, :rlevel, :wLevel, :sLevel, \
                          :comments) '
                cur.execute(ins_sql,
                            {'return_ind': evaluation_form.return_ind,
                             'branch': evaluation_form.branch,
                             'student_id': evaluation_form.student_id,
                             'first_name': evaluation_form.first_name,
                             'middle_name': evaluation_form.middle_name,
                             'last_name': evaluation_form.last_name,
                             'email': evaluation_form.email,
                             'birth_date': evaluation_form.birth_date,
                             'mobile_no': evaluation_form.mobile_no,
                             'parent_fname': evaluation_form.parent_fname,
                             'parent_lname': evaluation_form.parent_lname,
                             'grade': evaluation_form.grade,
                             'rlevel': evaluation_form.read_level,
                             'wLevel': evaluation_form.write_level,
                             'sLevel': evaluation_form.speak_level,
                             'comments': evaluation_form.comments
                             })
            con.commit()
            return 'Success'
        except sql.IntegrityError:
            return 'already exist'


class EvalResultDB(EvalDB):

    def delete_eval_result(self, student):
        with sql.connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute("DELETE from eval_result WHERE id = :id", {'id': student.id})
            con.commit()
            app.logger.info('Successfully deleted')

    def add_eval_result(self, eval_result):
        with sql.connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO evaluation_result (student_id, eval_app_date,eval_grade,test_required) VALUES \
                (:student_id, :eval_date, :grade, :test_required)",
                        {'student_id': eval_result.student_id,
                         'eval_date': datetime.now(), 'grade': eval_result.eval_grade,
                         'test_required': eval_result.test_required})
            con.commit()
            app.logger.info('Successfully added')


class SkillSet(EvalDB):

    def fetch_skill_set(self, grade):
        skillset=[]
        with sql.connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute("SELECT grade_level, Age, Skills, Grammar, Reading, Writing, Oral, Project FROM skill_set WHERE grade_level = :grade", {'grade':grade})
            skill_res= cur.fetchall()
            for row in skill_res:
                s = Skill(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                skillset.append(s)
                app.logger.debug("Grade Level : %s, Age: %d, Skills : %s",s.grade_level,s.age,s.skills)
            app.logger.info('Successfully received')
        return skillset

    def fetch_skillset_by_age(self, age,is_test_req,cur_reg_gradeno):
        skillset=[]
        with sql.connect(self.db_name) as con:
            cur = con.cursor()
            qry = ("SELECT grade_level, Age, Skills, Grammar, Reading, Writing, Oral, Project " +
                   "FROM skill_set WHERE age <= :age and testreq_ind = :isTestReq ")
            p_dict = {'age':age, 'isTestReq':str(is_test_req).lower()}
            if int(cur_reg_gradeno) >= 1:
                qry = qry + " and grade_no > :gradeno"
                p_dict.update({'gradeno':cur_reg_gradeno}) 
            app.logger.debug("Query : %s, Values : %s",qry,p_dict)    
            cur.execute(qry,p_dict )
            skill_res= cur.fetchall()
            for row in skill_res:
                s = Skill(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                skillset.append(s)
                app.logger.debug("Grade Level : %s, Age: %d, Skills : %s",s.grade_level,s.age,s.skills)
            app.logger.info('Successfully received')
        return skillset    
