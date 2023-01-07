from django.urls import path
from TransferRequest import views

urlpatterns = [
    path('transfer_req', views.TransferReq.as_view(), name='transfer_req'),
]


