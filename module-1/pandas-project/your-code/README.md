README.md

# Proyecto Pandas

Dada una base de datos de ataques de tiburones, debíamos sacar una hipótesis para posteriormente proceder a depurar la base de datos.

--------

## Hipótesis
### Los hombres sufren más ataques de tiburones debido a que asumen comportamientos con mayor riesgo.
----


La revista Forbes afirma "A diferencia de la testosterona, la hormona femenina, la oxitocina, actúa en gran medida como responsable de la estabilidad emocional femenina pero de forma calmada y explicaría, según el estudio de AFS Finance, que en plena crisis financiera a las mujeres inversoras les fuera mucho mejor que a sus homólogos masculinos."

Cabe añadir que el sexo masculino sí es muy propenso a tomar riesgos, esto se debe a que los hombres adquieren mayor estatus social asumiendo este tipo comportamientos. También la asunción de riesgos y conductas violentas, sobre todo en la edad adulta joven, está relacionado con el establecimiento de órdenes jerárquicos entre sus competidores.

*Fuente: ¿Son los hombres más proclives a asumir riesgos que las mujeres?*: https://forbes.es/empresas/43241/son-los-hombres-mas-proclives-a-asumir-riesgos-que-las-mujeres/

---

Para el análisis y limpieza de datos dado que la BB.DD. muestra 25.723 filas y 24 columnas, he decidido centrarme en tan solo 6 columnas que me permitan obtener los datos que necesito o bien que me ayuden a averiguar datos erroneos, inexactos o NaN de otras columnas.

He eliminado todos los datos duplicados, y convertido los datos NaN de la columna 'Years' a 'flotantes' para después convertir toda la columan en 'int'.


Después elimino los NaN y todos aquellos valores inferiores a 1.970, para poder obtener los datos agrupados por decadas.

Modifico el nombre de la columna 'Sex' para dejar todos los nombres bajo el mismo patrón y termino de limpiar aquellos datos que dentro de la columna sexo no refieren a hombre o mujer, ayudándome de la variable nombre en muchos de ellos.

El resultado es una gráfica que muestra ya no solo que el ataque de tiburones a los hombre es mucho mayor que a las mujeres, sino que tanto en cómputo global como divididos por cuota ha aumentado estrepitosmanente los ataques a ambos sexos.