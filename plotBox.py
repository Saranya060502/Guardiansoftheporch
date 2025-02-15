import cv2
import json

# Load the image
image_path = "download.jpg"
image = cv2.imread(image_path)

# JSON output from inference
json_result = '''{
    "inference_id": "771df01b-1b7b-4204-8896-75d67c11efdb",
    "time": 0.03718314100115094,
    "image": {"width": 275, "height": 183},
    "predictions": [
        {"x": 105.5, "y": 112.0, "width": 71.0, "height": 30.0, "confidence": 0.760699450969696, "class": "Box", "class_id": 0, "detection_id": "fcfdbe55-b24c-4728-92c7-5da9fcdaf835"},
        {"x": 108.0, "y": 83.0, "width": 54.0, "height": 28.0, "confidence": 0.6146883964538574, "class": "Box", "class_id": 0, "detection_id": "d80df8b5-0c37-42b8-a979-a814c6ebd287"},
        {"x": 104.0, "y": 142.5, "width": 100.0, "height": 35.0, "confidence": 0.584709644317627, "class": "Box", "class_id": 0, "detection_id": "5bac3de2-de32-4907-99cb-c603196de9b7"}
    ]
}'''

# Parse the JSON result
result = json.loads(json_result)
predictions = result["predictions"]

# Draw bounding boxes
for pred in predictions:
    x, y, w, h = int(pred["x"]), int(pred["y"]), int(pred["width"]), int(pred["height"])
    top_left = (x - w // 2, y - h // 2)
    bottom_right = (x + w // 2, y + h // 2)
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)  # Blue box
    cv2.putText(image, f"{pred['class']} ({pred['confidence']:.2f})", (top_left[0], top_left[1] - 5), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Display the image
cv2.imshow("Bounding Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
