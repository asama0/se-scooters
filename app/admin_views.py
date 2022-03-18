from flask import flash
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView

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

# admin pages setup
admin = Admin(app, template_mode='bootstrap4', index_view=AdminHomeView())

# add models to admin page
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Scooter, db.session))
admin.add_view(ModelView(Parking, db.session))
# admin.add_view(ModelView(Cost, db.session))
admin.add_view(Analytics(name='Analytics', endpoint='analytics'))
