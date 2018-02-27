import glob as glob
import os as os
import subprocess as sp

directories = []
source = '/data/nhenriksen/projects/cds/wat6/bgbg-tip3p/a-bam-p/'
destination = 'a-bam-p/'

# for directory in glob.glob(source + 'a*'):
#     directories.append(os.path.basename(directory))
# for directory in glob.glob(source + 'u*'):
#     directories.append(os.path.basename(directory))
# for directory in glob.glob(source + 'r*'):
#     directories.append(os.path.basename(directory))
for window in range(0, 14):
    directories.append('a' + f'{window:02d}')
for window in range(0, 1):
    directories.append('r' + f'{window:02d}')
for window in range(0, 46):
    directories.append('u' + f'{window:02d}')

for directory in directories:
    if not os.path.exists(destination + directory + '/original/'):
        os.makedirs(destination + directory + '/original/')

for directory in directories:
    log_file = destination + 'rsync.log'
    rsync_list = [
        'rsync', '-armv', '-e "ssh"', '--include="mini.in"',
        '--include="therm1.in"', '--include="therm2.in"',
        '--include="eqnpt.in"', '--include="mdin"', '--include="full.crds"',
        '--include="full.hmr.topo"', '--include="disang.rest"',
        '--include="MGO.mol2"', '--include="bam.mol2"', '--exclude="*"',
        '{}'.format('davids4@kirkwood:' + source + directory + '/'),
        '{}'.format(directory + '/original/')
    ]
    with open(log_file, 'a') as file:
        file.write(' '.join(rsync_list))
        file.write('\n')
        p = sp.Popen(
            [' '.join(rsync_list)],
            cwd=destination,
            stdout=file,
            stderr=file,
            shell=True)
        output, error = p.communicate()
        if p.returncode == 0:
            pass
        elif p.returncode == 1:
            print('Output: {}'.format(output))
            print('Error: {}'.format(error))
