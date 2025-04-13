

from logic.transform import simulation_adapter
from make_gif_simulation import do_simulation_with_binded_data
from simulation_one_day import one_day_simulation


def simulation_bind_with_analysis():
    one_day_simulation() 
    simulation_adapter()
    do_simulation_with_binded_data()



