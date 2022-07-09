import textwrap

def wrap(string, max_width):
    wraped=textwrap.wrap(text=string, width=max_width)
    line="\n".join(wraped)
    return line

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)