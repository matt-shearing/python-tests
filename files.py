# with open("st.txt", "w") as st:
#     st.write(input("Type a sentence"))
#
# with open("st.txt", "r") as st:
#     print(st.read())
import csv
#
# list1 = [["Top Gun", "RB", "MR"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
#
# with open("excel.csv", "w") as e:
#     e = csv.writer(e, delimiter=",")
#     for list in list1:
#         e.writerow(list)

with open("excel.csv", "r") as e:
    e = csv.reader(e, delimiter=",")
    for row in e:
        print(",".join(row))
