def classify10(path):
    import requests
    #classify the audio
    classify_url='http://max-audio-classifier.max.us-south.containers.appdomain.cloud/model/predict?start_time=0'
    localclassify_url='http://localhost:5000/model/predict'
    with open(path,'rb') as filedata:
        r = requests.post(localclassify_url, files={'audio': filedata})
        #print(r.text)
    predictions = r.json()['predictions']
    #print(predictions)
    category={}
    for label in predictions:
        category['%s'%label['label']]= label['probability']
    return category