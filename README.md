The Palle Admin Project is a role-based access control (RBAC) system built with Django for managing employees and students. It supports two user types:

Admin – Full permissions
Sales – Limited access
User Roles & Permissions:
Admin (Superuser/Full Control):View, add, update, and delete employees and students.Full access to Admin Dashboard.Can assign a student to any employee via the added_by dropdown
Sales (Restricted Access):Can add new students and view student list (read-only).Cannot modify/delete students or view employees.added_by is auto-filled with their own username
Technologies:
Backend: Python, Django (FBVs, ORM, authentication)
Frontend: Django Templates, HTML, Bootstrap, CSS
Database: MySQL with normalized schema and constraints

Admin users get full CRUD access
Sales users have limited access (add + read)
Dynamic dashboards based on role
Clean, secure handling of student assignments via added_by
Used Django ORM and Function-Based Views for all logic
Forms built using ModelForms for validation
Admin site used for backend data management
