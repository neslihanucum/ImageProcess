from django.urls import path
from ImagePro.views import upload_photo, photo_list, colorspace, morphology, edge, blur, imgflip, togrey, torgb, \
    rgbtobgf, erod, dilafe, morfopen, morfclose, morfgradiant, innerblur, gausianblur, medianblur, bileteralfilter, \
    yuzseksen, artidoksan, eksidoksan

app_name = 'imagepro'

urlpatterns = [
    path('', upload_photo, name="upload_photo"),
    path('/photo_list/', photo_list, name="photos"),
    path('/colorspace/', colorspace, name='colorspace' ),
    path('/morphology/', morphology, name='morphology' ),
    path('/edge/', edge, name='edge' ),
    path('/blur/', blur, name='blur' ),
    path('/imgflip/', imgflip, name='imgflip' ),
    path('/togrey/', togrey, name='togrey' ),
    path('/torgb/', torgb, name='torgb' ),
    path('/rgbtobgf/', rgbtobgf, name='rgbtobgf' ),
    path('/erod/', erod, name='erod' ),
    path('/dilafe/', dilafe, name='dilafe' ),
    path('/morfopen/', morfopen, name='morfopen' ),
    path('/morfclose/', morfclose, name='morfclose' ),
    path('/morfgradiant/', morfgradiant, name='morfgradiant' ),
    path('/innerblur/', innerblur, name='innerblur' ),
    path('/gausianblur/', gausianblur, name='gausianblur' ),
    path('/medianblur/', medianblur, name='medianblur' ),
    path('/bileteralfilter/', bileteralfilter, name='bileteralfilter' ),
    path('/yuzseksen/', yuzseksen, name='yuzseksen'),
    path('/artidoksan/', artidoksan, name='artidoksan'),
    path('/eksidoksan/', eksidoksan, name='eksidoksan'),

]