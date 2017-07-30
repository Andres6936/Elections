# Candidato

 La clase Candidato representa el candidato de la elección.

# Jerarquía de Clase

 Diagrama de la clase Candidato.

# Resumen de Métodos

 <b style="color: orange">
 <a href="#GetNombre">GetNombre</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#GetNombre">GetNombre</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#GetPartidoPolitico">GetPartidoPolitico</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#GetEdad">GetEdad</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#GetCostoCampanha">GetCostoCampanha</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#GetVotos">GetVotos</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#IngresarUnVoto">IngresarUnVoto</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#IngresarVotoTelevision">IngresarVotoTelevision</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#IngresarVotoRadio">IngresarVotoRadio</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#IngresarVotoInternet">IngresarVotoInternet</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#ReiniciarConteoVotos">ReiniciarConteoVotos</a>
 </b>

 <br>

 <b style="color: orange">
 <a href="#ReiniciarCostoCampanha">ReiniciarCostoCampanha</a>
 </b>

  <br>

# API Clase

Métodos
=======

---

<a name="__init__"></a>

**__init__**

    __init__()


----

<a name="GetNombre"></a>

**GetNombre**

    GetNombre(self):

Returns:
    Devuelve el nombre del Candidato.

----

<a name="GetApellido"></a>

**GetApellido**

    GetApellido(self):

Returns:
    Devuelve el apellido del Candidato.

----

<a name="GetPartidoPolitico"></a>

**GetPartidoPolitico**

    GetPartidoPolitico(self):

Returns:
    Devuelve el partido polítco del Candidato.

----

<a name="GetEdad"></a>

**GetEdad**

    GetEdad(self):

Returns:
    Devuelve la edad del Candidato.

---

<a name="GetCostoCampanha"></a>

**GetCostoCampanha**

    GetCostoCampanha(self):

Returns:
    Devuelve el costo de campaña del Candidato.

----

<a name="GetVotos"></a>

**GetVotos**

    GetVotos(self):

Returns:
    Devuelve el número de votos del Candidato.

----

<a name="IngresarUnVoto"></a>

**IngresarUnVoto**

    IngresarUnVoto(self):

Resumen:
    Ingresa un voto al candidato.

Poscondición:
    Se modificó el número de votos aumentándose el existente en 1.

----

<a name="IngresarVotoTelevision"></a>

**IngresarVotoTelevision**

    IngresarVotoTelevision(self):

Resumen:
    Adiciona un voto influenciado por la televisión.

Poscondición:
    Se adiciona al costo de la camapaña la suma de $1000 y se
    incrementa el número de votos en 1.

----

<a name="IngresarVotoRadio"></a>

**IngresarVotoRadio**

    IngresarVotoRadio(self):

Resumen:
    Adiciona un voto influenciado por la radio.

Poscondición:
    Se adiciona al costo de la campaña la suma de $500 y se
    incrementa el número de votos en 1.

----

<a name="IngresarVotoInternet"></a>

**IngresarVotoInternet**

    IngresarVotoInternet(self):

Resumen:
    Adiciona un voto influenciado por internet.

Poscondición:
    Se adiciona al costo de la camapaña la suma de $100
    y se incrementa el número de votos en 1.

----

<a name="ReiniciarConteoVotos"></a>

**ReiniciarConteoVotos**

    ReiniciarConteoVotos(self):

Resumen:
    Se reinicia el conteo de votos.

Poscondición:
    self.votos = 0

----

<a name="ReiniciarCostoCampanha"></a>

**ReiniciarCostoCampanha**

    ReiniciarCostoCampanha(self):

Resumen:
    Se reinicia el costo de camapaña.

Poscondición:
    self.costoCampanha = 0

 ----
