# PR-274 — Página informativa pública

2026-11-06 · issue #1 leído antes de editar · rama feat/pr-274-public-project-site.

Crear docs/index.html, estilo adaptable, 404 y marca HACKEAT suministrada por el titular.
Contenido informativo sobre un proyecto en desarrollo, sin fechas de lanzamiento ni
afirmaciones de servicio disponible. No formularios, cuenta, pagos, pedidos o llamadas a API.
No importar el código ni documentos de la plataforma privada. Mantener esa plataforma privada.

Validar enlaces/archivos, idioma, viewport, texto alternativo y ausencia de contenido activo
antes de PR. CI sobre runners hospedados GitHub; publicar main/docs sólo tras validar y merge.
Verificar HTTPS y recursos remotos, escritorio/móvil y página inexistente. Registrar resultado
y rollback en README, sin publicar datos internos del servidor o credenciales.

GitHub Pages sirve HTML/CSS y no aloja el backend ni sustituye un dominio propio para la app.
El aviso de alojamiento identifica la recogida de IP por GitHub para seguridad y enlaza su
política. Sin cookies propias ni analítica. Revisar cualquier cambio de alcance por separado.
