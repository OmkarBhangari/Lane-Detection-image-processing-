# Lane Detection of Self Driving car(ADAS)
Lane line detection is a critical aspect of modern driving safety systems, especially in the context of autonomous vehicles and driver assistance technologies. To address the challenges of real-time performance and accuracy in lane detection, a sophisticated algorithm leveraging advanced Hough transform techniques is proposed. This algorithm, implemented using Python and image processing libraries, follows a systematic approach to enhance the detection of lane lines in roadway images.

## Algorithm Overview

1. **RGB to Grayscale Conversion**: The first step involves converting the RGB frame captured by the vehicle’s camera into a grayscale image. This conversion simplifies the image data while retaining essential features relevant for lane detection.

2. **Noise Reduction with Gaussian Blur**: Subsequently, a Gaussian blur is applied to the grayscale image to reduce noise and smooth out any irregularities, ensuring cleaner edge detection results.

3. **Edge Detection with Canny Algorithm**: Edge detection is performed using the Canny algorithm, which identifies areas of significant intensity change within the Gaussian blurred image. These identified edges often correspond to potential lane lines on the road surface.

4. **Region of Interest Extraction**: To improve efficiency and accuracy, it’s essential to focus on the region of interest within the image, corresponding to the lane the vehicle intends to navigate. Through region of interest extraction, the algorithm isolates the relevant portion of the image containing the lane of interest. This step helps in concentrating computational resources on the critical areas, thereby enhancing the detection performance.

5. **Masking Operation**: Finally, a masking operation is applied to further refine the region of interest, eliminating irrelevant information outside the lane boundaries.

## Objective

By implementing this comprehensive approach to lane detection using Python and image processing techniques, the algorithm aims to facilitate safer driving conditions. By assisting drivers in staying within their lanes and potentially preventing accidents caused by negligence or fatigue, it contributes to overall road safety and enhances the capabilities of autonomous vehicles.
