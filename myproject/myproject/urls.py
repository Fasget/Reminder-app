from django.urls import path, include

from accounts import views as vw
from myapp import views

urlpatterns = [
    path('', vw.login_view, name='login'),
    path('reminder/', views.category_list, name='category_list'),
    path('reminder/category/<int:category>/', views.reminder_list, name='reminder_list'),
    path('reminder/category/<int:category>/<int:pk>/', views.reminder_detail, name='reminder_detail'),
    path('reminder/category/new/', views.category_new, name='category_new'),
    path('reminder/category/<int:category>/edit/', views.category_edit, name='category_edit'),
    path('reminder/category/<int:category>/new/', views.reminder_new, name='reminder_new'),
    path('reminder/category/<int:category>/<int:pk>/edit/', views.reminder_edit, name='reminder_edit'),
    path('reminder/category/<int:category>/<int:pk>/delete/', views.reminder_delete, name='reminder_delete'),
    path('reminder/category/<int:category>/delete/', views.category_delete, name='category_delete'),
    path('reminder/delete/all/', views.reminder_delete_all, name='reminder_delete_all'),
    path('reminder/categories/delete_all/', views.category_delete_all, name='category_delete_all'),
    path('reminder/category/', views.completed_all_reminders, name='completed_all_reminders'),
    path('reminder/category/', views.uncompleted_all_reminders, name='uncompleted_all_reminders'),
    path('accounts/', include('accounts.urls')),
    path('account/', views.personal_account, name='personal_account'),


]

