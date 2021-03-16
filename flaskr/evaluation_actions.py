import app

from evaluation_models import EvalForm
from evaluation_db import EvalFormDB
from evaluation_db import EvalResultDB
from evaluation_models import EvalResult
from evaluation_engine import EvaluationEngine
from datetime import datetime
from evaluation_db import SkillSet
from evaluation_models import EvalRecommendation
from evaluation_models import Skill


def submit_eval_rec(request, database):
    g_det = request.form.get('select_grade')
    app.logger.debug("Grade Detail : %s",g_det)
    det = g_det.split("_")
    evalDb = EvalResultDB(database)
    evRec = EvalRecommendation(det[0],det[1],det[2],det[3],[])
    evRes = EvalResult(evRec.student_id,evRec.first_name, evRec.last_name,evRec.grade,"yes")
    evalDb.add_eval_result(evRes)
    app.logger.debug("Grade Detail : %s",g_det)
    return evRec

def submit_eval_form(request,database):
    form = request.form
    return_ind = "no"
    if form.get('new_student') and form.get('new_student').strip():
        return_ind = "yes"
    rLevel = 1
    if form.get('rLevel_2'):
        rLevel = form.get('rLevel_2')
    elif form.get('rLevel_3'):
        rLevel = form.get('rLevel_3')
    wLevel = 1
    if form.get('wLevel_2'):
        wLevel = form.get('wLevel_2')
    elif form.get('wLevel_3'):
        rLevel = form.get('wLevel_3')
    sLevel = 1
    if form.get('sLevel_2'):
        sLevel = form.get('sLevel_2')
    elif form.get('sLevel_3'):
        sLevel = form.get('sLevel_3')
    evaluation_form = EvalForm(return_ind,
                                form.get('branch'),
                                form.get('student_id'),
                                form.get('first_name'),
                                form.get('middle_name'),
                                form.get('last_name'),
                                form.get('email'),
                                form.get('date'),
                                form.get('mobile_number'),
                                form.get('parent_fname'),
                                form.get('parent_lname'),
                                form.get('grade'),
                                rLevel,sLevel,wLevel,
                                form.get('comments'))
    logger = app.logger                           
    logger.debug("Birth Date : %s",form.get("date"))                            
    eval_form_db = EvalFormDB(database)
    eval_form_db.add_evaluation_form(evaluation_form)
    cur_date = datetime.now()
    evalEng = EvaluationEngine(str(cur_date.year) + "-09-01")
    grade,g_age,test_required = evalEng.determine_grade(evaluation_form)
    logger.debug("Grade : %s Age: %d ",grade,g_age)
    skills = []
    if test_required is True:
        test_req_ind = 'Yes'
        cur_reg_gradeno=0
        if form.get('grade'):
            cur_reg_gradeno = form.get('grade')[:6]    
        skill_set_db = SkillSet(database)
        skills = skill_set_db.fetch_skillset_by_age(g_age,test_required,cur_reg_gradeno)
    evRec = EvalRecommendation(form.get('student_id'),
                form.get('first_name'),form.get('last_name'),
                grade,skills)
    return evRec


