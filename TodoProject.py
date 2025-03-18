import mysql.connector as mysql

con = mysql.connect(host="localhost", user="root", passwd="admin")
cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")
cursor.execute("USE TODOAPP")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")
 
for i in cursor:
    print(i)
 
 
while True:
    print("\n Task Management")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
 
    choice = input("Enter your choice: ").strip()
 
    if choice == "1":
        task = input("Enter task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        con.commit()
        print("Task added successfully!")
    
    
    elif choice == "2":
        cursor.execute("SELECT * FROM tb_todo")
        tasks = cursor.fetchall()
        if tasks:
            print("\nYour Tasks:")
            for task in tasks:
                print(f"{task[0]}. {task[1]}")
        else:
            print("No tasks available.")

    elif choice == "3":
        task_id = input("Enter task ID to update: ")
        new_task = input("Enter new task: ")
        cursor.execute("UPDATE tb_todo SET task = %s WHERE id = %s", (new_task, task_id))
        con.commit()
        print("Task updated successfully!")

    elif choice == "4":
        task_id = input("Enter task ID to delete: ")
        cursor.execute("DELETE FROM tb_todo WHERE id = %s", (task_id,))
        con.commit()
        print("Task deleted successfully!")
 
    elif choice == "5":
        print("Exiting Task Management...")
        break
 
    else:
        print("Invalid choice. Please try again.")
 
cursor.close()
con.close()
