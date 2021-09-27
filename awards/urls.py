from django.urls import path
from . import views

app_name = "awards"
urlpatterns = [
    path('', views.adwardList, name="list"),
    path('<str:award_code>/update', views.updateAwardee, name="update"),
    path('<str:award_code>/save-pdf', views.render_pdf_view, name="save_pdf"),
    path('<str:award_code>/delete', views.deleteAward, name="delete"),
    path('export-pdf', views.export_pdf_by_date, name="export_pdf_by_date")
]
