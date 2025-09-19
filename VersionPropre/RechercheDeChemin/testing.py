import pandas as pd
# attention au nom de base du fichier et de le foutre dans le bon répertoire
import my_algo as algo
# faire gaffe quand j'utilise des variables qui viennent d'algo il faut qu'elles soient globales !

df = pd.DataFrame(0, index=algo.liste_pixels_global,
                  columns=algo.liste_pixels_global)


trajet = algo.algo()

print(trajet)
# Pour inserer une liste ou tuple dans un df il faut convertir les colonnes du df en type object !
df = df.astype('object')

df.at[algo.pixel_arriverTuple, algo.pixel_debutTuple] = trajet
print(df)
