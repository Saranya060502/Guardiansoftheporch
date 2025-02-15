from inference_sdk import InferenceHTTPClient
import cv2
import json

ImageName = "download.jpg"
image = cv2.imread(ImageName)

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="b7BmmitawLgeQwTGzCmB"
)

result = CLIENT.infer(ImageName, model_id="doorbell-camera-alert/3")
result = json.loads(result)
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