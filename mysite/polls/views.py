from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.utils import timezone
from .models import Choice, Question

from django.template import loader
from django.shortcuts import render,get_object_or_404

def homepage (request):
    return render(request,'polls/homepage.html')

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['Choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def personal_data (request):
    return render(request, 'polls/p_data.html')


def delete (request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk = request.POST['Choice'])
    selected_choice.delete()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:vote', args=(question.id,)))

def delete_question (request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.objects.get(pk = request.POST['Question'])
    selected_choice.delete()

    return HttpResponseRedirect(reverse('polls:index'))
