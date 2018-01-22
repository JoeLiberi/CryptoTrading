from django.shortcuts import render

# Create your views here.


# Create your views here.
def scanner(request):

	context = {
		'stuff' : 'this is some stuff!!!'
	}

	return render(request, 'scanner.html', context)