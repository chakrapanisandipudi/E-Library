
from django.urls import path

from . import views

urlpatterns = [
    # path("register", views.register, name="register"),
    path("logout",views.logout,name="logout"),
    path("about_us",views.about_us,name="about_us"),
    path("contact_us",views.contact_us,name="contact_us"),
    path("show_login",views.show_login,name="show_login"),
    path("register",views.register,name="register"),
    path("error404",views.error404, name="error404"),
    path("coming_soon",views.coming_soon, name="coming_soon"),
    path("maintenance",views.maintenance, name="maintenance"),

    #---- admin templates ---#
    path("admin_dashboard",views.admin_dashboard,name="admin_dashboard"),
    path("admin_login",views.admin_login,name="admin_login"),
    path("add_book",views.add_book,name="add_book"),
    path("book_list",views.book_list,name="book_list"),
    path("issue_book",views.issue_book,name="issue_book"),
    path("student_list",views.student_list,name="student_list"),
    path("view_issued_book", views.view_issued_book, name="view_issued_book"),
    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path('edit/<int:pk>/', views.book_update, name='book_edit'),
    path("view_book/<int:myid>/", views.view_book, name="view_book"),
    path("view_student/<int:myid>/", views.view_student, name="view_student"),
    path("delete_student/<int:myid>/", views.delete_student, name="delete_student"),
    path("admin_accepted_books", views.admin_accepted_books, name="admin_accepted_books"),
    path("admin_recieved_books", views.admin_recieved_books, name="admin_recieved_books"),
    path("admin_requested_books", views.admin_requested_books, name="admin_requested_books"),
    # path("edit_book_save", views.edit_book_save, name="edit_book_save"),
    # path('edit/<int:id>',views.edit,name="edit"),
    # path('update/<int:pk>',views.update,name="update"),

    #---- Student templates ---#
    path("student_dashboard",views.student_dashboard,name="student_dashboard"),
    path("student_register", views.student_register, name="student_register"),
    path("student_login",views.student_login,name="student_login"),
    path("student_profile",views.student_profile,name="student_profile"),
    path("student_edit_profile",views.student_edit_profile,name="student_edit_profile"),
    path("student_issued_books", views.student_issued_books, name="student_issued_books"),
    path("student_borrow_books", views.student_borrow_books, name="student_borrow_books"),
    path("student_requested_books", views.student_requested_books, name="student_requested_books"),
    path("student_received_books", views.student_received_books, name="student_received_books"),
    path("student_rejected_books", views.student_rejected_books, name="student_rejected_books"),
    path("student_change_password", views.student_change_password, name="student_change_password"),
]
