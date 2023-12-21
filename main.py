from cost_organizer import extract_data_from_file
from receipt_api import receipt_processesor, image_to_json

def main():
    image = "image.png"
    json_response = "response1.json"
    result_response = "result.txt"

    # image_to_json(image, json_response)
    # receipt_processesor(json_response, result_response)
    # items = extract_data_from_file(result_response)
    
    #image_to_json("image.png", "response1.json")
    receipt_processesor("response1.json", "result.txt")
    items = extract_data_from_file("result.txt")

    for i in items:
        print(i, items[i])





if __name__ == "__main__":
    main()