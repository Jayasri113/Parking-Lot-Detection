import cv2
def detect_parking_spots(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply image processing techniques to detect parking spots
    # (This can vary based on your specific requirements and the image characteristics)

    # Example: Applying Canny edge detection
    edges = cv2.Canny(gray, 30, 150)

    # Example: Applying contour detection
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the detected contours and check for parking spots
    parking_spots = 0
    for contour in contours:
        # Example: Check contour area to identify parking spots
        contour_area = cv2.contourArea(contour)
        if contour_area > 500:  # Adjust this threshold based on your image
            parking_spots += 1
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)  # Mark parking spots on the image

    # Display the detected parking spots
    cv2.imshow("Detected Parking Spots", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return parking_spots

# Provide the path to the parking lot image here
image_path = "C:/Users/Abiksha G/Pictures/car 3.1.jpeg"

# Call the function to detect parking spots and display the result
available_parking_spots = detect_parking_spots(image_path)
print("Available parking spots:", available_parking_spots)
