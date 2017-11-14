from django.shortcuts import render
import django.http
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice, FrameModel
from django.shortcuts import render, get_object_or_404, render_to_response
#from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#from django.views import View
#from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions. (not including those set to be
        published in the future)
        """
        return Question.objects.filter(
        pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

""" def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
"""

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


""" def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
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


class PictureView(TemplateView):
    template_name = 'polls/pictureSlideshow.html'


def frameFromModel(request):
    img = FrameModel.objects.all() #.order_by('-id')
    args = {'imageToShow':img}
    return render(request,'polls/frameFromModel.html',args)



