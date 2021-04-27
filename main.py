from flask import Flask, render_template, redirect, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from connection import Connection

app = Flask(__name__)
URL_FOLDER = os.path.abspath('./static/img')
app.config["UPLOAD_FOLDER"] = URL_FOLDER
extensiones_permi = set(['png', 'jpg'])


def verif_extens(filename):
    return "." in filename and filename.rsplit('.', 1)[1] in extensiones_permi


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/blogs")
def blogs():
    connection = Connection.get_connection()
    cursor = Connection.get_cursor()
    query = "SELECT id_blog, title_blog, text_blog, description_blog FROM blog"
    cursor.execute(query)
    data_blogs = cursor.fetchall()
    Connection.close()
    return render_template('blogs.html', dtblogs=data_blogs)


@app.route("/blog/<int:_id>")
def blog(_id):
    connection = Connection.get_connection()
    cursor = Connection.get_cursor()
    query = "SELECT title_blog, text_blog, description_blog, img_blog FROM blog WHERE id_blog=?"
    cursor.execute(query, (_id,))
    data_blog = cursor.fetchone()
    Connection.close()
    list_dt_blog = list(data_blog)
    list_dt_blog[3] = f"img/{data_blog[3]}"
    # img = send_from_directory(app.config["UPLOAD_FOLDER"], data_blog[3])
    return render_template('blog.html', dtblog=tuple(list_dt_blog))


@app.route("/new_blog", methods=['GET', 'POST'])
def new_blog():
    if request.method == "POST":
        connection = Connection.get_connection()
        cursor = Connection.get_cursor()
        query = "INSERT INTO blog(title_blog, text_blog, description_blog, img_blog) VALUES(?,?,?,?)"
        file_img = request.files['img']
        imgname = secure_filename(file_img.filename)
        if imgname == "":
            return render_template('new_blog.html')
        data = (request.form['title'], request.form['paragram'], request.form['descrip'], imgname)
        cursor.execute(query, data)
        connection.commit()
        file_img.save(os.path.join(app.config["UPLOAD_FOLDER"], imgname))
        Connection.close()
    return render_template('new_blog.html')


@app.route("/remove_blog", methods=['GET', 'POST'])
def del_blog():
    if request.method == "POST":
        connection = Connection.get_connection()
        cursor = Connection.get_cursor()
        query = "DELETE FROM blog WHERE title_blog=?"
        data = (request.form['title'],)
        cursor.execute(query, data)
        connection.commit()
        Connection.close()
    return render_template('remove_blog.html')


@app.route("/update_blog", methods=['GET', 'POST'])
def update_blog():
    if request.method == "POST":
        connection = Connection.get_connection()
        cursor = Connection.get_cursor()
        query = "UPDATE blog SET title_blog=?, text_Blog=?, description_blog=?, img_blog=? WHERE id_blog=?"
        file_img = request.files['img']
        imgname = secure_filename(file_img.filename)
        if imgname == "":
            return render_template('update.html')
        data = (request.form['n_title'], request.form['paragram'], request.form['descrip'],
                imgname, request.form['id_blog'])
        cursor.execute(query, data)
        connection.commit()
        Connection.close()
        file_img.save(os.path.join(app.config["UPLOAD_FOLDER"], imgname))
    return render_template('update.html')


def main():
    app.run(debug=True, port=3000)


if __name__ == '__main__':
    main()
