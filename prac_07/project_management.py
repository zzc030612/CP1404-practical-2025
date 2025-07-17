"""
Project Management Program
Time Estimate: ~3 hours
"""

from project import Project
from datetime import datetime


def main():
    """Main function to manage projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save_decision = input("Would you like to save to projects.txt? (y/n): ").lower()
            if save_decision == "y":
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


def load_projects(filename):
    """Load projects from a text file."""
    projects = []
    try:
        with open(filename, "r") as file:
            file.readline()  # Skip header line
            for line in file:
                parts = line.strip().split("\t")
                projects.append(Project(*parts))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
    return projects


def save_projects(filename, projects):
    """Save projects to a text file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        for project in sorted(filtered_projects, key=lambda p: p.start_date):
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        project_index = int(input("Project choice: "))
        project = projects[project_index]
        print(project)
        new_completion = input("New Percentage: ")
        if new_completion:
            project.completion_percentage = int(new_completion)
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid project choice.")


if __name__ == "__main__":
    main()