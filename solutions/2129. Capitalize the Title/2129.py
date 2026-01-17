def capitalize_title(title: str) -> str:
    title_list = list(
        map(
            lambda x: x.lower() if len(x) in [1, 2] else x.capitalize(),
            title.split(" "),
        )
    )

    return " ".join(title_list)


print(capitalize_title("First leTTeR of EACH Word"))
