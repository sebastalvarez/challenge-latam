# Data Engineer Challenge
​
## Descripción General
Bienvenido al desafío para Ingenieros de Datos. En esta ocasión, tendrás la oportunidad de acercarte a parte de la realidad del rol, demostrar tus habilidades y conocimientos en procesamiento de datos con python y diferentes estructuras de datos.
​
## Instrucciones
1. Tu solución debe estar en un repositorio público de la plataforma github. 
2. Para enviar tu desafío, debes hacer un `POST` request a `https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer`. Esto es un ejemplo del cuerpo que debes enviar:
```json
    {
      "name": "Juan Perez",
      "mail": "juan.perez@example.com",
      "github_url": "https://github.com/juanperez/latam-challenge.git"
    }
```

3. El plazo máximo de entrega del challenge son **5 días corridos completos** a partir de la recepción del challenge. Por ejemplo: Si recibiste el challenge el día jueves 21 de Septiembre a las 3 pm, tienes plazo hasta el martes 26 de septiembre a las 23:59.
3. Puedes utilizar las tecnologías y técnicas que prefieras para el procesamiento de datos. ¡Valoraremos tus conocimientos en plataformas cloud!. En tal caso, procura seguir el paso a paso en tus archivos **SIN** agregar las credenciales de acceso a los distintos servicios.
4. Los desafíos que posean un orden claro, sean explicativos, modulares, eficientes y creativos serán mejor rankeados. 
5. ¡Recuerda que no estamos en tu cabeza! Escribe los supuestos que estás asumiendo. Además, incluye las versiones de las librerías que estás usando en el archivo `requirements.txt`. Por favor, `NO BORRAR` lo que ya viene escrito en el archivo.
6. Para este desafío te recomendamos que describas claramente cómo mejorar cada parte de tu ejercicio en caso de que tenga opción de mejora.
7. Debes utilizar los datos contenidos en el [siguiente archivo](https://drive.google.com/file/d/1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis/view?usp=sharing).
8. Puedes utilizar la [documentación oficial de twitter](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object) para entender la estructura de los datos.
9. Evaluaremos positivamente las buenas prácticas de uso de git. Tus commits, branches, pull requests. 
10. Usa la rama main para cualquier versión final que quieras que revisemos. Te recomendamos que uses alguna práctica de [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). NOTA: No borres tus ramas de desarrollo.
10. Recuerda considerar el manejo de errores y casos borde.
11. Recuerda que vas a trabajar a la par con más desarrolladores, por lo que la mantenibilidad, legibilidad y escalabilidad de tu código es esencial.
12. Una buena documentación del código siempre ayuda al lector.

​
## Challenge
En el [archivo](https://drive.google.com/file/d/1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis/view?usp=sharing) encontrarás un conjunto aproximado de 398MBs. Se pide resolver los siguientes problemas implementando funciones, usando **2 enfoques por cada problema**: Uno en el que se optimice el tiempo de ejecución, y otro en que se optimice la memoria en uso.

Tu desafío debe tener al menos 6 archivos python en la carpeta `src`. Cada uno de estos archivos correspondiente a la función del mismo nombre, con el mismo formato que se indica en las instrucciones de más abajo. Solo deja la función. Además de eso, debes tener un archivo `.ipynb` donde expliques con mayor claridad tu código. En este jupyter notebook puedes ejecutar tus funciones, medir el tiempo de ejecución, memoria en uso y explayarte según estimes conveniente. Te recomendamos fuertemente que utilices celdas markdown para que expliques el paso a paso de tu código.

**NOTA:** los archivos `.py` y `.ipynb` de interés ya están creados en la estructura del desafío, solo debes completarlos con tu solución y/o agregar los archivos que estimes convenientes.
​
1. Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días. Debe incluir las siguientes funciones:
```python
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
Returns: 
[(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
```
​
2. Los top 10 emojis más usados con su respectivo conteo. Debe incluir las siguientes funciones:
```python
def q2_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("✈️", 6856), ("❤️", 5876), ...]
```
3. El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos. Debe incluir las siguientes funciones:
```python
def q3_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python

Returns: 
[("LATAM321", 387), ("LATAM_CHI", 129), ...]
```
​
## Sugerencias
* Para medir la memoria en uso te recomendamos [memory-profiler](https://pypi.org/project/memory-profiler/) o [memray](https://github.com/bloomberg/memray)
* Para medir el tiempo de ejecución te recomendamos [py-spy](https://github.com/benfred/py-spy) o [Python Profilers](https://docs.python.org/3/library/profile.html)


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_reject_shift(self, base_rejects, compare_rejects):

    if self.use_score_rej:
        # Filtramos las filas donde haya rechazo tanto en base como en comparación
        reject_merged = self.merged_total[base_rejects | compare_rejects][
            [self.identifier, f'{self.score_variable}_x', f'{self.score_variable}_y']
        ]

        # Verificamos si las columnas 'score_x' y 'score_y' existen
        if f'{self.score_variable}_x' not in reject_merged.columns or f'{self.score_variable}_y' not in reject_merged.columns:
            raise KeyError(f"Las columnas {self.score_variable}_x o {self.score_variable}_y no existen en reject_merged.")

        # Asignamos NaN a los valores que están fuera del rango
        reject_merged.loc[
            (reject_merged[f'{self.score_variable}_x'] >= self.min_sc) & 
            (reject_merged[f'{self.score_variable}_x'] <= self.max_sc),
            f'{self.score_variable}_x'
        ] = np.nan

        reject_merged.loc[
            (reject_merged[f'{self.score_variable}_y'] >= self.min_sc) & 
            (reject_merged[f'{self.score_variable}_y'] <= self.max_sc),
            f'{self.score_variable}_y'
        ] = np.nan

        # Convertimos a object
        reject_merged[f'{self.score_variable}_x'] = reject_merged[f'{self.score_variable}_x'].astype("object")
        reject_merged[f'{self.score_variable}_y'] = reject_merged[f'{self.score_variable}_y'].astype("object")

        rej_var = self.score_variable

    else:
        rej_var = self.reject_variable

    # Filtramos y completamos los valores faltantes
    reject_merged.dropna(thresh=2, inplace=True)
    reject_merged.fillna('Valid', inplace=True)

    # Generamos la tabla cruzada (crosstab)
    reject_crosstab = pd.crosstab(reject_merged[f"{rej_var}_x"], reject_merged[f"{rej_var}_y"])

    # Si estás generando un PDF o un gráfico
    if self.pdf:
        list_bins_index = reject_crosstab.index.tolist()
        list_bins_columns = reject_crosstab.columns.tolist()

        fig, ax = plt.subplots(figsize=(12, 12))
        sns.set(font_scale=2)

        # Mapa de calor
        crosstab_image = sns.heatmap(
            reject_crosstab, cmap='Reds', annot=True, cbar=False, 
            linecolor="white", linewidths=.5, robust=True, ax=ax, 
            vmin=0, vmax=np.diag(reject_crosstab).mean(), fmt='d', 
            annot_kws={'size':6, 'fontsize':45}
        )

        ax.xaxis.tick_top()
        ax.xaxis.set_label_position('top')

        for t in ax.texts:
            t.set_text('{:,d}'.format(int(t.get_text())))

        crosstab_image.set_yticklabels(list_bins_index, rotation=0, fontsize='xx-large')
        crosstab_image.set_xticklabels(list_bins_columns, horizontalalignment='center', rotation=0, fontsize='xx-large')
        crosstab_image.set_xlabel("Compare", fontsize='xx-large', fontstyle="italic")
        crosstab_image.set_ylabel("Base", fontsize='xx-large', fontstyle="italic")

        # Guardar el gráfico
        self.reject_shift = crosstab_image
        self.reject_shift.figure.savefig(f'{self.report_path} Reject Shifts Counts.png')

    # Creación del DataFrame para almacenar los resultados
    rej_tab = pd.DataFrame(columns=['Index', 'Columns', 'Values'])

    # Lista para almacenar las series a concatenar
    data_list = []

    for x in reject_crosstab.index:
        for y in reject_crosstab.columns:
            # Crear una serie con los valores de la tabla cruzada
            a_series = pd.Series([x, y, reject_crosstab.loc[x, y]], index=rej_tab.columns)
            data_list.append(a_series)

    # Concatenar las series y crear el DataFrame final
    rej_tab = pd.concat([rej_tab, pd.DataFrame(data_list)], ignore_index=True)

    # Añadir la columna de nombre de tabla
    rej_tab['Table_Name'] = 'Reject CrossTab'

    # Concatenar con self.meta_data
    self.meta_data = pd.concat([self.meta_data, rej_tab], ignore_index=True)
