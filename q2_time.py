from typing import Tuple, List
from datetime import datetime
import json
from collections import Counter
import re

def extract_emojis(text: str) -> List[str]:
    """
    Extrae todos los emojis de una cadena de texto.

    :param text: La cadena de texto de la que se extraerán los emojis.
    :return: Una lista de emojis encontrados en el texto.
    """
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251" 
        "]+", flags=re.UNICODE)
    return emoji_pattern.findall(text)

def q2_time(file_path: str) -> Tuple[List[Tuple[str, int]], float]:
    """
    Mide el tiempo de ejecución para identificar los 10 emojis más utilizados en los tweets.

    :param file_path: Ruta del archivo JSON que contiene los datos de los tweets.
    :return: Una tupla que contiene una lista de los 10 emojis más utilizados y su frecuencia, 
             y el tiempo de ejecución en segundos.
    """
    start_time = datetime.now()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        tweets = [json.loads(line) for line in f]
    
    emoji_count = Counter()

    for tweet in tweets:
        text = tweet.get('content', '')
        emojis = extract_emojis(text)
        emoji_count.update(emojis)

    end_time = datetime.now()
    exec_time = (end_time - start_time).total_seconds()
    
    return emoji_count.most_common(10), exec_time

