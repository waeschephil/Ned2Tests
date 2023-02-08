# Imports
from pyniryo import *

# - Constants
workspace_name = "tictactoe"  # "ITM-Test"  # Robot's Workspace Name
robot_ip_address = "169.254.200.200"  # "192.168.0.228"

# The pose from where the image processing happens
# observation_pose = PoseObject(
#    x=0.16, y=0.0, z=0.35,
#    roll=0.0, pitch=1.57, yaw=0.0,
# )
observation_pose = PoseObject(
    x=0.006, y=0.16, z=0.35,
    roll=0.25, pitch=1.57, yaw=1.6,
)

#pick_pose = PoseObject(
#    x=0.180, y=0.003, z=0.242,
#    roll=2.935, pitch=1.504, yaw=2.95,
#)

pick_pose = PoseObject( #Rampe
    x=-0.168, y=0.124, z=0.167,
    roll=-0.021, pitch=1.184, yaw=1.697,
)
# Place pose
place_pose = PoseObject(
    x=0.0, y=-0.2, z=0.085,
    roll=0.0, pitch=1.57, yaw=-1.57
)

robot = NiryoRobot(robot_ip_address)
robot.calibrate_auto()

positions = [
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=0.07, y_rel=0.2, yaw_rel=0),
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=0.55, y_rel=0.2, yaw_rel=0),
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=1.0, y_rel=0.2, yaw_rel=0),
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=0.07, y_rel=0.45, yaw_rel=0),
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=0.55, y_rel=0.5, yaw_rel=0),
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=1.0, y_rel=0.45, yaw_rel=0),
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=0.05, y_rel=0.715, yaw_rel=0),
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=0.53, y_rel=0.715, yaw_rel=0),
    robot.get_target_pose_from_rel(workspace_name, height_offset=0.005, x_rel=1.0, y_rel=0.715, yaw_rel=0)
]


def tictactoe_place(index):
    preposition = PoseObject(x=-0.168, y=0.124, z=0.257, roll=-0.014, pitch=1.183, yaw=1.716,)
    pos = positions[index-1]
    robot.release_with_tool()
    robot.move_pose(preposition)
    robot.move_pose(pick_pose)
    robot.wait(0.1)
    robot.grasp_with_tool()
    robot.move_pose(preposition)
    #robot.vision_pick("ITM-Test", height_offset=0.005)
    robot.move_pose(observation_pose)
    robot.place_from_pose(pos)
    robot.move_pose(observation_pose)


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
# while catch_count < max_catch_count:
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


tictactoe_place(5)
tictactoe_place(4)
tictactoe_place(2)
tictactoe_place(9)
tictactoe_place(7)
tictactoe_place(1)

# robot.place_from_pose(pos5)

# Getting calibration param
# mtx, dist = robot.get_camera_intrinsics()
# # Moving to observation pose
# robot.move_pose(observation_pose)
#
# while "User do not press Escape neither Q":
#     # Getting image
#     img_compressed = robot.get_img_compressed()
#     # Uncompressing image
#     img_raw = uncompress_image(img_compressed)
#     # Undistorting
#     img_undistort = undistort_image(img_raw, mtx, dist)
#
#     # - Display
#     # Concatenating raw image and undistorted image
#     concat_ims = concat_imgs((img_raw, img_undistort))
#
#     # Showing images
#     key = show_img("Images raw & undistorted", concat_ims, wait_ms=30)
#     if key in [27, ord("q")]:  # Will break loop if the user press Escape or Q
#         break
#
# robot.go_to_sleep()


# --- -------------- --- #


robot.go_to_sleep()
