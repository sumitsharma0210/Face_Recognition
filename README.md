### Face Recognition & Verification System

A deep learning-based face recognition and verification system built using Python, TensorFlow/Keras, OpenCV, and Siamese Neural Networks. The model uses a CNN-based embedding network to learn facial features and compares image embeddings to determine whether two faces belong to the same person.

The project includes anchor, positive, and negative image pairs for training the Siamese network. Images are preprocessed, resized, normalized, and passed through a CNN to generate feature embeddings. An L1 distance layer is used to measure the similarity between face embeddings, followed by a classification layer for verification.

Key Features
Siamese Neural Network for face verification
CNN-based facial feature extraction
Face embeddings for similarity comparison
Anchor, positive, and negative image pairs
Image preprocessing using TensorFlow and OpenCV
Real-time face verification using webcam
Similarity-based prediction with a configurable threshold
Model training, evaluation, saving, and loading
Tech Stack

Python | TensorFlow | Keras | OpenCV | NumPy 

Workflow

Face Image → Preprocessing → CNN Feature Extraction → Face Embedding → L1 Distance → Similarity Score → Same Person / Different Person

This project demonstrates practical implementation of Deep Learning, Computer Vision, CNNs, Siamese Networks, image preprocessing, feature embeddings, and face verification.
