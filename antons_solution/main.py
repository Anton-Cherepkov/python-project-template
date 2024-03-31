from antons_solution.utils.colorful_print import print_green, print_yellow


def print_two_lines(text: str) -> None:
    print_green(text)
    print_yellow(text)


if __name__ == "__main__":
    print_two_lines("hello world")
