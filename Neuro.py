from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from PIL import Image
from tkinter import *
import time
root = Tk()
root.title("Нейронная сеть распознование автомобиля")
def clicked():
    a = '%s (%.2f%%)' % (label[1], label[2]*100)
    lbls = Label(root, text = a , font=("Arial Bold", 20), bg = 'Beige')  
    lbls.place(x=570, y=450)     
def clicked_image():
    a = txt.get()
    print(a)
    # load the model
    model = VGG16()
    # load an image from file
    image = load_img(a, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    global label
    label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    label = label[0][0]
    # print the classification 
    print('%s (%.2f%%)' % (label[1], label[2]*100))   
def clicked_P():
    a = txt.get()
    s = "'" + a + "'"
    img = Image.open(s,"r")
    img.show()
c = Canvas(root, width = 1200, height = 500, bg = 'Beige')
c.pack()
lbl = Label(root, text="Вставьте фото в окно", font=("Arial Bold", 20), bg = 'Beige')
lbl.place(x=0, y=0) 
txt = Entry(root,width=35)  
txt.place(x=0, y=50) 
btn = Button(root, text="НАЖАТЬ", command=clicked_image)  
btn.place(x=230, y=50) 
lbl = Label(root, text="Для рассчета объекта нажмите на кнопку", font=("Arial Bold", 20), bg="Beige")
lbl.place(x=0, y=450)
btn = Button(root, text="НАЖАТЬ", command=clicked)  
btn.place(x=800, y=450) 
btn = Button(root, text="ФОТО", command=clicked_P)  
btn.place(x=230, y=75) 
root.mainloop()
