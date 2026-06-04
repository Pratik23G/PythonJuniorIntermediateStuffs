#recap on what we learned yesterday

#iterators are actually cool i do noot know much but here is
#what i remember
list_of_num = [23, 45, 67, 78, 90]
next_sum = iter(list_of_num)
print(list(next_sum))


#generators are really good if we have a large data sets to open and read
#they work lazily but saves a lot of memory
#way to open and read the file contents is by using yield

def read_file(file_name):
    with open(file_name, "r") as file:
        for row in file:
            col = row.split("|")
            if len(col) < 4:
                continue
            
            Offer = col[2].strip()
            Accepted = col[3].strip()
            company_name = col[0].strip()
            if Offer == "Yes" and Accepted == "Yes":
                yield company_name

show_content = read_file("jobGoals.txt")
print(list(show_content))