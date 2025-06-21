from jinja2 import Environment, FileSystemLoader

def renderizar_plantilla(nombre_plantilla, contexto):
    env = Environment(loader=FileSystemLoader("plantillas"))
    template = env.get_template(nombre_plantilla)
    return template.render(contexto)