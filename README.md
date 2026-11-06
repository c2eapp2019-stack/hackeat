# HACKEAT

Web informativa de un proyecto en desarrollo.

Dirección prevista: https://c2eapp2019-stack.github.io/hackeat/

## Publicación

GitHub Pages desde la rama main y la carpeta /docs, con HTTPS obligatorio.
Sólo /docs se sirve como web. Ningún archivo de la plataforma privada se importa aquí.
El commit inicial de GitHub contiene sólo este README; las modificaciones pasan por PR.

## Comprobación local

Python 3, sin dependencias externas:

```sh
python scripts/validate_site.py
python -m http.server 8088 --bind 127.0.0.1 --directory docs
```

Abrir http://127.0.0.1:8088/. Revisar también un ancho móvil y la página 404.html.
CI comprueba estructura y recursos en cada PR; la revisión visual sigue siendo necesaria.

## Alcance

No incluye aplicación, formularios, inicio de sesión, compras, cookies propias ni analítica.
No contiene retornos de autenticación. No es una declaración de disponibilidad comercial.
No identifica al titular legal ni sustituye avisos que requiera un futuro servicio comercial.
El logo procede del material de marca entregado por el titular para su uso en HACKEAT;
no se concede una licencia de reutilización de la marca o de otros activos.

GitHub puede recoger datos técnicos de las visitas conforme a su política, enlazada en la web.
Consultar [qué es Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
y [sus límites](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).

## Reversión

Para corregir contenido, revertir mediante PR el commit afectado y verificar la publicación.
Para retirar el sitio, desactivar Pages en los ajustes del repositorio; no borrar el historial.
No conectar este repositorio a los runners privados del PC o a secretos de la plataforma.
