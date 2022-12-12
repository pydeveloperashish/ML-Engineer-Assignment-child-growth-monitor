import pandas as pd

data = pd.read_excel("height_and_pose.xlsx")
print(data['Pose'].get('bbox_coordinates'))