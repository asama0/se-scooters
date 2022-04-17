from flask import flash
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.view import func

from app import app, db
from .models import *
from .forms import BookingForm
from .authentication_views import current_user, login, redirect, url_for, request

from flask_admin import BaseView, expose


class AdminHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        form = BookingForm()
        if form.validate_on_submit():
            pass

        return self.render('admin/index.html', form=form)

    # def is_accessible(self):
    #     if current_user.is_authenticated:
    #         return current_user.privilege == 22 or current_user.privilege == 333
    #     return False

    # def inaccessible_callback(self, name, **kwargs):
    #     # redirect to login page if user doesn't have access
    #     flash('/admin is staff only.', category='message alert-danger')
    #     return redirect(url_for('login'))


class Analytics(BaseView):
    @expose('/')
    def index(self):
        return self.render('analytics_index.html')


class UserView(ModelView):
    can_delete = False
    column_searchable_list = ['name', 'email', 'phone', 'birth_date']
    column_editable_list = ['name', 'email', 'phone', 'birth_date']
    column_filters = ['privilege', 'blocked']


class ScooterView(ModelView):
    can_delete = False
    column_filters = ['parking']


class ParkingView(ModelView):
    can_delete = False
    column_filters = ['name']
    column_searchable_list = ['name']


class PriorityFeedbackView(ModelView):
    def get_query(self):
        return self.session.query(self.model).filter(self.model.urgent == True)

    def get_count_query(self):
        return self.session.query(func.count('*')).filter(self.model.urgent == True)


# admin pages setup
admin = Admin(app, template_mode='bootstrap4', index_view=AdminHomeView())

# add models to admin page
admin.add_view(UserView(User, db.session))
admin.add_view(ScooterView(Scooter, db.session))
admin.add_view(ParkingView(Parking, db.session))
admin.add_view(ModelView(Booking, db.session))
# admin.add_view(ModelView(Feedback, db.session,name="feedback"))
admin.add_view(PriorityFeedbackView(Feedback, db.session))
admin.add_view(Analytics(name='Analytics', endpoint='analytics'))
