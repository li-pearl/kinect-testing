# import plotly.graph_objs as go
# import pandas as pd

# # Load the CSV data into a DataFrame
# data_file = r'C:\Users\anshi\code\pgss-folder\kinect-testing\KinectSkeletonRecording\SkeletonData.csv'
# df = pd.read_csv(data_file)

# # Initialize a 3D figure
# fig = go.Figure()

# # Define the connections between joints
# connections = [
#     ('SpineBase', 'SpineMid'),
#     ('SpineMid', 'Neck'),
#     ('Neck', 'Head'),
#     ('ShoulderLeft', 'ElbowLeft'),
#     ('ElbowLeft', 'WristLeft'),
#     ('WristLeft', 'HandLeft'),
#     ('ShoulderRight', 'ElbowRight'),
#     ('ElbowRight', 'WristRight'),
#     ('WristRight', 'HandRight'),
#     ('HipLeft', 'KneeLeft'),
#     ('KneeLeft', 'AnkleLeft'),
#     ('AnkleLeft', 'FootLeft'),
#     ('HipRight', 'KneeRight'),
#     ('KneeRight', 'AnkleRight'),
#     ('AnkleRight', 'FootRight'),
#     ('SpineMid', 'SpineShoulder'),
#     ('SpineShoulder', 'ShoulderLeft'),
#     ('SpineShoulder', 'ShoulderRight'),
#     ('HandLeft', 'HandTipLeft'),
#     ('HandRight', 'HandTipRight'),
#     ('HandLeft', 'ThumbLeft'),
#     ('HandRight', 'ThumbRight')
# ]

# # Add traces for each connection
# for connection in connections:
#     joint1, joint2 = connection
    
#     # Construct column names for X, Y, Z coordinates
#     joint1x, joint1y, joint1z = f'{joint1}X', f'{joint1}Y', f'{joint1}Z'
#     joint2x, joint2y, joint2z = f'{joint2}X', f'{joint2}Y', f'{joint2}Z'
    
#     # Add a line trace for this connection
#     fig.add_trace(
#         go.Scatter3d(
#             x=[df[joint1x].iloc[0], df[joint2x].iloc[0]],  # Use .iloc[0] to get the first frame; adjust as needed
#             y=[df[joint1y].iloc[0], df[joint2y].iloc[0]],
#             z=[df[joint1z].iloc[0], df[joint2z].iloc[0]],
#             mode='lines+markers',
#             line=dict(width=2, color='blue'),
#             marker=dict(size=4, color='red'),
#             name=f'{joint1} to {joint2}'
#         )
#     )

# # Adjust layout for 3D plotting
# fig.update_layout(
#     title='3D Skeleton Visualization',
#     scene=dict(
#         xaxis=dict(title='X'),
#         yaxis=dict(title='Y'),
#         zaxis=dict(title='Z'),
#         aspectmode='cube'  # Adjust aspect ratio
#     )
# )

# # Show the figure
# fig.show()

import pandas as pd

# Load the CSV data into a DataFrame
data_file = r'C:\Users\anshi\code\pgss-folder\kinect-testing\KinectSkeletonRecording\SkeletonData.csv'
df = pd.read_csv(data_file)

# Print the column names to debug
print(df.columns)