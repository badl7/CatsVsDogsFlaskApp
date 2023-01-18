# sourcery skip: use-fstring-for-concatenation
from flask import Flask, render_template, request, send_from_directory
import os
from keras.models import load_model
from keras.preprocessing import image 
import numpy as np 
import tensorflow as tf 


app = Flask(__name__)


STATIC_FOLDER = 'static'
# Path to the folder where we'll store the upload before prediction
UPLOAD_FOLDER = f'{STATIC_FOLDER}/uploads'
# Path to the folder where we store the different models
MODEL_FOLDER = f'{STATIC_FOLDER}/models'


model = load_model(f'{MODEL_FOLDER}/cat_dog_inceptionV3.h5')
print('[INFO] : Model loaded')

def predict(full_path):
    data = tf.io.read_file(full_path)
    data = tf.image.decode_jpeg(data, channels=3)
    # (224, 224, 3) > (150, 150, 3) - used a self trained model, not the inceptionV3
    data = tf.image.resize(data, [150, 150])
    data = np.expand_dims(data, axis=0) #Expand the shape of a data
    # rescaling
    data = data.astype('float') / 255.0

    # prediction
    result = model.predict(data)
    
    return result



# Home Page
@app.route('/')
def index():
    return render_template('index.html')


# Process upload file and predict  
@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')

    file = request.files['image']
    full_name = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(full_name)

    result = predict(full_name)
    """
    label = "Dog" if result[0][0] >=0.5 else "Cat"
    acc = round((result[0][0])*100, 2) if result[0][0] >= 0.5 else 1 - result[0][0]
    """
    prob_pred = result.item()
    if prob_pred > .5:
        label = 'Dog'
        acc = round(prob_pred * 100, 2)
    else:
        label ='Cat'
        acc = round((1 - prob_pred) * 100, 2)
    print(result)
    
    return render_template('predict.html', image_file_name=file.filename, label=label, acc=acc)


@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)




if __name__ == "__main__":
    #app = create_app()
    app.run(debug=True)