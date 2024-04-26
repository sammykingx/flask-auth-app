from flask import redirect, render_template, request, url_for
from app.extensions import bcrypt
from app.models.users import db, Users
from app.models import db_crud
from . import auth_bp


@auth_bp.route("/admin_register", methods=["GET", "POST"])
def admin_registration():
    """admin registration endpoint"""

    if request.method == "POST":
        user_data = dict(request.form)
        if not user_data:
            return render_template("admin_signup.html")

        existing_user = db_crud.return_single_record(
            Users, email=user_data.get("email", None)
        )

        if existing_user:
            return redirect(url_for("auth.user_checkpoint"))

        user_data["password"] = bcrypt.generate_password_hash(user_data["password"])
        user_data.update(role="admin", is_verified=False)
        new_user = Users(**user_data)
        
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user)

        login_user(new_user)
        return redirect(url_for("admin.render_dashboard"))

    return render_template("admin_signup.html")
