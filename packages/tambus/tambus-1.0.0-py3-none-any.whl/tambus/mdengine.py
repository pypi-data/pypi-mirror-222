from components import Component

class MDEngine:
    
    def __init__(self, components: list[Component]):
        self.components = components 
    
    
    def translate(self, content: str):
        for component in self.components:
            content = component.replace_regex(content)
        return content
