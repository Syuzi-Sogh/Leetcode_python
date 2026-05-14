def process_grades(records: list[str]) -> dict:
    mark = 0
    lst_mark = []
    avg = 0
    skipped = 0
    passed = []

    for record in records:
        for ch in record:

            if ch.isdigit():
                mark = mark * 10 + int(ch)

            index = record.index(':')
            if index <= 1:
                break

        if mark != 0:
            lst_mark.append(mark)

        else:
            skipped += 1

        if mark >= 60:
            name = record.split(':')[0]
            passed.append(name)



        mark = 0

    for i in range(0, len(lst_mark)):
        avg = avg + lst_mark[i]

    if len(lst_mark) != 0:
        avg = avg / len(lst_mark)


    valid_count = len(lst_mark)
    passed = sorted(set(passed))

    return {
        "valid_count": valid_count,
        "average": avg,
        "passed": passed,
        "skipped": skipped
    }

data = [

"Иванов: 85",
"Петров: 42",
"Сидоров: abc", # битая
"Козлов: 90",
": 55", # битая
"Иванов: 70" # повтор (считаем как отдельную запись)
]
print(process_grades(data))