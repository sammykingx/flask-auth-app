from flask import render_template


def not_found_error(e):
    return render_template("errors/404.html"), 404


def internal_server_error(e):
    return render_template("errors/500.html"), 500
