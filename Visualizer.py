import pandas as pd
import plotly.graph_objects as go

# Load the CSV data
df = pd.read_csv('skeletonData.csv')

# Define a function to draw a skeleton
def draw_skeleton(row):
    fig = go.Figure()

    # Define joint connections
    connections = [
        ('WristLeftX', 'HandLeftX'),
        ('WristRightX', 'HandRightX'),
        ('ShoulderCenterX', 'SpineX'),
        ('SpineX', 'HipCenterX'),
        ('HipCenterX', 'HipLeftX'),
        ('HipCenterX', 'HipRightX'),
        ('HipLeftX', 'KneeLeftX'),
        ('HipRightX', 'KneeRightX'),
        ('KneeLeftX', 'AnkleLeftX'),
        ('KneeRightX', 'AnkleRightX'),
        ('AnkleLeftX', 'FootLeftX'),
        ('AnkleRightX', 'FootRightX')
    ]

    # Draw skeleton
    for start, end in connections:
        fig.add_trace(go.Scatter3d(x=[row[start], row[end]],
                                   y=[row[start.replace('X', 'Y')], row[end.replace('X', 'Y')]],
                                   z=[row[start.replace('X', 'Z')], row[end.replace('X', 'Z')]],
                                   mode='lines+markers',
                                   marker=dict(size=4, color='red'),
                                   line=dict(color='blue', width=2)))

    # Set plot layout
    fig.update_layout(title='Skeleton Visualization',
                      scene=dict(xaxis=dict(title='X'),
                                 yaxis=dict(title='Y'),
                                 zaxis=dict(title='Z'),
                                 aspectmode='cube'))

    fig.show()

# Example: Draw the skeleton for the first row in the DataFrame
draw_skeleton(df.iloc[0])