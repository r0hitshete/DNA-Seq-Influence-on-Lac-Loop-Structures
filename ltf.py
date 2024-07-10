import Computations
import pandas as pd
import os
import re


data = {
    'Slide': [],
    'Rise': [],
    'Tilt': [],
    'Roll': [],
    'Twist': []
}




df = pd.DataFrame(data)
files = os.listdir("P2F1 tal")
files  = list(filter(lambda s: True if "dimer_opt.par" in s else False,files))
print(files)


dimeric = df
for f in files:
    n = int((re.findall("\d+", f))[2])
    shift = pd.Series(data = {'Shift', n}, index = ["Shift"])
    series = Computations.get_means(f)
    series = pd.concat([shift, series])

    fp = os.path.join("/P2F1", f)
    dimeric = pd.concat([dimeric,(Computations.get_means(fp)).to_frame().transpose()], ignore_index= True)

dimeric




