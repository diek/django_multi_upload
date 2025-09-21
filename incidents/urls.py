from django.urls import path
from django.views.generic import TemplateView
from .views import FileFieldFormView

urlpatterns = [
    path("upload/", FileFieldFormView.as_view(), name="file_upload"),
    path(
        "upload/success/",
        TemplateView.as_view(template_name="incidents/upload_success.html"),
        name="upload_success",
    ),
]
