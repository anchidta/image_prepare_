import os
import shutil

def select_and_save_frames(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            frame_number = int(filename.split('_')[1].split('.')[0])
            # Check if the frame number is in the range of the selected frames for each second
            if frame_number % 30 in [1, 7, 15, 19, 30]:
                shutil.copy(os.path.join(input_folder, filename), os.path.join(output_folder, filename))


# Example usage
input_folder = '/home/anchidta/wk_law/frames_output_vi4'
output_folder = 'selected_frames_vi4'
select_and_save_frames(input_folder, output_folder)
