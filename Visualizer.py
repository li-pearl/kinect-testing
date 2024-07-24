import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the CSV file
data_file = r'C:\Users\anshi\code\pgss-folder\kinect-testing\KinectSkeletonRecording\SkeletonData.csv'
data = pd.read_csv(data_file)

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)  
ax.set_ylim(-2, 2) 
ax.set_aspect('equal')

# Initialize lists to store the joint positions
lines = []
joint_positions = {
    'SpineBase': (0, 1),
    'SpineMid': (0, 2),
    'Neck': (0, 3), 
    'Head': (0, 4),
    'ShoulderLeft': (0, 5),
    'ElbowLeft': (0, 6),
    'WristLeft': (0, 7),
    'HandLeft': (0, 8),
    'ShoulderRight': (0, 9),
    'ElbowRight': (0, 10),
    'WristRight': (0, 11),
    'HandRight': (0, 12),
    'HipLeft': (0, 13),
    'KneeLeft': (0, 14),
    'AnkleLeft': (0, 15),
    'FootLeft': (0, 16),
    'HipRight': (0, 17),
    'KneeRight': (0, 18),
    'AnkleRight': (0, 19),
    'FootRight': (0, 20),
    'SpineShoulder': (0, 21),
    'HandTipLeft': (0, 22),
    'ThumbLeft': (0, 23),
    'HandTipRight': (0, 24),
    'ThumbRight': (0, 25)
}

def update_plot(frame):
    ax.clear()
    ax.set_xlim(-2, 2) 
    ax.set_ylim(-2, 2)  
    ax.set_aspect('equal')

    # Get the frame data
    if frame >= len(data):
        return
    frame_data = data.iloc[frame]

    # # Plot each joint
    # for joint, index in joint_positions.items():
    #     if joint in frame_data:
    #         x = frame_data[f'{joint}X']
    #         y = frame_data[f'{joint}Y']
    #         ax.plot(x, y, 'o', label=joint)
    #     else:
    #         print(f"Missing data for {joint} at frame {frame}")

    # Draw lines between connected joints (e.g., spine, arms, legs)
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

    for start, end in connections:
        if start in joint_positions and end in joint_positions:
            if f'{start}X' in frame_data and f'{end}X' in frame_data:
                x_start = frame_data[f'{start}X']
                y_start = frame_data[f'{start}Y']
                x_end = frame_data[f'{end}X']
                y_end = frame_data[f'{end}Y']
                ax.plot([x_start, x_end], [y_start, y_end], 'k-')

    return lines

# Set up the animation
ani = animation.FuncAnimation(fig, update_plot, frames=len(data), interval=10, repeat=True)

plt.show()
