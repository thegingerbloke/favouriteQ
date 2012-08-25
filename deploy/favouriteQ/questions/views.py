from django.shortcuts import render_to_response
from questions.models import Question, Answer

def current_question(request):

    # get the question with the most recent asked date (null asked date means question hasn't been asked)
    question = Question.objects.order_by('-asked_date').filter(asked_date__isnull=False)[0]
    answers = Answer.objects.filter(question_id=question.id)

    for answer in answers:
        print answer.answer_text
        print answer.person

    return render_to_response('questions/current_question.html', {"question": question, "answers":answers})
    # {"results": results, "query": query}, context_instance=RequestContext(request)