from django.urls import path
from . import views

app_name = "awards"
urlpatterns = [
    path('', views.adwardList, name="list"),
    path('<int:pk>', views.awardFilter, name="filter"),
    path('<str:award_code>/update', views.updateAwardee, name="update"),
    path('<str:award_code>/save-pdf', views.render_pdf_view, name="view_pdf"),
    path('<str:award_code>/export-pdf', views.render_pdf, name="export_pdf"),
    path('<str:award_code>/delete', views.deleteAward, name="delete"),
]
