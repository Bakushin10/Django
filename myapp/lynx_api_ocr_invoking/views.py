import os, sys, json
from PIL import Image, ImageDraw2
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from lynx_api_ocr_invoking.models import OCRInputModel, JsonOCRInputModel
from lynx_api_ocr_invoking.serializers import OCRInputModelSerializer, JsonOCRInputModelSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def post_dummy_data(request):
    """
        basic API call for a POST method
        it will post dummy data
        based on the OCRInputModel defined lynx_api_ocr_invoking.models
    """
    if request.method == "POST":
        data = {"ocrJson" : "Two"}
        serializer = OCRInputModelSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            data_saved = serializer.save()
        return HttpResponse("success: {} was created".format(data))

@csrf_exempt
def post_ocr_results(request):
    """
        **** Please dont call this API if data is alrady stored at endpoint ****

        demo API POST call for OCR result.
        read a Json from a local file and post it to endpoint.
    """
    if request.method == "POST":
        response = readJson()
        print("{} {} {}".format("*"*10, "tatal amount of data : ", len(response["response"])))
        print("{} {}".format("*"*10, request))
        
        for json_data in response["response"]:
            # print(json_data)
            x , y = [], []
            for coordinate in json_data["coordinates"]:
                x.append(coordinate["y"])
                y.append(coordinate["x"])
            data = {
                "field" : str(json_data["field"]),
                "hasField" : json_data["hasField"],
                "coordinates" : str(json_data["coordinates"]),
                "x_coordinates" : str(x),
                "y_coordinates" : str(y),
                "text" : json_data["text"]
            }
            serializer = JsonOCRInputModelSerializer(data = data)
            if serializer.is_valid(raise_exception = True):
                data_saved = serializer.save()
        return HttpResponse("{} {} {}".format("All ", len(response["response"]), " data posted!"))        

@csrf_exempt
def get_ocr_results(request):
    """
        retrieve fake OCR data from an endpoint
    """
    data = JsonOCRInputModel.objects.all()
    if request.method == "GET":
        serializer = JsonOCRInputModelSerializer(data, many = True)
        dataToDisplay = getDataToDisplay(serializer.data)
        return JsonResponse(dataToDisplay, safe = False)

@csrf_exempt
def get_ocred_image(request):
    """
        retrieve fake OCR data from an endpoint
    """
    data = JsonOCRInputModel.objects.all()
    SUCCESS_MESSAGE = {"image successfully ocred": "OK"}
    ERROR_MESSAGE = {"image could not be ocred": "ERROR"}

    if request.method == "GET":
        serializer = JsonOCRInputModelSerializer(data, many = True)
        imagePath = "lynx_api_ocr_invoking/img/"
        imageName = "sample_tokyo_marin_written.jpg"
            
        try:
            drawLinesOnImages(imagePath, imageName, serializer.data)
        except:
            return JsonResponse(ERROR_MESSAGE, safe = False)    
        return JsonResponse(SUCCESS_MESSAGE, safe = False)

@csrf_exempt
def get_dummy_data(request):
    """
        basic API call for a GET method 
    """
    data = OCRInputModel.objects.all()
    if request.method == "GET":
        serializer = OCRInputModelSerializer(data, many=True)
        dataToDisplay = getDataToDisplay(serializer.data)
        return JsonResponse(dataToDisplay, safe=False)

def readJson():
    """
        read JSON data from local file 
    """
    
    #path = "lynx_api_ocr_invoking/json/test.json"
    path = "lynx_api_ocr_invoking/json/ocrReturnValues.json"
    #return ""
    
    
    with open(os.path.join(sys.path[0], path)) as f:
        data = json.load(f)
    print("{} {}".format("*"*10, data["response"]))
    return data

def getDataToDisplay(data):
    """
        add "total amount amount of data" for readability purposes 
    """
    return ["total amount data : " + str(len(data))] + data

def drawLinesOnImages(imagePath, imageName, data):
    detectTextOnImage(imagePath, imageName, data)
    # detectTextBoxOnImage(imagePath)

def detectTextOnImage(imagePath,imageName, data):
    """
        draw line to the image based on the x and y coordinates from JSON
    """
    im = Image.open(imagePath + imageName)
    d = ImageDraw2.Draw(im)
    pen = ImageDraw2.Pen(color="red")

    for j in data:
        x = j["x_coordinates"].replace("[","").replace("]","").split(",")
        y = j["y_coordinates"].replace("[","").replace("]","").split(",")
        #LB, LT, RT, RB = (c[0]["x"], c[0]["y"]), (c[1]["x"], c[1]["y"]), (c[2]["x"], c[2]["y"]), (c[3]["x"], c[3]["y"])
        LB, LT, RT, RB = (int(y[0]), int(x[0])), (int(y[1]), int(x[1])), (int(y[2]), int(x[2])), (int(y[3]), int(x[3]))
        d.line([LB, LT, RT, RB, LB], pen) #red line
    im.save(imagePath + "ocred_" + imageName)
    print("image saved")

def detectTextBoxOnImage():
    """
        detect the textbox on a policy
    """
    pass