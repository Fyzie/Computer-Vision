# Computer-Vision

<details open>
<summary>face_detection</summary>
<br>
  
line 12: detectMultiScale(gray, scaleFactor, minNeighbors)  
  
The parameters are:
1. The gray scale variable — gray in our case
2. scaleFactor — Parameter specifying how much the image size is reduced at each image scale. Basically, the scale factor is used to create your scale pyramid. More explanation, your model has a fixed size defined during training, which is visible in the XML. This means that this size of the face is detected in the image if present. However, by rescaling the input image, you can resize a larger face to a smaller one, making it detectable by the algorithm. 1.05 is a good possible value for this, which means you use a small step for resizing, i.e. reduce the size by 5%, you increase the chance of a matching size with the model for detection is found. This also means that the algorithm works slower since it is more thorough. You may increase it to as much as 1.4 for faster detection, with the risk of missing some faces altogether. In our case, I have used 1.0485258 as the scaleFactor as this worked perfectly for the image that I was using.
3. minNeighbors — Parameter specifying how many neighbors each candidate rectangle should have to retain it. This parameter will affect the quality of the detected faces. Higher value results in fewer detections but with higher quality. 3~6 is a good value for it. In our case, I have taken 6 as the minNeighbors and this has worked perfectly for the image that I have used.  
  
*can be tested with different pictures with more/ lesser faces

credit: https://towardsdatascience.com/computer-vision-detecting-objects-using-haar-cascade-classifier-4585472829a9
  
</details>

<details open>
<summary>eye_detection</summary>
<br>
  
The appropriate configurations for line 14 (depend on the objects' features(eye)):
  
  two_people.jpg--> eye_cascade.detectMultiScale(gray, 1.1, 5)  
  group_people--> eye_cascade.detectMultiScale(gray, 1.05, 7)
  
</details>
