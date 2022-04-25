from flask import flash
from flask_admin import BaseView, Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.view import func
from datetime import date
from datetime import datetime

from app import app, db
from helper_functions import flash_errors
from .models import *
from .forms import AdminBookingForm
from .authentication_views import current_user, login, redirect, url_for, request

import analytics_quries


class AdminHomeView(AdminIndexView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        form = AdminBookingForm()
        if form.validate_on_submit():
            new_booking = Booking(
                pickup_date=datetime.combine(
                    form.pickup_date.data, form.pickup_time.data),
                user_id=current_user.id,
                scooter_id=form.scooter_id.data.id,
                price_id=form.time_period.data.id,
            )
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking was saved successfuly.',
                  category='message alert-success')
        else:
            flash_errors(form=form)

        return self.render(
            'admin/index.html',
            form=form,
            date_today=date.today(),
            time_now=datetime.now().strftime("%H:00"))

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.privilege == 22 or current_user.privilege == 333
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('admin is for staff only.', category='message alert-danger')
        return redirect(url_for('authentication_views.login'))


class UserView(ModelView):
    can_delete = False
    column_searchable_list = ['name', 'email', 'phone', 'birth_date']
    column_filters = ['privilege', 'blocked']


class ParkingView(ModelView):
    can_delete = True
    column_filters = ['name']
    column_searchable_list = ['name']


class ScooterView(ModelView):
    can_delete = True
    column_filters = ['parking']


class BookingView(ModelView):
    can_delete = False
    can_edit = False
    can_export = True


class PriorityFeedbackView(ModelView):
    def get_query(self):
        if current_user.privilege == 333:
            return self.session.query(self.model).filter(self.model.urgent == True)
        else:
            return super().get_query()

    def get_count_query(self):
        if current_user.privilege == 333:
            return self.session.query(func.count('*')).filter(self.model.urgent == True)
        else:
            return super().get_count_query()


class PriceView(ModelView):
    can_delete = False

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.privilege == 333
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('Analytics are Admin only.', category='message alert-danger')
        return redirect(url_for('authentication_views.login'))


class Analytics(BaseView):
    @expose('/')
    def index(self):
        analytics_quries.get_analitics(7, "week")
        analytics_quries.get_analitics(30, "month")
        analytics_quries.get_analitics(12, "year")
        analytics_quries.get_data_list_days(1, 1, "total")

        return self.render(
            'analytics_index.html',
            week_analytics=analytics_quries.week,
            month_analytics=analytics_quries.month,
            year_analytics=analytics_quries.year,
            total_analytics=analytics_quries.max_period,
            bobo_hour=analytics_quries.one_h,
            bobo_4=analytics_quries.four_h,
            bobo_day=analytics_quries.one_day,
            bobo_week=analytics_quries.one_week
        )

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.privilege == 333
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('Analytics are Admin only.', category='message alert-danger')
        return redirect(url_for('authentication_views.login'))


# admin pages setup
admin = Admin(app, template_mode='bootstrap4', index_view=AdminHomeView())

# add models to admin page
admin.add_view(UserView(User, db.session))
admin.add_view(ParkingView(Parking, db.session))
admin.add_view(ScooterView(Scooter, db.session))
admin.add_view(ModelView(Booking, db.session))
admin.add_view(PriorityFeedbackView(Feedback, db.session))
admin.add_view(PriceView(Price, db.session))
admin.add_view(Analytics(name='Analytics', endpoint='analytics'))
