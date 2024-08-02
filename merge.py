import json

def merge_json_files(input_path1, input_path2, output_path):
    # Read the first JSON file with UTF-8 encoding
    with open(input_path1, 'r', encoding='utf-8') as file1:
        json1 = json.load(file1)
    
    # Read the second JSON file with UTF-8 encoding
    with open(input_path2, 'r', encoding='utf-8') as file2:
        json2 = json.load(file2)
    
    # Convert lists to dictionaries for easy merging
    json1_items = {item["id"]: item for item in json1["items"]}
    json2_items = {item["id"]: item for item in json2["items"]}
    
    # Merge data
    merged_items = []
    for item_id, item in json1_items.items():
        if item_id in json2_items:
            # Combine the two dictionaries
            merged_item = {**item, **json2_items[item_id]}
            merged_items.append(merged_item)
        else:
            merged_items.append(item)
    
    # Write the merged JSON to the output file with UTF-8 encoding
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for item in merged_items:
            json.dump(item, outfile)
            outfile.write(',\n')

# Example usage
input_path1 = 'StrSheets/StrSheet_Item-21.json'
input_path2 = 'Data/ItemData/ItemData-00020.json'
output_path = 'Items_21.json'

merge_json_files(input_path1, input_path2, output_path)