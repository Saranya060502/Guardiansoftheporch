# Project: PorchProtector

## Inspiration
Many delivery packages are left at doorsteps, leading to package theft or misdelivery. Current security cameras record footage but do not actively alert the owner if someone unauthorized picks up the package. We aim to address this problem using modern Computer Vision technology.

## Problem Statement
We try to model this problem as a computer vision-based package security system that detects when a package is picked up and checks whether the person is authorized (recognized face) or unauthorized (stranger). If an unauthorized person picks up the package, an instant alert is sent to the package owner.

## How we built it
Our first approach leverages distinct pre-trained models for package detection, face recognition, and body detection. Specifically:
**Package Detection**- We employ a pre trained object detection model (hosted on Roboflow) to localize parcels within each frame. (link)
**Face Recognition**- We rely on the Python-based face-recognition library to draw bounding boxes around any detected faces.
**Body Detection**- Using OpenCV’s built-in functions, we identify and bound the person’s body region.

After obtaining these three bounding boxes (parcel, face, body) per frame, we compute their overlap. If at least 80% of the parcel’s bounding box area intersects with either the face or body bounding box, we infer that the parcel is being picked up. This threshold-based overlap check helps minimize false positives while ensuring robust pickup detection


## Challenges we ran into
1. Acquiring diverse, high-quality training data for real scenarios
2. Ensuring reliable performance under varied environmental conditions (lighting, weather, clutter).
3. Handling limited or unstable connectivity that can delay or disrupt real-time alerts and app updates

## Edge Cases that we thought of considering
1. Minimizing false alarms by accurately distinguishing between authorized and unauthorized package pickups (for example- relatives/friends).
2. Avoiding tagging delivery person when they are delivering the package
3. Handling overlapping or stacked packages that obscure the system’s view of each parcel.
4. Distinguishing user-placed parcels (e.g., outgoing returns) from newly delivered packages.


