import os, sys, json
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from lynx_ui.models import OrchestratorInputModel, OCRInputModel
from lynx_ui.serializers import OrchestratorInputModelSerializer, OCRInputModelSerializer

from django.views.decorators.csrf import csrf_exempt


"""
in django view is considered as 'controller'
"""


@csrf_exempt
def get_data(request):
	data = OrchestratorInputModel.objects.all()
	if request.method == 'GET':
		serializer = OrchestratorInputModelSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)


"""
what is @csrf_exempt?
"""
@csrf_exempt
def create_data(request):
	if request.method == "POST":
		# saving dummy data
		data = {
					"agentCode" : "shin",
					"companyCode" : "01",
					"imageSourceType" : "B"
				}
		print("{} {}".format("*"*10, request))
		serializer = OrchestratorInputModelSerializer(data = data)
		if serializer.is_valid(raise_exception = True):
			data_saved = serializer.save()
		return HttpResponse("success: {} was created".format(data))



"""
OBSOLETE
"""
@csrf_exempt
def ocr_results(request):
	"""
		inject json object into model and show it on screen
	"""
	data = OrchestratorInputModel.objects.all()
	response = readJson()
	#return response
	if request.method == 'GET':
		serializer = OCRInputModelSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
		# return {"hello": "koko"}#response

def readJson():
	path = "lynx_ui/ocrReturnValues.json"
	#path = "lynx_ui/test.json"
	response = []
	with open(os.path.join(sys.path[0], path)) as f:
		s = f.read()
		response.append(s)
	response = json.dumps(response)
	#print(request)
	#print(len(request["response"]))
	return response


