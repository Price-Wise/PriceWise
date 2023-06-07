import shutil

def get_item_from_file():
    item_list = ['iphone', 'ipad', 'macbook', 'glasses', 'mug', 'airpods', 'watch','backpack']
    file_path = "runs\detect\labels\captured_image.txt" 
    
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            first_number = int(first_line.split()[0])
            item_index = first_number   # Adjusting index as the list starts from 0
            if 0 <= item_index < len(item_list):
                return item_list[item_index]
            else:
                return "Invalid number"
    except FileNotFoundError:
        return " No items to detect"

print(get_item_from_file())

def clear_runs_directory():
    directory_path="runs\detect"
    shutil.rmtree(directory_path)

clear_runs_directory()



