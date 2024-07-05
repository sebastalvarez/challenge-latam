from typing import Tuple, List
from memory_profiler import memory_usage
import json
from collections import defaultdict
from datetime import datetime

def get_top_dates_and_users(tweets: List[dict]) -> List[Tuple[datetime.date, str]]:
    """
    Identifica las 10 fechas con más tweets y, para cada una de estas fechas,
    encuentra el usuario que más tweets ha publicado.

    :param tweets: Lista de diccionarios que contienen los datos de los tweets. Cada diccionario
                   debe tener una clave 'date' que contiene información de fecha y hora, y una clave
                   'user' que contiene otro diccionario con información de los usuarios, incluyendo 'username'.
    :return: Una lista de tuplas. Cada tupla contiene una fecha y el nombre de usuario que más tweets
             ha publicado en esa fecha.
    """
    date_user_count = defaultdict(lambda: defaultdict(int))

    for tweet in tweets:
        date_str = tweet['date'].split('T')[0]
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        username = tweet['user']['username']
        date_user_count[date][username] += 1

    top_dates = sorted(date_user_count.items(), key=lambda item: sum(item[1].values()), reverse=True)[:10]
    result = [(date, max(user_count.items(), key=lambda item: item[1])[0]) for date, user_count in top_dates]

    return result

def q1_memory(file_path: str) -> Tuple[List[Tuple[datetime.date, str]], float]:
    """
    Mide el uso de memoria para identificar las 10 fechas con más tweets y los usuarios
    que más tweets han publicado en esas fechas.

    :param file_path: Ruta del archivo JSON que contiene los datos de los tweets.
    :return: Una tupla que contiene una lista de las 10 fechas con más tweets y los usuarios que
             más tweets han publicado en esas fechas, y el uso máximo de memoria en MiB.
    """
    def inner_function():
        with open(file_path, 'r', encoding='utf-8') as f:
            data = [json.loads(line) for line in f]
        
        return get_top_dates_and_users(data)
    
    mem_usage, result = memory_usage(inner_function, retval=True, max_usage=True)
    return result, mem_usage


