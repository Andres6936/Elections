# Candidato

 La clase Candidato representa el candidato de la elección.

# Jerarquía de Clase

 Diagrama de la clase Candidato.

# Resumen de Métodos

 <b style="color: orange">GetNombre</b>

 <b style="color: orange">GetApellido</b>

 <b style="color: orange">GetPartidoPolitico</b>

 <b style="color: orange">GetEdad</b>

 <b style="color: orange">GetCostoCampanha</b>

 <b style="color: orange">GetVotos</b>

 <b style="color: orange">IngresarUnVoto</b>

 <b style="color: orange">IngresarVotoTelevision</b>

 <b style="color: orange">IngresarVotoRadio</b>

 <b style="color: orange">IngresarVotoInternet</b>

 <b style="color: orange">ReiniciarConteoVotos</b>

 <b style="color: orange">ReiniciarCostoCampanha</b>

# API Clase

Métodos
=======

---

    __init__()


----

**GetNombre**

    GetNombre(self):

    Returns:
        Devuelve el nombre del Candidato.

----

**GetApellido**

    GetApellido(self):

    Returns:
        Devuelve el apellido del Candidato.

----

**GetPartidoPolitico**

    GetPartidoPolitico(self):

    Returns:
        Devuelve el partido polítco del Candidato.

----

**GetEdad**

    GetEdad(self):

    Returns:
        Devuelve la edad del Candidato.

---

**GetCostoCampanha**

    GetCostoCampanha(self):

    Returns:
        Devuelve el costo de campaña del Candidato.

----

**GetVotos**

    GetVotos(self):

    Returns:
        Devuelve el número de votos del Candidato.

----

**IngresarUnVoto**

    IngresarUnVoto(self):

    Resumen:
        Ingresa un voto al candidato.

    Poscondición:
        Se modificó el número de votos aumentándose el existente en 1.

----

**IngresarVotoTelevision**

    IngresarVotoTelevision(self):

    Resumen:
        Adiciona un voto influenciado por la televisión.

    Poscondición:
        Se adiciona al costo de la camapaña la suma de $1000 y se
        incrementa el número de votos en 1.

----

**IngresarVotoRadio**

    IngresarVotoRadio(self):

    Resumen:
        Adiciona un voto influenciado por la radio.

    Poscondición:
        Se adiciona al costo de la campaña la suma de $500 y se
        incrementa el número de votos en 1.

----

**IngresarVotoInternet**

    IngresarVotoInternet(self):

    Resumen:
        Adiciona un voto influenciado por internet.

    Poscondición:
        Se adiciona al costo de la camapaña la suma de $100
        y se incrementa el número de votos en 1.

----

**ReiniciarConteoVotos**

    ReiniciarConteoVotos(self):

    Resumen:
        Se reinicia el conteo de votos.

    Poscondición:
        self.votos = 0

----

**ReiniciarCostoCampanha**

    ReiniciarCostoCampanha(self):

    Resumen:
        Se reinicia el costo de camapaña.

    Poscondición:
        self.costoCampanha = 0

 ----
