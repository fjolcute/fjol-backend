from django.urls import path


from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('about/', about, name = 'about'),
    path('newreq/', NewRequest.as_view(), name ='newrequest'),
    path('newmail/', RequestMessageById.as_view() ,name = 'newmailbyid'),
    path('newmail/<int:request_id>', NewRequestMessage.as_view() ,name = 'newmail'),
    path('reqinfo/', RequestsInfo.as_view(), name= 'requestinfo'),
    path('reqinfo/<int:request_id>', RequestsInfoById.as_view(), name= 'requestinfobyid'),
    path('reqlist/', RequestListView.as_view(), name = 'requestlist'),
    path('personalarea/', personal_area, name = 'personalarea'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('reqinfobyid/', RequestsInfo.as_view(), name='requestinfo'),
    path('reqmessages/', RequestMessages.as_view(), name= 'requestmessages'),
    path('reqmessages/<int:request_id>', RequestMessagesById.as_view(), name='requestmessagesbyid'),



]