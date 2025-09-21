from django.db import models


class IncidentImage(models.Model):
    image = models.ImageField(upload_to="incident_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"IncidentImage {self.id}"


class IncidentReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(
        IncidentImage, through="IncidentImages", related_name="incident_reports"
    )

    def __str__(self):
        return self.title


class IncidentImages(models.Model):
    incident_report = models.ForeignKey(IncidentReport, on_delete=models.CASCADE)
    incident_image = models.ForeignKey(IncidentImage, on_delete=models.CASCADE)
    # Add any extra fields if needed, e.g., description or ordering
    # e.g., order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("incident_report", "incident_image")
