(Based on Notes from lectures, HackSoftware Django Style Guide and answers from ChatGPT)


1.	Model level validation with clean

 ![image](https://github.com/user-attachments/assets/fc1b91f4-5677-4e98-846c-636d1c4a517f)

•  When it runs: This validation is triggered when calling the model’s clean() method, which is typically invoked when you call full_clean() on a model instance or when using Django forms.
•  Application level: This is an application-level validation. It runs only when you are using Django’s ORM and validation mechanisms. If data is inserted directly into the database (e.g., through raw SQL), this check is not enforced.
•  Flexibility: Since this is custom logic, it allows more flexibility to add any additional validation rules as needed.

![image](https://github.com/user-attachments/assets/a2fc044f-81cf-4d5d-a344-d18044068f69)

 
2.	DB level with constraints

   ![image](https://github.com/user-attachments/assets/460994b5-7327-4b53-a2bd-b74944a64e5e)

 
Leads to IngtegrityError: Related to data integrity but if you use full_clean and save (instead of create) you get validation error
•  When it runs: This is a database-level constraint, meaning it is enforced at the database level, not just within the Django application. The database will reject any invalid data, even if it’s inserted through a raw SQL query or another application.
•  Application independence: Since this constraint is enforced by the database, it applies even if someone interacts with the database directly (e.g., inserting data outside Django).
•  Performance: Database constraints are optimized for performance and ensure that invalid data is prevented from being inserted in the first place.
•  Less flexibility: The logic is more limited compared to the clean() method, as the database can only handle certain types of constraints (e.g., comparisons between fields).

 ![image](https://github.com/user-attachments/assets/8c2c086c-2478-4f7a-9ff7-9de04753ea6f)

![image](https://github.com/user-attachments/assets/bf7a9cb5-f00b-4229-9c8d-4b580f88db8c)

 
Field lvl vs model lvl, model level are constraints and field lvl are values entered in the db
 
 
 ![image](https://github.com/user-attachments/assets/ef428a84-a299-4237-b4a0-da689a5471cf)

 ![image](https://github.com/user-attachments/assets/bf518c60-15d6-497b-842a-76ed6dbf63f4)

 ![image](https://github.com/user-attachments/assets/4362103d-7bb0-4897-bcd7-d2f5c94bd30c)

 ![image](https://github.com/user-attachments/assets/9eb23f63-87b4-4e79-a950-4c187caffc92)

 ![image](https://github.com/user-attachments/assets/5430b2b5-ab1f-4fd7-afa6-caad77b94a1f)

 ![image](https://github.com/user-attachments/assets/0242acbc-74f3-494f-b1f4-52431c7087f8)

![image](https://github.com/user-attachments/assets/d194b573-2cde-44fb-94c3-f75c0bffc20e)

![image](https://github.com/user-attachments/assets/30290e69-7ca3-488c-9106-89fc4efdf1cf)

![image](https://github.com/user-attachments/assets/87b7a6f4-9283-4555-8a4c-a110f90804f7)

![image](https://github.com/user-attachments/assets/5a693e3b-0ff4-4a7f-913a-1e9219f67b9c)

![image](https://github.com/user-attachments/assets/b97813cf-7105-43be-8049-27954df04c26)

![image](https://github.com/user-attachments/assets/f778fb6c-f23b-4815-9822-ce5c6e4f5c1e)





 
 
 
 
 
 
 
 
 
