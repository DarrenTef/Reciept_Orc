from cost_organizer import extract_data_from_file
from receipt_api import receipt_processesor
def main():
    receipt_processesor("response2.json", "result.txt")
    items = extract_data_from_file("result.txt")
    for i in items:
        print(i, items[i])





if __name__ == "__main__":
    main()