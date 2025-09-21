from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import IncidentReport, IncidentImage, IncidentImages
from .forms import FileFieldForm


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = "incidents/upload.html"  # Your template
    success_url = reverse_lazy("upload_success")

    def form_valid(self, form):
        files = form.cleaned_data[
            "file_field"
        ]  # Assuming this is a list of uploaded files
        # Example: get or create an IncidentReport; adjust as needed
        incident_report = IncidentReport.objects.create(
            title="New Incident",  # Or get from form.cleaned_data if available
            description="Description of incident",  # Or get from form.cleaned_data
        )

        for f in files:
            # Save each file as an IncidentImage
            incident_image = IncidentImage.objects.create(image=f)
            # Link the image to the incident report via IncidentImages
            IncidentImages.objects.create(
                incident_report=incident_report, incident_image=incident_image
            )
        return super().form_valid(form)
