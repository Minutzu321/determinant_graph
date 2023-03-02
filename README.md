
# :large_orange_diamond: Metoda simpla si Metoda Gauss-Jordan

Programul ruleaza functiile aferente de 100 de ori si face o medie a timpului de executie pentru fiecare functie in parte.

Matricele sunt luate cu elemente intregi, la intamplare, cu dimensiunile de la 2 la 12.


### :pray: Executarea programului
Pentru a genera graficul, va trebui instalată biblioteca următoare:
```
pip install matplotlib
```

### :hammer_and_wrench: Alcătuirea proiectului

Funcția calculează mai întâi dimensiunea matricei de intrare luând lungimea matricei m. Apoi verifică dacă matricea este pătratică, afirmând că dimensiunea matricei este egală cu lungimea primului rând al matricei.
În cazul în care dimensiunea matricei este 1 sau 2, funcția returnează determinantul matricei folosind formula corespunzătoare.
În cazul în care dimensiunea matricei este mai mare de 2, funcția utilizează o abordare recursivă pentru a calcula determinantul. Aceasta inițializează o variabilă "det" la 0, apoi trece prin fiecare coloană a primului rând al matricei. Pentru fiecare coloană, se creează o submatrice prin eliminarea primului rând și a coloanei în cauză. Apoi calculează determinantul submatricei în mod recursiv, și îl înmulțește cu un cofactor care depinde de poziția coloanei. În cele din urmă, se adaugă produsul la variabila "det".
După ce toate coloanele au fost iterate, funcția returnează valoarea lui det.
```
def det_simplu_c(m: list[list]):
    n = len(m)
    assert n == len(m[0]), "Matricea nu e patratica!"
    if n == 1:
        return m[0][0]
    elif n == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    else:
        det = 0
        for j in range(n):
            subm = [[m[i][k] for k in range(n) if k != j] for i in range(1, n)]
            cofactor = (-1)**j * det_simplu_c(subm)
            det += m[0][j] * cofactor
        return det
```

Funcția calculează mai întâi dimensiunea matricei de intrare prin luarea lungimii matricei m și a lungimii primului rând al matricei m[0]. Apoi verifică dacă matricea este pătratică, afirmând că dimensiunea matricei este egală pentru rânduri și coloane.
Funcția inițializează o variabilă det la 1, care va stoca determinantul matricei.
Funcția trece prin fiecare rând al matricei. Pentru fiecare rând, aceasta găsește elementul cu cea mai mare valoare absolută din coloana corespunzătoare și înlocuiește rândul curent cu rândul care conține elementul respectiv.
În cazul în care cel mai mare element din coloană este 0, funcția returnează 0, deoarece matricea nu are inversă și, prin urmare, determinantul este 0.
În cazul în care rândurile au fost schimbate, funcția înmulțește determinantul cu -1 pentru a compensa schimbarea de semn.
Funcția înmulțește apoi determinantul cu valoarea elementului diagonal curent al matricei.
În cele din urmă, funcția efectuează operații pe rânduri asupra matricei folosind eliminarea gaussiană pentru a reduce matricea la forma triunghiulară superioară. Apoi returnează determinantul.
```
def det_gauss_jordan_c(m: list[list]):
    randuri, coloane = len(m), len(m[0])
    assert randuri == coloane, "Matricea nu e patratica"
    det = 1
    for i in range(randuri):
        m_val = abs(m[i][i])
        m_rand = i
        for j in range(i+1, randuri):
            if abs(m[j][i]) > m_val:
                m_val = abs(m[j][i])
                m_rand = j
        if m_val == 0:
            return 0
        if m_rand != i:
            m[i], m[m_rand] = m[m_rand], m[i]
            det *= -1
        det *= m[i][i]
        for j in range(i+1, randuri):
            c = m[j][i] / m[i][i]
            for k in range(i, coloane):
                m[j][k] -= c * m[i][k]
    return det
```
### :ok_hand: Rezultat:
![rezultat](https://raw.githubusercontent.com/Minutzu321/determinant_graph/main/grafic.png)
### :busts_in_silhouette: Realizator
- Chiruș Mina-Sebastian - Grupa 142
