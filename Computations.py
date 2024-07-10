import pandas as pd
from io import StringIO


def get_means (input):
    file_path = input

    with open(file_path, 'r') as file:
        file_contents = file.read()

    file_contents = '\n'.join(file_contents.split('\n')[2:])

    df = pd.read_csv(StringIO(file_contents), delim_whitespace=True)

    df = df[['Slide','Rise', 'Tilt', 'Roll', 'Twist']]

    mean = df.mean()

    return mean

