
def get_cats_info(path):
    cats=[]
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Невірний запис: {line}")
                    continue
                cat_id, name, age = parts
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    return cats
        
cats_info = get_cats_info("cats_file.txt")
print(cats_info)

