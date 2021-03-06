def hello_world():
    print('Hello world')
    
if __name__ == "__main__": 
    import csv
    row_list = [["SN", "Name", "Contribution"],
                 [1, "Linus Torvalds", "Linux Kernel"],
                 [2, "Tim Berners-Lee", "World Wide Web"],
                 [3, "Guido van Rossum", "Python Programming"]]
    with open('..\data\interim\protagonist.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)