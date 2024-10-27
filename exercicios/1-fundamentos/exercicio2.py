"""
Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto 
o próprio primeiro caractere

Ex:
fifa 23 → **fi$a 23
restart → resta$t
"""

name = "Fifa 23"
char = name[0].lower() #transformou a primeira letra em minuscula
new_name = name.replace(char, '$')
new_name = char + new_name[1:]
#print(new_name)




"""
Substituindo caractere repetido

Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:
abc xyz → **xyc abz** 
"""

st1 = "cab" #zyb
st2 = "zyx" #cax

new_st1 = st2[:2] + st1[2:]
print(new_st1)

new_st2 = st1[:2] + st2[2:]
print(new_st2)