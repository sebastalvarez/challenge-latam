from typing import Tuple, List
from memory_profiler import memory_usage
import json
import re
from collections import Counter

def get_top_influential_users(tweets: List[dict]) -> List[Tuple[str, int]]:
    """
    Obtiene los 10 usuarios más influyentes en función del número de menciones en los tweets.

    :param tweets: Lista de diccionarios que contienen los datos de los tweets. Cada diccionario
                   debe tener una clave 'content' que contiene el texto del tweet.
    :return: Una lista de tuplas. Cada tupla contiene un nombre de usuario y el número de menciones.
    """
    mention_count = Counter()

    for tweet in tweets:
        mentions = tweet.get('content', '')
        mentioned_users = re.findall(r'@\w+', mentions)
        mention_count.update(mentioned_users)

    return mention_count.most_common(10)

def q3_memory(file_path: str) -> Tuple[List[Tuple[str, int]], float]:
    """
    Mide el uso de memoria para identificar los 10 usuarios más influyentes en función
    del número de menciones en los tweets.

    :param file_path: Ruta del archivo JSON que contiene los datos de los tweets.
    :return: Una tupla que contiene una lista de los 10 usuarios más influyentes y el número de menciones,
             y el uso máximo de memoria en MiB.
    """
    def inner_function():
        with open(file_path, 'r', encoding='utf-8') as f:
            tweets = [json.loads(line) for line in f]
        
        return get_top_influential_users(tweets)
    
    mem_usage, result = memory_usage(inner_function, retval=True, max_usage=True)
    return result, mem_usage
