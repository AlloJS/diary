import random
def _generate_random_id():
    """
    Generatore per id unico di eventi
    :return: Ritorna un id univoco per assegnazione evento
    """
    casual_num = [random.randint(0,100) for _ in range(10)]
    casual_num_str = ''.join(str(num) for num in casual_num)
    return casual_num_str