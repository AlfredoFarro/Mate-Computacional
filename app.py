import functions as F
import os
from flask import Flask, flash, request, redirect, url_for
import flask
from werkzeug.utils import secure_filename, send_file

UPLOAD_FOLDER = '.cache/'


# Create the application.
APP = Flask(__name__)
APP.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')



@APP.route('/handle_encrypt', methods=['POST'])
def handle_encrypt():
    p_value = int(flask.request.form['p_value'])
    q_value = int(flask.request.form['q_value'])
    d_value = flask.request.form['d_value']
    text_value = flask.request.form['text_value']
    

    if not F.isPrime(p_value) or not F.isPrime(q_value) or p_value*q_value < 26:
        #print("WRONG")
        return flask.render_template('index.html')

    eul = F.euler(p_value,q_value)
    pv = F.selectd(eul)
    
    if d_value == '':
        d_value = F.choice(pv)


    n = p_value * q_value
    e = F.finde(d_value, eul)

    key_public = [n, e]
    key_private = [n, d_value]

    #print(f"Public: {key_public}")
    #print(f"Private: {key_private}")

    arr_word1=[x for x in F.process(text_value, key_public).split()]##08 02 01 46 arrqord[08,02,01,46]
    out_text = ' '.join(arr_word1)
    #print(f"Encriptado: {out_text}")


    f = open('.cache/latest_file_out.txt', 'w')
    f.write(out_text)
    f.close()
    fn = f"Key_{key_private[0]}_{key_private[1]}.txt"
    return flask.send_from_directory(APP.config['UPLOAD_FOLDER'], 'latest_file_out.txt', 
                                     as_attachment=True, download_name = fn)


def read_and_decrypt(c1, c2):
    msg = [int(x) for x in open('.cache/latest_file_in.txt', 'r').read().split()]
    return f"Desencriptado: {F.process1(msg, [c1,c2])}"



@APP.route('/handle_decrypt', methods=['GET', 'POST'])
def handle_decrypt():
    if request.method == 'POST':
        # check if the post request has the file part
        #print(f"FILES: '{request.files}'")
        if 'filename' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['filename']
        
        
        #print('GAAAAAAAAAAAAAAAAAAAAA')
        #print(flask.request.form)
        c1 = flask.request.form['C1']
        c2 = flask.request.form['C2']
        #print(c1)
        if c1 != '' and c2 != '':
            c1 = int(c1)
            c2 = int(c2)
        else:
            return flask.render_template('index.html')

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(APP.config['UPLOAD_FOLDER'], 'latest_file_in.txt'))
            return f'<h2>{read_and_decrypt(c1, c2)}</h2>'
            

            
    return flask.render_template('index.html')



if __name__ == '__main__':
    APP.debug=True
    APP.run()
