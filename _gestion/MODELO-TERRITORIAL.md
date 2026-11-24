# Modelo territorial reutilizable

Estado: estándar de trabajo abierto, sujeto a validación del piloto La Alberca.

## Arquitectura

Raíz del pueblo: /pueblos/conjuntos-historicos/<slug>/ para conjuntos históricos; la ubicación de otros pueblos se verificará contra la arquitectura vigente antes de crear URLs.

Secciones candidatas: historia, patrimonio, geografía y territorio, naturaleza, cultura y tradiciones, sociedad y economía, visitar y artículos. No son obligatorias: publicar únicamente cuando exista conocimiento específico suficiente. Las investigaciones transversales pertenecen a su ámbito principal y se enlazan desde los pueblos relacionados.

## Contrato documental

- Front matter: layout, title inequívoco, description específica, permalink estable; parent, grand_parent y nav_order cuando procedan.
- Comprobar referencias de navegación antes de renombrar títulos. No introducir campos SEO que el motor no consuma.
- H1 descriptivo, contenido propio y enlaces contextuales a documentos relacionados.
- last_modified_at basado en revisión sustantiva comprobada; no usar fecha de compilación.
- Registro de entidades: identificador estable, nombre, tipo Schema.org válido, URL y relaciones verificadas. Coordenadas y sameAs solo con evidencia.
- Fuentes identificables, distinción entre hechos, testimonios, tradiciones, interpretaciones, hipótesis y desconocimiento conforme al Canon IA.
- Inventarios y expedientes patrimoniales: identificadores locales estables, evidencia y estado de investigación; decidir explícitamente qué documentos son públicos. nav_exclude y search_exclude no garantizan privacidad ni desindexación.
- Imágenes: derechos verificados, atribución, texto alternativo y tamaño optimizado.

## Validación antes de expansión

1. Compilar y revisar HTML real, navegación, títulos, canonical, JSON-LD y enlaces.
2. Comprobar sitemap y llms.txt; distinguir documentos públicos de materiales internos.
3. Revisar rigor editorial y fuentes; no exigir cuotas de extensión ni secciones vacías.
4. Registrar incidencias técnicas separadamente de investigaciones pendientes.
5. Aplicar aprendizajes a nuevos pueblos sin copiar afirmaciones ni uniformar su historia.

La Alberca es el piloto metodológico, no una plantilla rígida. Este estándar complementa el Canon IA y el plan maestro; no los sustituye.
