import string
import random 


def generate_random_str(length: int) -> str:
    characters: str = string.ascii_letters + string.digits + string.punctuation
    result_string = ''.join(random.choice(characters) for _ in range(length))

    return result_string


def fuzzer() -> str:
    while True:
        yield generate_random_str(random.randint(1,100))


def sample_func(input_str:str) -> int:
    try:
        if '!!!' in input_str:
            raise Exception('Bad Input') 
        




if __name__ == '__main__':
    print(generate_random_str(20))