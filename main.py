# Imports
from pyniryo import *

# - Constants
workspace_name = "tictactoe" #"ITM-Test"  # Robot's Workspace Name
robot_ip_address = "169.254.200.200" #"192.168.0.228"

# The pose from where the image processing happens
#observation_pose = PoseObject(
#    x=0.16, y=0.0, z=0.35,
#    roll=0.0, pitch=1.57, yaw=0.0,
#)
observation_pose = PoseObject(
    x=0.006, y=0.16, z=0.35,
    roll=0.25, pitch=1.57, yaw=1.6,
)
# Place pose
place_pose = PoseObject(
    x=0.0, y=-0.2, z=0.085,
    roll=0.0, pitch=1.57, yaw=-1.57
)

# - Initialization

# Connect to robot
robot = NiryoRobot(robot_ip_address)
# Calibrate robot if the robot needs calibration
robot.calibrate_auto()
# Updating tool
#robot.update_tool()
#robot.grasp_with_tool()

# --- -------------- --- #

# robot.move_pose(observation_pose)
# # Trying to pick target using camera
# obj_found, shape_ret, color_ret = robot.vision_pick(workspace_name)
# if obj_found:
#     robot.place_from_pose(place_pose)
#
# robot.set_learning_mode(True)


# Initializing variables
offset_size = 0.05
max_catch_count = 2

# Loop until enough objects have been caught
catch_count = 0
robot.vision_pick("ITM-Test", height_offset=0.005)
#while catch_count < max_catch_count:
#    # Moving to observation pose
#    robot.move_pose(observation_pose)
#    # Trying to get object via Vision Pick
#    obj_found, shape, color = robot.vision_pick(workspace_name, height_offset=0.005)
#    if not obj_found:
#        robot.wait(0.1)
#        continue
#    # Calculate place pose and going to place the object
#    next_place_pose = place_pose.copy_with_offsets(x_offset=catch_count * offset_size)
#    robot.place_from_pose(next_place_pose)
#    catch_count += 1

robot.move_pose(observation_pose)
#TODO am anfang über ne Funktion die 9 Positionen der Felder einlesen
pose_1 = robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=0.5, y_rel=0, yaw_rel=0)
pose_2 = robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=0.5, y_rel=0.5, yaw_rel=0)
print(robot.detect_object(workspace_name))
print(robot.detect_object(workspace_name))
robot.move_pose(pose_1)
robot.move_pose(observation_pose)
robot.place_from_pose(pose_2)
#robot.move_pose(pose_2)
#robot.release_with_tool()

# Getting calibration param
mtx, dist = robot.get_camera_intrinsics()
# Moving to observation pose
robot.move_pose(observation_pose)

while "User do not press Escape neither Q":
    # Getting image
    img_compressed = robot.get_img_compressed()
    # Uncompressing image
    img_raw = uncompress_image(img_compressed)
    # Undistorting
    img_undistort = undistort_image(img_raw, mtx, dist)

    # - Display
    # Concatenating raw image and undistorted image
    concat_ims = concat_imgs((img_raw, img_undistort))

    # Showing images
    key = show_img("Images raw & undistorted", concat_ims, wait_ms=30)
    if key in [27, ord("q")]:  # Will break loop if the user press Escape or Q
        break

robot.go_to_sleep()


# --- -------------- --- #



robot.go_to_sleep()