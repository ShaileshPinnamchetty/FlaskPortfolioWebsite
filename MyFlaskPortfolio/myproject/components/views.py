from flask import Blueprint,render_template,redirect,url_for,flash, request, send_file
from myproject import db, mail, app
from myproject.models import Message
from myproject.components.forms import AddMessage
from flask_mail import Message as flask_message
import os

components_blueprint = Blueprint('components',
                              __name__,
                              template_folder='templates/components')

@components_blueprint.route('/addMessage', methods=['GET', 'POST'])
def addMessage():

    form = AddMessage()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # Add new message to database
        new_message = Message(name, email, message)
        db.session.add(new_message)
        db.session.commit()
        #Send email for very message received
        msg = flask_message('New message on shaileshatwork.herokuapp.com', sender='shaileshshetty0@gmail.com', recipients=['shailesh.pinnamchetty@gmail.com'])
        # msg.body = """Message from: {}\n\nEmail: {}\n\nMessage: {}""".format(name, email, message)
        msg.html = (f'''<h1>You have received a new message!</h1>
                    <h2>Message from: <b>{name}</b></h2>
                    <h2>Email: <b>{email}</b></h2>
                    <h2>Message: <b>{message}</b></h2>''')
        mail.send(msg)
        flash("Thanks! Your message is received.")
        return redirect(url_for('components.addMessage'))
    return render_template('contact.html',form=form)

@components_blueprint.route('/listAllMessages')
def listMessages():
    messages = Message.query.all()
    return render_template('list.html', messages=messages)

@components_blueprint.route('/deleteAllMessages')
def deleteAllMessages():
    form = AddMessage()
    Message.query.delete()
    db.session.commit()
    return render_template('contact.html', form=form)

@components_blueprint.route('/about_me')
def about_me():
    return render_template('about_me.html')

@components_blueprint.route('/work_history')
def work_history():
    return render_template('work_history.html')

@components_blueprint.route('/work_timeline')
def work_timeline():
    return render_template('work_timeline.html')

@components_blueprint.route('/uploadResume', methods=["GET","POST"])
def uploadResume():
    if request.method == "POST":
        if request.files:
            try:
                os.remove(os.path.join(app.config["UPLOAD_FOLDER"], "Shailesh_Pinnamchetty_Resume.pdf"))
            except FileNotFoundError as e:
                pass
            myfile = request.files["filename"]
            myfile.save(os.path.join(app.config["UPLOAD_FOLDER"], myfile.filename))
            return redirect(url_for('index'))
    return render_template('uploadResume.html')

@components_blueprint.route('/downloadResume')
def downloadResume():
    path = app.config["UPLOAD_FOLDER"]
    resumeFileName = "Shailesh_Pinnamchetty_Resume.pdf"
    return send_file(os.path.join(path, resumeFileName), as_attachment=True, cache_timeout=-1)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    #r.headers['Cache-Control'] = 'public, max-age=0'
    return r