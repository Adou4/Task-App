from storage import Storage
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load_tasks()
    
    def add_task(self, title, description=""):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_at": None
        }
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print(f"Tâche '{title}' ajoutée avec succès!")
    
    def display_tasks(self):
        if not self.tasks:
            print("Aucune tâche pour le moment.")
            return
        
        print("\n=== Liste des Tâches ===")
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            print(f"{task['id']}. [{status}] {task['title']}")
            if task["description"]:
                print(f"   Description: {task['description']}")
            print(f"   Créée le: {task['created_at']}")
            if task["completed"]:
                print(f"   Complétée le: {task['completed_at']}")
            print()
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                if not task["completed"]:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.storage.save_tasks(self.tasks)
                    print(f"Tâche '{task['title']}' marquée comme complétée!")
                else:
                    print("Cette tâche est déjà complétée.")
                return
        print("ID de tâche non trouvé.")
    
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_title = task["title"]
                del self.tasks[i]
                # Réorganiser les IDs
                for j, t in enumerate(self.tasks[i:], start=i):
                    t["id"] = j + 1
                self.storage.save_tasks(self.tasks)
                print(f"Tâche '{deleted_title}' supprimée avec succès!")
                return
        print("ID de tâche non trouvé.")