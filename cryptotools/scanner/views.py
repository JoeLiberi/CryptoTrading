from django.shortcuts import render
from .forms import ScanForm
from django.http import HttpResponseRedirect
# Create your views here.


# Create your views here.
def scanner(request):
	form = ScanForm()

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ScanForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/')

		# if a GET (or any other method) we'll create a blank form
		else:
			form = ScanForm()

	context = {
		'stuff' : 'this is some stuff!!!',
		'form' : form
	}

	return render(request, 'scanner.html', context)