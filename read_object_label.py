import shutil

def get_item_from_file(directory):
    item_list = ['iphone', 'ipad', 'macbook', 'glasses', 'mug', 'airpods', 'watch']
    file_path = directory + "\captured_image.txt" 
    
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        first_number = int(first_line.split()[0])
        item_index = first_number   # Adjusting index as the list starts from 0
        if 0 <= item_index < len(item_list):
            return item_list[item_index]
        else:
            return "Invalid number"

directory_path = f"runs\detect\labels"  
item = get_item_from_file(directory_path)
print(item)

def clear_runs_directory():
    directory_path="runs\detect"
    shutil.rmtree(directory_path)

clear_runs_directory()



