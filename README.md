Image Processing:

Image processing is a technique used to enhance, analyze, and manipulate digital images, typically through algorithms and computer vision tools. It involves a series of operations that transform an image to improve its quality, extract useful information, or prepare it for further analysis. Image processing has a wide array of applications, including photography, medical imaging, robotics, surveillance, and autonomous vehicles.

Libraries or Frame works used - opencv

Version - 4.10.0.84

Developed Logics - 

A. bgr2gray

Converts a color image from BGR (Blue-Green-Red) to grayscale.

Grayscale images reduce memory usage and computational cost since they contain only intensity information.

Useful as a preprocessing step for many image processing algorithms, like edge detection and object tracking.

Input Image:

![image1](https://github.com/user-attachments/assets/e8974556-2e3b-4ef8-937d-d3e05f6f37c6)

Output Image:

![image2](https://github.com/user-attachments/assets/77b28683-a89e-46f3-9402-798f930f6edd)

B. blur

Applies blurring to reduce image noise and smooth out details.

Common blurring techniques include Gaussian, median, and bilateral blurs.

Helps to remove small details, making it easier to detect larger features or objects.

Output Image:

![image2](https://github.com/user-attachments/assets/77b28683-a89e-46f3-9402-798f930f6edd)

c. contour

Detects and outlines the contours of objects within an image, often based on shape or intensity changes.
   
Useful for object recognition, shape analysis, and image segmentation.
   
Commonly used with thresholding or edge detection techniques to isolate contours.

Output Image:

![contour](https://github.com/user-attachments/assets/e73aeadb-3f78-4f1f-a426-d3a37ec69b11)

D. crop

Extracts a specific region of interest (ROI) from the image.

Helps focus on relevant parts of the image and can improve computational efficiency.

Frequently used in facial recognition, object tracking, and image localization tasks.

Output Image:

![crop](https://github.com/user-attachments/assets/20f92200-65b7-4fb7-b655-1fa6b3fc1945)

E. dil_ero

Detects features and applies erosion to remove small noise or unwanted features.

Erosion reduces the thickness of object boundaries, which can be useful for separating close objects.

Often combined with dilation (another morphological operation) to refine object shapes.

Output Image:

![dil_ero](https://github.com/user-attachments/assets/a95b4bd9-2947-4e09-bbb5-cd1e86fd0529)

F. edge

Identifies edges in the image by detecting changes in intensity using gradient techniques.

Common algorithms include Canny, Sobel, and Laplacian edge detectors.

Useful for finding object boundaries, lanes in road images, and other structural information.

Output Image:

![edge](https://github.com/user-attachments/assets/db5042f7-0928-43b7-b575-a44c9cf0a239)

G. hist_eq

Enhances image contrast by equalizing its histogram, making details in different brightness ranges more visible.

Helps in improving image visibility, especially in low-light conditions or images with low contrast.

Adaptive histogram equalization (CLAHE) can be used for localized contrast enhancement.

Output Image:

![hist_eq](https://github.com/user-attachments/assets/65f5865c-0f53-404d-bdee-ae09f4cadfc0)

H. hsv

Converts an image from BGR to HSV (Hue, Saturation, Value) color space.

HSV makes color-based segmentation and detection easier as hue and saturation channels separate color and intensity.

Widely used in color-based filtering and object tracking.

Output Image:

![hsv](https://github.com/user-attachments/assets/f65690ed-8e23-4832-abf7-e7188fa01e39)

I. img_noiseremoval

Techniques such as Gaussian blur, median filtering, and bilateral filtering reduce noise while maintaining edges.

Effective noise removal minimizes noise without blurring important details, requiring a balance between smoothing and detail retention.

Noise reduction is essential in computer vision tasks like object detection, improving algorithm accuracy.

Output Image:

![noise_removal](https://github.com/user-attachments/assets/93820fc2-1dc5-4252-bbce-b4fd96671489)

J. morphological_transformation

Performs morphological transformations like dilation, erosion, opening, and closing.

Used for noise removal, enhancing object boundaries, and filling gaps.

Commonly applied after thresholding or edge detection for shape refinement.

Output Image:

![image](https://github.com/user-attachments/assets/6cbce538-c9f8-44d0-ad92-f094476fe433)

K. resize

Changes the image dimensions while preserving or adjusting aspect ratio.

Important for preparing images for machine learning models that require fixed input sizes.

Can help balance image resolution with computational efficiency.

Output Image:

![resize](https://github.com/user-attachments/assets/362d667e-ca9d-4b87-bbb5-5d3a5e1538a3)

L. rotate

Rotates the image to a specified angle, either clockwise or counterclockwise.

Useful for correcting orientation or creating rotated data augmentations for models.

The rotation center and scale can be adjusted to control the rotation behavior.

Output Image:

![image](https://github.com/user-attachments/assets/9b541cf9-898e-41a7-9ed0-986d34f825d6)

M. stack

Combines multiple images into a single stacked format, often side-by-side or in a grid.

Useful for comparing processed images with the original or for creating multi-image displays.

Helps in visualizing step-by-step transformations in image processing.

Output Image:

Horizontal stacking:

![stack1](https://github.com/user-attachments/assets/a727ebcd-e14e-4003-8b16-949274ceebea)


Vertical stacking:

![stack](https://github.com/user-attachments/assets/33930efa-c736-420b-ac15-ebe27583b2e4)

N. template

Creates a template for matching specific patterns or objects within an image.

Uses template matching techniques to find occurrences of the template in larger images.

Helpful in applications like logo detection, object localization, and pattern recognition.

Output Image:

![image](https://github.com/user-attachments/assets/d0d37723-bef7-47f6-b0f1-c4e2c899425e)

Video Processing

Video processing refers to the manipulation, enhancement, and analysis of video data using various computational techniques. It involves applying algorithms to extract useful information, improve video quality, or transform the video for specific applications, such as computer vision, entertainment, security, or healthcare. Video processing encompasses a range of operations from basic editing to complex analysis, often performed in real-time or on pre-recorded content.

Libraries or Frame works used - opencv

Version - 4.10.0.84

Developed Logics - 

A. multivid

Specifies the directory for storing and accessing video files for organized processing.

Enables batch processing by allowing automated access to multiple videos.

Facilitates easy retrieval and organization of video datasets or archived footage.

Output Screenshot:

![multivid](https://github.com/user-attachments/assets/115c8f0b-dbc8-42ca-885f-f077fe30e459)

B. vid_fps

Controls the playback speed and smoothness of video.

Allows adjustment of video speed, such as slow-motion or time-lapse effects.

Essential for synchronization with audio and meeting playback standards.

Output Screenshot:


    C. vid_save
    D. vid_stack
    E. vid_stream

ANNOTATIONS
Libraries or Frame works used - opencv, labelimg
Version - 4.10.0.84 , version of labelImg - 1.8.6
Developed Logics - 
    A. label

Face_Recognition
opencv-python ==4.10.0.84
face_recognition == 1.3.0
dlib == 19.24.6
pandas == 2.2.3
numpy == 2.1.2
datetime == 5.5
imutils == 0.5.4
Developed Logics -
    A. Atten_save
    B. Atten_score
    C. Avg_atten_score
    D. Excel_dt_sc
    E. Excel_sc
    F. Face_recognition
    G. Landmark
    H. Test
    I. vaadyuthi_attendance_save
    J. vaadyuthi_atten_score
    K. vaadyuthi_avg_atten_score
    L. vaadyuthi_excel_sc_dt
    M. vaadyuthi_excel_sc
    N. vaadyuthi_face_recog
    O. vaadyuthi_landmark
    P. vaadyuthi_test
