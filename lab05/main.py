from tablestats import read_rows, count_types, total_minutes
filename = input().strip()
with open(filename, encoding="utf-8") as table:
    rows = read_rows(table)
    
counts = count_types(rows)
print(len(rows))
print(len(counts))
print(total_minutes(rows, 'ошибка'))





if __name__ == "__main__":
    main()
    
