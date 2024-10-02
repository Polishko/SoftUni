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


Real-app example from ChatGPT with full validation on DB level and App-level, including models, forms and custom fields.

![image](https://github.com/user-attachments/assets/5026b805-398e-4a59-8d63-d0d354ed26d2)
![image](https://github.com/user-attachments/assets/c944d4bc-97da-4f9a-9b26-0ad23f6e02de)
![image](https://github.com/user-attachments/assets/cf8200b4-929d-48f6-80f5-bc16b4b8458e)
![image](https://github.com/user-attachments/assets/2145c24c-c0e4-4d7b-bf9c-2694f410df41)
![image](https://github.com/user-attachments/assets/d15108a7-6845-4d46-b9c1-a016ee9765a2)

![image](https://github.com/user-attachments/assets/512398e4-a0a0-4b1d-b6ae-c9f8ccce32f6)
![image](https://github.com/user-attachments/assets/c549629b-5815-4bd4-98c8-fff7479337fd)

![image](https://github.com/user-attachments/assets/e9989460-39dd-4712-b728-4a446b859254)

![image](https://github.com/user-attachments/assets/3051dd95-7335-42fa-a502-db7a5ad6f318)


Some more information
* Form and Model field validation

  ![image](https://github.com/user-attachments/assets/7fba022c-bb79-49bf-b2ef-9d1e6d3f6b33)

* Custom field validation

![image](https://github.com/user-attachments/assets/c5de24c2-8f97-4ca9-885a-8059f53e647b)

 ![image](https://github.com/user-attachments/assets/dfa3a64b-594f-425c-a895-7889e57a8b19)

* Calling full-clean?

  ![image](https://github.com/user-attachments/assets/82c747ec-24af-44c0-ad34-d977c85bee81)

  ![image](https://github.com/user-attachments/assets/d012bd40-4dab-47a5-9e05-0a8fb6913fe7)


* Has to_python really have to do anything with validating? (short answer: no! but you might need to)

![image](https://github.com/user-attachments/assets/fb8b8e5c-cec1-4b57-ba7d-005caf612d61)

* Validation of constraints

![image](https://github.com/user-attachments/assets/b518dbde-16b8-4431-bd80-5256ffb56306)

* Form vs. Model Error Messages

  ![image](https://github.com/user-attachments/assets/cff254c0-f30c-4fab-ac57-21d9fcfbb0f5)

  ![image](https://github.com/user-attachments/assets/6d78c371-00b7-44b4-88d4-621dc8947d98)

![image](https://github.com/user-attachments/assets/eafe3970-470b-41a5-b067-77e4206dcc9d)

![image](https://github.com/user-attachments/assets/ab2850c6-a98b-4a31-9e1c-23fc91a29aa3)

![image](https://github.com/user-attachments/assets/54a39227-58f6-4cd7-afce-511cab4142f9)

* More on clean() and full-clean()

![image](https://github.com/user-attachments/assets/10bd9432-a31d-447e-9f45-36e634ca2683)

![image](https://github.com/user-attachments/assets/86c4ece7-fbdb-4912-8086-c0f6eb2d0f96)

![image](https://github.com/user-attachments/assets/8a24b340-8705-4ec5-93c4-86e28e7756f3)

![image](https://github.com/user-attachments/assets/91e5eddc-9a5f-4cc6-a6f6-00f6286a6b53)

![image](https://github.com/user-attachments/assets/d0aaaa3d-4554-4a8d-88e4-48864bca62ea)



  









 
 
 
 
 
 
 
 
 
