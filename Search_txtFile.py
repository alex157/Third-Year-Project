#Search the text file containing all the JSON files to map the track_id to an artist and title
search = input("Search: ")
for line in open("C:/Users/User/Desktop/BSc Computer Science/Year 3/COMP3200 - Part III Individual Project/Dataset/Last fm dataset/Final/all_data_text.txt", encoding="utf-8"):
    if search in line:
        print (line, end=" ")
