# Requerimientos Funcionales

## Listado de Requerimientos

### Requerimieto Número 1

<table>
 <tr>
    <th>Nombre</th>
    <th>R1-Votar por un candidato</th>
 </tr>
 <tr>
    <th>Resumen</th>
    <td>Se incrementa un voto al número de votos actuales del
    candidato. Se debe especificar cuál fue el medio que más
    influenció a la persona para realizar dicha votación
    (Televisión, Radio o Internet). Dependiendo del medio
    seleccionado, el candidato recibirá un aumento en el costo de
    campaña</td>
 </tr>
 <tr>
    <th colspan="2">Entradas</th>
 </tr>
 <tr>
    <td colspan="2">El número del candidato, siendo opciones válidas
    candidato 1, 2 ó 3.</td>
 </tr>
 <tr>
    <td colspan="2">El medio publicitario que influenció en la votación
    (Televisión, Radio o Internet)</td>
 </tr>
 <tr>
    <th colspan="2">Resultados</th>
 </tr>
 <tr>
    <td colspan="2">El número total de votos del candidato se incrementó
    en 1.</td>
 </tr>
 <tr>
    <td colspan="2">El costo de campaña del candidato cuyo número se
    especifica en las entradas se incrementó dependiendo del medio
    publicitario. Si este fue Televisión, se incrementa en 1000; si
    fue Radio, se incremento en 500; si fue Internet, se incremento
    en 100.</td>
 </tr>
</table>

### Requerimieto Número 2

<table>
 <tr>
    <th>Nombre</th>
    <th>R2-Mostrar el costo de campaña de un candidato</th>
 </tr>
 <tr>
    <th>Resumen</th>
    <td>Se debe informar el costo de campaña de un candidato.
    El costo de campaña se calcula según el número de votos y la
    influencia (Televisión, Radio o Internet) sobre cada uno de
    ellos.</td>
 </tr>
 <tr>
    <th colspan="2">Entradas</th>
 </tr>
 <tr>
    <td colspan="2">El número del candidado, siendo opciones válidas
    candidato 1, 2 o 3.</td>
 </tr>
 <tr>
    <th colspan="2">Resultados</th>
 </tr>
 <tr>
    <td colspan="2">Costo de campaña del candidato escogido.</td>
 </tr>
</table>

### Requerimiento Número 3

<table>
 <tr>
    <th>Nombre</th>
    <th>R3-Vaciar la urna de votación</th>
 </tr>
 <tr>
    <th>Resumen</th>
    <td>Se debe reinicar los votos y los costos de campaña de todos
    los candidatos, de tal manera que el número de votos y el costo
    de campaña queden en cero.</td>
 </tr>
 <tr>
    <th colspan="2">Entradas</th>
 </tr>
 <tr>
    <td colspan="2">Ninguna</td>
 </tr>
 <tr>
    <th colspan="2">Resultados</th>
 </tr>
 <tr>
    <td colspan="2">Los votos de los candidatos quedan en cero.</td>
 </tr>
 <tr>
    <td colspan="2">Los costos de campaña de los candidatos quedan
    en cero.</td>
 </tr>
</table>

### Requerimiento Número 4

<table>
 <tr>
    <th>Nombre</th>
    <th>R4-Mostrar el total de votos en la urna</th>
 </tr>
 <tr>
    <th>Resumen</th>
    <td>Se debe informar el total de votos que hay en la urna
    (La suma de los votos de cada uno de los candidatos).</td>
 </tr>
 <tr>
    <th colspan="2">Entradas</th>
 </tr>
 <tr>
    <td colspan="2">Ninguna</td>
 </tr>
 <tr>
    <th colspan="2">Resultados</th>
 </tr>
 <tr>
    <td colspan="2">Total de votos en la urna.</td>
 </tr>
</table>

### Requerimiento Número 5

<table>
 <tr>
    <th>Nombre</th>
    <th>R5-Mostrar el porcentaje de votos de un candidato</th>
 </tr>
 <tr>
    <th>Resumen</th>
    <td>Se debe informar el porcentaje de votos obtenido por un
    candidato, es decir la razón del total de los votos de un
    candidato y el total de votos en la urna.</td>
 </tr>
 <tr>
    <th colspan="2">Entradas</th>
 </tr>
 <tr>
    <td colspan="2">El número del candidato, siendo opciones válidas
    candidato 1, 2 ó 3.</td>
 </tr>
 <tr>
    <th colspan="2">Resultados</th>
 </tr>
 <tr>
    <td colspan="2">Porcentaje de votos obtenidos por el candidato
    sobre todos los votos en la urna.</td>
 </tr>
</table>

### Requerimiento Número 6

<table>
 <tr>
    <th>Nombre</th>
    <th>R6-Mostrar el costo promedio de campaña</th>
 </tr>
 <tr>
    <th>Resumen</th>
    <td>Se debe informar el promedio del costo de campaña de los tres
    candidatos, es decir la razón de la sumatoria de los costos de
    campaña de los candidatos y el número total de candidatos.</td>
 </tr>
 <tr>
    <th colspan="2">Entradas</th>
 </tr>
 <tr>
    <td colspan="2">El número del candidato, siendo opciones válidas
    candidato 1, 2 ó 3.</td>
 </tr>
 <tr>
    <th colspan="2">Resultados</th>
 </tr>
 <tr>
    <td colspan="2">Costo promedio por campaña en las elcciones
    Cupi2.</td>
 </tr>
</table>