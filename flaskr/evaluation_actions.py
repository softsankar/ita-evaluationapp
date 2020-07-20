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
    rec_form = request.form
    eval_rec = rec_form.get('grade')
    recommendation= EvalRecommendation(eval_rec.split())
    eval_res_db = EvalResultDB(database)
    eval_res_db.add_eval_result(recommendation)
    return eval_rec

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
                                form.get('birth_date'),
                                form.get('mobile_number'),
                                form.get('parent_fname'),
                                form.get('parent_lname'),
                                form.get('grade'),
                                rLevel,sLevel,wLevel,
                                form.get('comments'))
    eval_form_db = EvalFormDB(database)
    eval_form_db.add_evaluation_form(evaluation_form)
    cur_date = datetime.now()
    evalEng = EvaluationEngine(str(cur_date.year) + "-09-01")
    grade,test_required = evalEng.determine_grade(evaluation_form)
    print ('Test Required : ',test_required)
    test_req_ind = 'No'
    if test_required is True:
        test_req_ind = 'Yes'
    eval_res = EvalResult(evaluation_form.student_id,
                          evaluation_form.first_name, evaluation_form.last_name,
                          grade, test_req_ind)
    skill_set_db = SkillSet(database)
    skill_set_db.fetch_skill_set(eval_res)
    return eval_res


