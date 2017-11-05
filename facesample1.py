import cognitive_face as CF

KEY = 'bfe8026c584940aabc8a1a20c8ccd792'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'http://www.sriramachandra.edu.in/medical/oldmanager/images/doctors/pushpa-final.jpg'
result = CF.face.detect(img_url)
faceId1 = result[0]['faceId']

img_url = 'https://serving.photos.photobox.com/202914783673aa39228014902b6905eec5499927e3dd836c59645a8db0d77e560e407867.jpg'
result = CF.face.detect(img_url)
faceId2 = result[0]['faceId']

result = CF.face.verify(faceId1,faceId2)

print (result)


