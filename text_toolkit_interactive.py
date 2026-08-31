from text_toolkit import build_report, print_report

text = input("Введите текст для анализа: ")

report = build_report(text, top_n=5)

print_report(
    report,
    title="Interactive Text Analytics",
    author="Vladimir",
    mode="user_input"
)

