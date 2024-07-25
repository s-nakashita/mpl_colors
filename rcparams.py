import matplotlib as mpl
import matplotlib.pyplot as plt
import re

data = plt.rcParams

fname = 'rcparams.tex'
with open(fname, mode='w') as f:
    f.write('\\documentclass{article}\n')
    f.write('\\usepackage[top=15truemm,bottom=15truemm,left=20truemm,right=20truemm]{geometry}\n')
    f.write('\\usepackage{xtab}\n')
    f.write('\\begin{document}\n')
    f.write('\\topcaption{Matplotlib version '+mpl.__version__+' rcParams}\n')
    f.write('\\tablehead{\\hline key & default value\\\ \\hline}\n')
    f.write('\\tabletail{\\hline}\n')
    f.write('\\tablelasttail{\\hline}\n')
    f.write('\\centering\n')
    f.write('\\begin{xtabular}{p{0.35\\textwidth}|p{0.65\\textwidth}}\n')
    for k, v in data.items():
        vtxt = re.sub('#','\#',str(v))
        vtxt = re.sub('%','\%',vtxt)
        vtxt = re.sub('_','\_',vtxt)
        if vtxt=='^': vtxt="\\verb|^|"
        f.write('\\verb|'+k+'| & '+f'{vtxt}'+'\\\ \n')
    f.write('\\end{xtabular}\n')
    f.write('\\end{document}')

