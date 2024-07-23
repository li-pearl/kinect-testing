import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the CSV data
df = pd.read_csv('KinectSkeletonRecording/SkeletonData.csv')

# Define joint connections



connections = [
    ('WristLeftX', 'HandLeftX', 'WristLeftY', 'HandLeftY'),
    ('WristRightX', 'HandRightX', 'WristRightY', 'HandRightY'),
    ('ShoulderCenterX', 'SpineX', 'ShoulderCenterY', 'SpineY'),
    ('SpineX', 'HipCenterX', 'SpineY', 'HipCenterY'),
    ('HipCenterX', 'HipLeftX', 'HipCenterY', 'HipLeftY'),
    ('HipCenterX', 'HipRightX', 'HipCenterY', 'HipRightY'),
    ('HipLeftX', 'KneeLeftX', 'HipLeftY', 'KneeLeftY'),
    ('ShoulderLeftX', 'ElbowLeftX', 'ShoulderLeftY', 'ElbowLeftY'),
    ('ElbowLeftX', 'WristLeftX', 'ElbowLeftY', 'WristLeftY'),
    ('ShoulderRightX', 'ElbowRightX', 'ShoulderRightY', 'ElbowRightY'),
    ('ElbowRightX', 'WristRightX', 'ElbowRightY', 'WristRightY'),
    ('HipRightX', 'KneeRightX', 'HipRightY', 'KneeRightY'),
    ('KneeRightX', 'AnkleRightX', 'KneeRightY', 'AnkleRightY'),
    ('HipLeftX', 'KneeLeftX', 'HipLeftY', 'KneeLeftY'),
    ('KneeLeftX', 'AnkleLeftX', 'KneeLeftY', 'AnkleLeftY'),
    ('ShoulderCenterX', 'HeadX', 'ShoulderCenterY', 'HeadY')
]

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')

def update(frame_number):
    ax.clear()  # Clear the previous frame
    row = df.iloc[frame_number]  # Get the current frame's data
    joint_positions = {}  # Store joint positions to label them

    # Plot each connection and store joint positions
    for start_x, end_x, start_y, end_y in connections:
        ax.plot([row[start_x], row[end_x]], [row[start_y], row[end_y]], 'ro-')
        joint_positions[start_x[:-1]] = (row[start_x], row[start_y])  # Remove 'X' from name, store position
        joint_positions[end_x[:-1]] = (row[end_x], row[end_y])  # Remove 'X' from name, store position

    # Label each joint
    for joint, (x, y) in joint_positions.items():
        ax.text(x, y, joint, fontsize=9, ha='right', va='bottom')  # Adjust text alignment as needed

    # Set the plot limits
    ax.set_xlim(df[['WristLeftX', 'HandLeftX', 'WristRightX', 'HandRightX', 'ShoulderCenterX', 'SpineX', 'HipCenterX', 'HipLeftX', 'HipRightX', 'KneeLeftX', 'ShoulderLeftX', 'ElbowLeftX', 'ShoulderRightX', 'ElbowRightX', 'KneeRightX', 'AnkleRightX', 'AnkleLeftX', 'HeadX']].min().min(), df[['WristLeftX', 'HandLeftX', 'WristRightX', 'HandRightX', 'ShoulderCenterX', 'SpineX', 'HipCenterX', 'HipLeftX', 'HipRightX', 'KneeLeftX', 'ShoulderLeftX', 'ElbowLeftX', 'ShoulderRightX', 'ElbowRightX', 'KneeRightX', 'AnkleRightX', 'AnkleLeftX', 'HeadX']].max().max())
    ax.set_ylim(df[['WristLeftY', 'HandLeftY', 'WristRightY', 'HandRightY', 'ShoulderCenterY', 'SpineY', 'HipCenterY', 'HipLeftY', 'HipRightY', 'KneeLeftY', 'ShoulderLeftY', 'ElbowLeftY', 'ShoulderRightY', 'ElbowRightY', 'KneeRightY', 'AnkleRightY', 'AnkleLeftY', 'HeadY']].min().min(), df[['WristLeftY', 'HandLeftY', 'WristRightY', 'HandRightY', 'ShoulderCenterY', 'SpineY', 'HipCenterY', 'HipLeftY', 'HipRightY', 'KneeLeftY', 'ShoulderLeftY', 'ElbowLeftY', 'ShoulderRightY', 'ElbowRightY', 'KneeRightY', 'AnkleRightY', 'AnkleLeftY', 'HeadY']].max().max())

ani = FuncAnimation(fig, update, frames=len(df), repeat=False)

plt.show()