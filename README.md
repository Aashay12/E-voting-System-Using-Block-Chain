# E-voting-System Using-Block-Chain
This application allows you to create a online secured polling booth (which can be used by government or  any company) for conducting elections for specific positions.

# Backend

(train_model.py)

- This code trains a face recognition model using Support Vector Machines (SVM) algorithm. 
It takes pre-computed facial embeddings as input and trains the SVM model to recognize and classify faces based on these embeddings. The trained model and the label encoder used for encoding class labels are then saved to disk for later use in face recognition applications.

(savefaces.py)

- This code captures images from a webcam to create a dataset for face recognition. It uses the OpenCV library to detect faces in the webcam frames, crops and resizes the detected faces, and saves them as individual images in the specified dataset folder. The process continues until it captures 30 face images, and it displays the webcam feed with rectangles around the detected faces in real-time.

(recognize.py)
- This code performs face recognition on an input image using OpenCV's deep learning-based face detector, face embedding model, and a trained face recognition model. It detects faces in the image, extracts facial embeddings, and then classifies each face using the trained model. The recognized faces are then displayed on the image with bounding boxes and labels.

(register.py)
- This code is a PyQt5 application that allows users to register as voters. It captures user information such as name, email, contact, date of birth, Aadhar number, and address. It saves the information to a SQLite database and creates a directory with a random number as the name to store facial images captured using a webcam. The code utilizes OpenCV's face detection to capture and save multiple images of the user's face.

