from smart_matcher import SmartMatcher

# 1. Создаем матчер
matcher = SmartMatcher()

# 2. Загружаем имеющиеся тендеры
print("Загружаем тендеры...")
matcher.load_tenders()

# 3. Строим индекс для поиска (если он еще не построен)
matcher.build_index()

print("Готово!\n")

# 4. Магия умного поиска: находим все, что связано со "сверлильным станком"
test_query = "сверлильный станок"
print(f"Ищем тендеры по запросу: '{test_query}'")
print("-" * 40)

results = matcher.match(test_query)
for i, res in enumerate(results, 1):
    print(f"{i}. Файл: {res['file']}")
    print(f"   Релевантность: {res['score'] * 100:.1f}%")
    if res.get('matched_items'):
        print(f"   Найденные позиции: {', '.join(res['matched_items'])}")
    print("-" * 25)