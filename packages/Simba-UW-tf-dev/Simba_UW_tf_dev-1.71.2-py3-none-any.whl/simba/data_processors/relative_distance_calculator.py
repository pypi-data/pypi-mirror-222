from typing import Union, Tuple

import os
import pandas as pd
from itertools import combinations
from simba.mixins.config_reader import ConfigReader
from simba.mixins.feature_extraction_mixin import FeatureExtractionMixin
from simba.utils.errors import NoDataError
from simba.utils.read_write import read_df, get_fn_ext



class RelativeDistanceCalculator(ConfigReader, FeatureExtractionMixin):

    def __init__(self,
                 config_path: Union[str, os.PathLike],
                 time_windows_s: Tuple[float] = (0.2, 0.4, 0.8, 1.6)):

        ConfigReader.__init__(self, config_path=config_path, read_video_info=True)
        FeatureExtractionMixin.__init__(self)
        if len(self.feature_file_paths) == 0:
            raise NoDataError(msg=f'No data files found in {self.features_dir}')
        self.time_windows = time_windows_s


    def run(self):
        for file_cnt, file_path in enumerate(self.feature_file_paths):
            df = read_df(file_path=file_path, file_type=self.file_type)
            _, video_name, _ = get_fn_ext(filepath=file_path)
            _, _, fps = self.read_video_info(video_name=video_name)
            animal_combinations = list(combinations(list(self.animal_bp_dict.keys()), 2))
            for animal_combination in animal_combinations:
                first_animal_bps, second_animal_bps = [], []
                for bp in self.animal_bp_dict[animal_combination[0]]['X_bps']: first_animal_bps.extend(([f'{bp[:-2]}_x', f'{bp[:-2]}_y']))
                for bp in self.animal_bp_dict[animal_combination[1]]['X_bps']: second_animal_bps.extend(([f'{bp[:-2]}_x', f'{bp[:-2]}_y']))
                first_animal_df, second_animal_df = df[first_animal_bps].astype(int), df[second_animal_bps].astype(int)
                for time_window in self.time_windows:
                    frames_in_window = int(fps * time_window)
                    print(frames_in_window)




                # first_animal_array, second_animal_array = df[first_animal_bps].values.reshape(len(df), -1, 2), df[second_animal_bps].values.reshape(len(df), -1, 2)
                # print(second_animal_array)


                #print(first_animal_array)

            # for animal_name, animal_body_parts in self.animal_bp_dict.items():
            #     animal_bp_col_names = []
            #
            #


test = RelativeDistanceCalculator(config_path='/Users/simon/Desktop/envs/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini')
test.run()







