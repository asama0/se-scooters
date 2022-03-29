from app import db, bcrypt

new_user = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
new_stripe_id = stripe.Customer.create()['id']
user = User(name=form.name.data, email=form.email.data,
            password=hashedPassword, birth_date=form.birth_date.data,
            phone=form.phone.data, stripe_id=new_stripe_id)

db.session.add(new_user)
db.session.commit()