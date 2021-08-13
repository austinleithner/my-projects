from os.path import join
import numpy as np

map_number_to_see = 3
m_path = join('Maps', 'Map{}.npy'.format(map_number_to_see))
m = np.load(m_path)
print(m)
