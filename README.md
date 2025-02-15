# Voxel51
## Inspiration
Many delivery packages are left at doorsteps, leading to package theft or misdelivery. Current security cameras record footage but do not actively alert the owner if someone unauthorized picks up the package

## What it does
A computer vision-based package security system that detects when a package is picked up and checks whether the person is authorized (recognized face) or unauthorized (stranger). If an unauthorized person picks up the package, an instant alert is sent to the package owner.

## How we built it


## Challenges we ran into
1. If a person is picking up the package he/she might be his acquaintance, in that case, we can add the person’s image to the authorized set of personnel images.
2. In the second scenario, we might have the delivery person handling the package and the system might send a false alert
3. also the owner of the product might have relatives at his doorsteps who might not have anything to do with the project again forcing the system to send s false a alarm.


