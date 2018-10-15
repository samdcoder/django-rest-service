from django.http import JsonResponse

# Create your views here.

def addition(request):
	first = request.GET['first']
	second = request.GET['second']
	first = int(first)
	second = int(second)
	sum = first + second
	return JsonResponse({'result': sum})


def subtraction(request):
	first = request.GET['first']
	second = request.GET['second']
	first = int(first)
	second = int(second)
	diff = first - second
	return JsonResponse({'result': diff})


def multiplication(request):
	first = request.GET['first']
	second = request.GET['second']
	first = int(first)
	second = int(second)
	product = first * second
	return JsonResponse({'result': product})


def division(request):
	first = request.GET['first']
	second = request.GET['second']
	first = int(first)
	second = int(second)
	division = first / second
	return JsonResponse({'result': division})
