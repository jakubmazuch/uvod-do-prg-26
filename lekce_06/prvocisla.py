def sito(limit):
    sito = [True] * limit
    sito[0] = False
    sito[1] = False
    
    for i in range(2, int(limit**0.5)+1):
        if sito[i]:
            for j in range(i*i, limit, i):
                sito[j] = False
                
    prvocisla = []
    for i in range(limit):
        if sito[i]:
            prvocisla.append(i)
    
    return prvocisla


limit = int(input("Zadejte mez:"))

print(f"\nPrvočísla menší než {limit}:")
print(sito(limit))