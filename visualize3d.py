import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Load the CSV file
data_file = r'C:\Users\anshi\code\kinectv1-skeleton-recorder\new-occlusion-tests\Lukas\2_ld_whole_face.csv'
data = pd.read_csv(data_file)

# Create a 3D figure and axis for the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.view_init(elev=15, azim=-65)


# Initialize lists to store the joint positions
joint_positions = {
    # Add joint names and their initial positions here
    # Example: 'SpineBase': (0, 1, 2),
}

def update_plot(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 4 * 3)
    ax.set_zlim(-1.5, 1)
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Z Axis')
    ax.set_zlabel('Y Axis')


    if frame >= len(data):
        return

    frame_data = data.iloc[frame]

    # Plot each joint in 3D

    # for joint, (x, y, z) in joint_positions.items():
    #     if f'{joint}X' in frame_data and f'{joint}Y' in frame_data and f'{joint}Z' in frame_data:
    #         x = frame_data[f'{joint}X']
    #         y = frame_data[f'{joint}Y']
    #         z = frame_data[f'{joint}Z']
    #         ax.scatter(x, z, y, marker='o', label=joint)

    connections = [
        ('SpineBase', 'SpineMid'),
        ('SpineMid', 'Neck'),
        ('Neck', 'Head'),
        ('ShoulderLeft', 'ElbowLeft'),
        ('ShoulderLeft', 'Neck'),
        ('ElbowLeft', 'WristLeft'),
        ('WristLeft', 'HandLeft'),
        ('ShoulderRight', 'ElbowRight'),
        ('ShoulderRight', 'Neck'),
        ('ElbowRight', 'WristRight'),
        ('WristRight', 'HandRight'),
        ('HipLeft', 'KneeLeft'),
        ('KneeLeft', 'AnkleLeft'),
        ('AnkleLeft', 'FootLeft'),
        ('HipRight', 'KneeRight'),
        ('KneeRight', 'AnkleRight'),
        ('AnkleRight', 'FootRight'),
        ('SpineMid', 'SpineShoulder'),
        ('HandTipLeft', 'ThumbLeft'),
        ('HandTipRight', 'ThumbRight'),
        ('SpineBase', 'HipLeft'),
        ('SpineBase', 'HipRight')
    ]
        # Draw lines between connected joints
    for start_joint, end_joint in connections:
        if f'{start_joint}X' in frame_data and f'{start_joint}Y' in frame_data and f'{start_joint}Z' in frame_data and f'{end_joint}X' in frame_data and f'{end_joint}Y' in frame_data and f'{end_joint}Z' in frame_data:
            start_x = frame_data[f'{start_joint}X']
            start_y = frame_data[f'{start_joint}Y']
            start_z = frame_data[f'{start_joint}Z']
            end_x = frame_data[f'{end_joint}X']
            end_y = frame_data[f'{end_joint}Y']
            end_z = frame_data[f'{end_joint}Z']
            ax.plot([start_x, end_x], [start_z * 3, end_z * 3], [start_y, end_y], 'r-')

def on_key(event):
    """
    Event handler for keyboard input.
    """
    if event.key == 'enter':
        # Custom operation
        perform_custom_operation()

def perform_custom_operation():
    """
    Custom operation to be performed after input.
    """
    # Example: Scramble data or update plot data

# Bind the key press event to the 'on_key' function
fig.canvas.mpl_connect('key_press_event', on_key)

# Set up the animation
ani = animation.FuncAnimation(fig, update_plot, frames=len(data), interval=40, repeat=True)

plt.show()