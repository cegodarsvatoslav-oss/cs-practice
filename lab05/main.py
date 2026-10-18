from tablestats import read_rows, count_types

with open('events.csv', encoding="utf-8") as table:
    rows = read_rows(table)
    
counts = count_types(rows)
print(counts)





if __name__ == "__main__":
    main()
    
