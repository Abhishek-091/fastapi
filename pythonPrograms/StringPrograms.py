import javalang
from pydantic import BaseModel

def extract_spring_components(java_file_path):
        """Extract Spring components (Controllers, Services, Repositories)"""
        with open(java_file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        try:
            tree = javalang.parse.parse(content)
        except Exception as e:
            print(f"Error parsing {java_file_path}: {e}")
            return []

        components = []

        # Look for Spring annotations
        for path, node in tree.filter(javalang.tree.ClassDeclaration):
            annotations = [a.name for a in node.annotations]

            if any(a in ['Controller', 'RestController', 'Service', 'Repository', 'Component'] for a in annotations):
                component_info = {
                    'name': node.name,
                    'type': next((a for a in annotations if
                                  a in ['Controller', 'RestController', 'Service', 'Repository', 'Component']), None),
                    'path': java_file_path,
                    'package': tree.package.name if tree.package else None,
                    'methods': [],
                    'dependencies': []
                }

                # Extract methods
                for method in node.methods:
                    method_annotations = [a.name for a in method.annotations]

                    method_info = {
                        'name': method.name,
                        'return_type': str(method.return_type) if method.return_type else None,
                        'parameters': [{'name': p.name, 'type': str(p.type)} for p in method.parameters],
                        'annotations': method_annotations
                    }

                    # Extract JavaDoc if available
                    if method.documentation:
                        method_info['documentation'] = method.documentation

                    component_info['methods'].append(method_info)

                # Extract dependencies (fields with @Autowired or constructor params)
                for field in node.fields:
                    field_annotations = [a.name for a in field.annotations]
                    if 'Autowired' in field_annotations:
                        for declarator in field.declarators:
                            component_info['dependencies'].append({
                                'name': declarator.name,
                                'type': str(field.type)
                            })
                            # Add to dependency graph
                            # self.dependency_graph[node.name].append(str(field.type))

                # Constructor injection
                for constructor in [m for m in node.methods if m.name == node.name]:
                    for param in constructor.parameters:
                        component_info['dependencies'].append({
                            'name': param.name,
                            'type': str(param.type)
                        })
                        # Add to dependency graph
                        # self.dependency_graph[node.name].append(str(param.type))

                components.append(component_info)

        return components

components = extract_spring_components('C:\\Users\\AbhishekPatidar\\Learning\\python\\FastApiDemo\\pythonPrograms\\Test.java')




class User():
    name: str
    email: str | None = None
    age: int
    salary: float | None = None
     

    def set_user(self, name: str, email: str | None, age: int, salary: float | None):
        self.name = name
        self.email = email
        self.age = age
        self.salary = salary

    def get_user(self):
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "salary": self.salary
        }
    
user = User()

user.set_user("Abhishek", "a@gmail.com", 25, 1000.0)
print(user.get_user())


demo = {
    "name" : "Abhishek",
    "age" : 25,
    "email" : "hello"
}

for key in demo:
    print(f"{key} : {demo[key]}")