
from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse ,Http404,HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.models import Poll,Choice
def index(request):
	latest_poll_list=Poll.objects.all().order_by('-pub_date')[:5]
	
	context={'latest_poll_list':latest_poll_list}
	
	
	
	return render(request,'polls/index.html',context)

	
def detail(request,pid):
	
	p=Poll.objects.filter(pk=pid)
	print p.question
	
	return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
	
def results(request,pid):

	return HttpResponse('you are looking at the result of %s' %pid)
	
	
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
