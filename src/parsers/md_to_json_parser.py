import re
import json

def parse_dialog(md_text):
    """
    Парсит диалог из формата [User]/[AI] в JSON.
    
    Args:
        md_text (str): Текст диалога в формате markdown.
    
    Returns:
        str: JSON строка с структурой диалога.
    """
    # Регулярное выражение для извлечения реплик
    pattern = r'\[(User|AI)\]:\s*\n(.*?)(?=\n\[(?:User|AI)\]:|$)'
    matches = re.findall(pattern, md_text, re.DOTALL)
    
    dialog = []
    for speaker, message in matches:
        # Очищаем сообщение от лишних пробелов
        cleaned_message = message.strip()
        dialog.append({
            "speaker": speaker,
            "message": cleaned_message
        })
    
    # Формируем итоговый JSON
    output = {"dialog": dialog}
    return json.dumps(output, ensure_ascii=False, indent=2)

# Пример использования
if name == "main":
    example_dialog = """
[User]:
Привет

[AI]:
Привет! Как дела?

[User]:
Расскажи о себе.
"""
    result = parse_dialog(example_dialog)
    print(result)
