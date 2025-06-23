
def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            total = 0
            count = 0

            for line in file:
                line = line.strip()
                name, salary = line.split(',')
                total += int(salary)
                count += 1
            
            average = total / count if count else 0
            return total, average
    except FileNotFoundError:
        print("Файл не знайдений:", path)
        return 0, 0

total, average = total_salary("salary.txt")
print(f"Загальна сума: {total}, Середня зарплата: {average}")