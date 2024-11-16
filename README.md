__Image Processing:__

Image processing is a technique used to enhance, analyze, and manipulate digital images, typically through algorithms and computer vision tools. It involves a series of operations that transform an image to improve its quality, extract useful information, or prepare it for further analysis. Image processing has a wide array of applications, including photography, medical imaging, robotics, surveillance, and autonomous vehicles.

__Libraries or Frame works used - opencv__

__Version - 4.10.0.84__

__Developed Logics -__

__A. bgr2gray__

Converts a color image from BGR (Blue-Green-Red) to grayscale.

Grayscale images reduce memory usage and computational cost since they contain only intensity information.

Useful as a preprocessing step for many image processing algorithms, like edge detection and object tracking.

__Input Image:__

![image1](https://github.com/user-attachments/assets/e8974556-2e3b-4ef8-937d-d3e05f6f37c6)

__Output Image:__

![image2](https://github.com/user-attachments/assets/77b28683-a89e-46f3-9402-798f930f6edd)

__B. blur__

Applies blurring to reduce image noise and smooth out details.

Common blurring techniques include Gaussian, median, and bilateral blurs.

Helps to remove small details, making it easier to detect larger features or objects.

__Output Image:__

![image2](https://github.com/user-attachments/assets/77b28683-a89e-46f3-9402-798f930f6edd)

__c. contour__

Detects and outlines the contours of objects within an image, often based on shape or intensity changes.
   
Useful for object recognition, shape analysis, and image segmentation.
   
Commonly used with thresholding or edge detection techniques to isolate contours.

__Output Image:__

![contour](https://github.com/user-attachments/assets/e73aeadb-3f78-4f1f-a426-d3a37ec69b11)

__D. crop__

Extracts a specific region of interest (ROI) from the image.

Helps focus on relevant parts of the image and can improve computational efficiency.

Frequently used in facial recognition, object tracking, and image localization tasks.

__Output Image:__

![crop](https://github.com/user-attachments/assets/20f92200-65b7-4fb7-b655-1fa6b3fc1945)

__E. dil_ero__

Detects features and applies erosion to remove small noise or unwanted features.

Erosion reduces the thickness of object boundaries, which can be useful for separating close objects.

Often combined with dilation (another morphological operation) to refine object shapes.

__Output Image:__

![dil_ero](https://github.com/user-attachments/assets/a95b4bd9-2947-4e09-bbb5-cd1e86fd0529)

__F. edge__

Identifies edges in the image by detecting changes in intensity using gradient techniques.

Common algorithms include Canny, Sobel, and Laplacian edge detectors.

Useful for finding object boundaries, lanes in road images, and other structural information.

__Output Image:__

![edge](https://github.com/user-attachments/assets/db5042f7-0928-43b7-b575-a44c9cf0a239)

__G. hist_eq__

Enhances image contrast by equalizing its histogram, making details in different brightness ranges more visible.

Helps in improving image visibility, especially in low-light conditions or images with low contrast.

Adaptive histogram equalization (CLAHE) can be used for localized contrast enhancement.

__Output Image:__

![hist_eq](https://github.com/user-attachments/assets/65f5865c-0f53-404d-bdee-ae09f4cadfc0)

__H. hsv__

Converts an image from BGR to HSV (Hue, Saturation, Value) color space.

HSV makes color-based segmentation and detection easier as hue and saturation channels separate color and intensity.

Widely used in color-based filtering and object tracking.

__Output Image:__

![hsv](https://github.com/user-attachments/assets/f65690ed-8e23-4832-abf7-e7188fa01e39)

__I. img_noiseremoval__

Techniques such as Gaussian blur, median filtering, and bilateral filtering reduce noise while maintaining edges.

Effective noise removal minimizes noise without blurring important details, requiring a balance between smoothing and detail retention.

Noise reduction is essential in computer vision tasks like object detection, improving algorithm accuracy.

__Output Image:__

![noise_removal](https://github.com/user-attachments/assets/93820fc2-1dc5-4252-bbce-b4fd96671489)

__J. morphological_transformation__

Performs morphological transformations like dilation, erosion, opening, and closing.

Used for noise removal, enhancing object boundaries, and filling gaps.

Commonly applied after thresholding or edge detection for shape refinement.

__Output Image:__

![image](https://github.com/user-attachments/assets/6cbce538-c9f8-44d0-ad92-f094476fe433)

__K. resize__

Changes the image dimensions while preserving or adjusting aspect ratio.

Important for preparing images for machine learning models that require fixed input sizes.

Can help balance image resolution with computational efficiency.

__Output Image:__

![resize](https://github.com/user-attachments/assets/362d667e-ca9d-4b87-bbb5-5d3a5e1538a3)

__L. rotate__

Rotates the image to a specified angle, either clockwise or counterclockwise.

Useful for correcting orientation or creating rotated data augmentations for models.

The rotation center and scale can be adjusted to control the rotation behavior.

__Output Image:__

![image](https://github.com/user-attachments/assets/9b541cf9-898e-41a7-9ed0-986d34f825d6)

__M. stack__

Combines multiple images into a single stacked format, often side-by-side or in a grid.

Useful for comparing processed images with the original or for creating multi-image displays.

Helps in visualizing step-by-step transformations in image processing.

__Output Image:__

__Horizontal stacking:__

![stack1](https://github.com/user-attachments/assets/a727ebcd-e14e-4003-8b16-949274ceebea)

__Vertical stacking:__

![stack](https://github.com/user-attachments/assets/33930efa-c736-420b-ac15-ebe27583b2e4)

__N. template__

Creates a template for matching specific patterns or objects within an image.

Uses template matching techniques to find occurrences of the template in larger images.

Helpful in applications like logo detection, object localization, and pattern recognition.

__Output Image:__

![image](https://github.com/user-attachments/assets/d0d37723-bef7-47f6-b0f1-c4e2c899425e)

__Video Processing__

Video processing refers to the manipulation, enhancement, and analysis of video data using various computational techniques. It involves applying algorithms to extract useful information, improve video quality, or transform the video for specific applications, such as computer vision, entertainment, security, or healthcare. Video processing encompasses a range of operations from basic editing to complex analysis, often performed in real-time or on pre-recorded content.

__Libraries or Frame works used - opencv__

__Version - 4.10.0.84__

__Developed Logics -__

__A. multivid__

Specifies the directory for storing and accessing video files for organized processing.

Enables batch processing by allowing automated access to multiple videos.

Facilitates easy retrieval and organization of video datasets or archived footage.

__Output Screenshot:__

![multivid](https://github.com/user-attachments/assets/115c8f0b-dbc8-42ca-885f-f077fe30e459)

__B. vid_fps__

Controls the playback speed and smoothness of video.

Allows adjustment of video speed, such as slow-motion or time-lapse effects.

Essential for synchronization with audio and meeting playback standards.

__Output Screenshot:__

![1](https://github.com/user-attachments/assets/587ece74-6c36-41d6-85cd-cd6a170cf276)

__C. vid_save__

Saves the processed video in a specified format (e.g., MP4, AVI).

Allows configuration of compression and resolution for quality and compatibility.

Supports adding metadata like timestamps or annotations for better tracking.

__Output Screenshot:__

![2](https://github.com/user-attachments/assets/fe1954b3-657a-4df7-b408-224dd07a62e0)

__D. vid_stack__

Combines multiple frames side-by-side or sequentially for analysis.

Useful for visual comparisons, like original vs. processed frames.

Supports temporal visualization, aiding in monitoring changes over time.

__Output Screenshot:__

![3](https://github.com/user-attachments/assets/fe3ded8b-302a-4083-9a11-51b571bbfd1c)

__E. vid_stream__

Captures live video from sources like webcams, IP cameras, or online streams.

Ideal for real-time applications like surveillance or live broadcasting.

Enables integration with processing features like motion detection or object tracking.

__Output Screenshot:__

![4](https://github.com/user-attachments/assets/a80e02f1-3423-4b05-a405-9fd0e8bb8842)


__ANNOTATIONS__

Annotations in the context of data science, machine learning, and image/video processing refer to the process of adding descriptive or metadata labels to data. These labels provide additional context or information that helps in training algorithms, understanding data, or facilitating analysis. Annotations are particularly important in supervised learning, where models are trained using labeled data.

__Libraries or Frame works used - opencv, labelimg__

__Version - 4.10.0.84 , version of labelImg - 1.8.6__

__Developed Logics -__ 

__A. Data Segregate__

Splits data into different categories or sets for analysis based on certain criteria or characteristics.

Helps in organizing data into groups, making it easier to process, analyze, and draw meaningful conclusions.

Commonly used in machine learning to separate training, validation, and test datasets, or to organize data based on features like class labels, demographics, or time periods.

__Output Screenshot:__

![5](https://github.com/user-attachments/assets/4aadac84-5846-47bf-b198-51a47eba478e)

__B. label__

Directory and File Handling:The code iterates through the label files in the specified label_dir and checks for corresponding images in image_dir. If the output directory does not exist, it creates it to save processed images with bounding boxes.

Bounding Box Drawing:For each label file, the code reads bounding box information (class ID, x and y center, width, height), calculates the bounding box coordinates, and draws a green rectangle on the image to represent the bounding box.

Output Image Saving:Each processed image with bounding boxes is saved to output_dir, and a confirmation message is printed for each successfully processed file.

__Output Screenshot:__

![gun](https://github.com/user-attachments/assets/e5f2cf79-5a83-4360-a449-106cd3d11274)

__C. Label Manipulate__

Modifies or adjusts labels to refine data categories or correct labeling errors.

Can be used to handle mislabeled data or to reassign labels to reflect more accurate or refined categories, such as updating class labels based on new insights or correcting annotation mistakes.

Often used during data cleaning and preprocessing phases to improve the quality of the dataset and ensure the accuracy of the model being trained.

__Output Screenshot:__

![6](https://github.com/user-attachments/assets/b7451501-1836-426f-85e6-c15e21b8ff9c)


__Face_Recognition__

Face recognition is a biometric technology used to identify or verify individuals by analyzing their facial features. It involves capturing and analyzing facial patterns from an image or video and comparing them to a database of known faces to find a match. Face recognition can be used for both identification (determining who someone is) and verification (confirming someone’s identity).

__Libraries or Frameworks used-__

opencv-python ==4.10.0.84
face_recognition == 1.3.0
dlib == 19.24.6
pandas == 2.2.3
numpy == 2.1.2
datetime == 5.5
imutils == 0.5.4

__Developed Logics -__

__A. vaadyuthi_attendance_save__

Face Recognition and Detection:The code detects faces in real-time using the webcam, compares the detected face with a known face (Vaadyuthi), and identifies her if the match is above a certain confidence threshold.

Recording Attendance:When Vaadyuthi is recognized, the system records the date and time in a DataFrame and saves the attendance to an Excel file once a specified number of recognitions (5) is reached.

Real-Time Video Processing:The code captures video from the webcam, draws a bounding box around recognized faces, displays "Vaadyuthi" or "Not Vaadyuthi," and shows the video stream in real-time until the 'q' key is pressed.

__Output Screenshot:__

![7](https://github.com/user-attachments/assets/88bd7fa4-4ea7-42c4-a1de-8bcad7f03a56)

![8](https://github.com/user-attachments/assets/1e847227-5d9a-4d74-bb42-0d4877a64f3d)

__B. vaadyuthi_atten_score__

1.Face Recognition and Attentiveness:The code recognizes Vaadyuthi's face and calculates an attentiveness score based on her head pose (yaw and pitch). If the score is above 0.5, she is marked as attentive. 

2. Logging and Saving Screenshots:When Vaadyuthi is recognized, the program logs her attendance, attentiveness score, and saves a screenshot with a label indicating her attentiveness.

3. Periodic Data Saving:The attendance and attentiveness data is saved to an Excel file every 30 seconds and also upon program exit to preserve the information.

__Output Screenshot:__

![9](https://github.com/user-attachments/assets/923cb931-5fd7-4e34-8d23-43ac624e94c2)

![10](https://github.com/user-attachments/assets/9f67776f-260a-423b-851a-d093ea58b214)

__C. vaadyuthi_avg_atten_score__

Face Recognition and Attentiveness Calculation:The code recognizes Vaadyuthi's face and calculates an attentiveness score based on head pose (yaw and pitch). If the score is above 0.5, she is considered attentive. 

2.Logging and Screenshot Saving:When Vaadyuthi is detected, the program logs her attendance, attentiveness score, and saves a screenshot with a label indicating her attentiveness.

3.**Periodic Data Saving and Average Calculation:**The code saves the attendance data to an Excel file every 30 seconds and calculates the average attentiveness score at the end of the session, appending it to the final log.

__Output Screenshot:__

![11](https://github.com/user-attachments/assets/4141723a-7e8d-405d-ac42-d0c68816f790)

![12](https://github.com/user-attachments/assets/62a4d720-a3a2-49dd-b655-7b9558bdfbc1)

__D. vaadyuthi_excel_sc_dt__

Face Recognition and Logging: The code recognizes "Vaadyuthi" by comparing detected faces with a known image, and logs her attendance every 2 minutes or after a 5-minute gap, capturing screenshots with timestamps.

Time-Based Logging and Screenshot Saving:Screenshots are saved with a timestamp on them, and the attendance of "Vaadyuthi" is logged in a DataFrame with a screenshot and time. New entries are logged if 2 minutes pass or if a 5-minute gap occurs.

Periodic Excel Saving:The code saves the attendance DataFrame to an Excel file every 30 seconds, ensuring continuous logging, and performs a final save at the end of the session.

__Output Screenshot:__

![13](https://github.com/user-attachments/assets/25664870-94f3-42af-8e88-44ab0fc9bcf5)

![14](https://github.com/user-attachments/assets/f84f98f7-e2b1-43ab-8178-1088e18c3353)

__E. vaadyuthi_excel_sc__

Face Recognition and Logging:The code recognizes "Vaadyuthi" by comparing detected faces with a known image, logging her attendance in a DataFrame with a screenshot and timestamp when she is detected. 

Time-based Logging and Gap Control:It logs an entry for Vaadyuthi every 30 seconds, and if 5 minutes pass without recognition, it logs again. Screenshots are saved with each log.

Periodic Excel Saving:The code periodically saves the attendance DataFrame to an Excel file every 30 seconds and at the end of the session, ensuring all recognized entries are recorded.

__Output Screenshot:__

![15](https://github.com/user-attachments/assets/8965dfc8-99d3-4145-86a4-58ed7615f689)

![16](https://github.com/user-attachments/assets/207dc863-0078-4672-b94c-b9867e688959)

__F. vaadyuthi_face_recog__

Face Recognition with Known Image:The code loads a known image (presumed to be Vaadyuthi) and compares detected faces in the video stream with this known image using face encoding.

Face Detection and Recognition in Real-Time:The camera continuously captures frames, detects faces, and compares them to the known face encoding. If the detected face matches the known image (based on a confidence threshold), it labels the face as "Vaadyuthi".

Display and Annotate Video Stream:The code draws bounding boxes around recognized faces and displays the name "Vaadyuthi" or "Not Vaadyuthi" based on whether the face is recognized. The video stream continues until the user presses the 'q' key to stop it.

__Output Screenshot:__

![17](https://github.com/user-attachments/assets/dc7f1bde-b935-4971-9032-fc5bfee2e5b9)

__G. vaadyuthi_landmark__

Face Recognition and Landmark Detection:The code captures live video, detects faces, and compares them to a known image of Vaadyuthi. Upon recognizing Vaadyuthi, it performs facial landmark detection to analyze the head pose and detect attentiveness.

Head Pose Analysis for Attentiveness:Using detected facial landmarks, the code estimates the head's yaw, pitch, and roll to determine if Vaadyuthi is attentive (i.e., facing forward with minimal head movement).

Screenshot and Data Logging:If Vaadyuthi is attentive, a screenshot is saved with a label ("Attentive" or "Not Attentive"). This information, along with the date, time, and screenshot path, is logged in a DataFrame and saved to an Excel file every 30 seconds.

__Output Screenshot:__

![18](https://github.com/user-attachments/assets/a889c0ce-ff05-4919-b4e0-d2fb961a7137)

![19](https://github.com/user-attachments/assets/d62fdbe9-3962-4552-a008-2142abc008f2)

__H. vaadyuthi_test__

Face Recognition and Attendance Logging:The code uses the face_recognition library to recognize a known face (Vaadyuthi) from the webcam feed. If Vaadyuthi is detected, the code logs the recognition event in a DataFrame with the current date and time.

Entry Validity and Time Gap Handling:The code checks if a person has been recognized within the last 2 minutes. If no recognition has occurred within that time, a new entry is logged. If 5 minutes have passed since the last entry, another entry is recorded for the same person.

Periodic Data Saving:The attendance data (name, date, time) is saved to an Excel file (vaadyuthi_recognized_faces.xlsx) every 30 seconds, ensuring that the information is periodically backed up during the live video stream.

__Output Screenshot:__

![20](https://github.com/user-attachments/assets/904ff1e1-e097-4f42-a808-01d8e19c2b0c)

