* Using 'only' in template inheritance: purpose

![image](https://github.com/user-attachments/assets/d0fa7cea-0dca-44ac-be7a-a28cc1684196)

![image](https://github.com/user-attachments/assets/2ef1aadb-4cb3-498f-b2c0-cd3014e12e37)

* The @register.inclusion_tag(template-name.html) tells Django, when the following custom tag is used render the template-name.html template. Provides modularity, reusability.

* Filter functions
![image](https://github.com/user-attachments/assets/b46c571c-70d5-437a-a446-0a927b4ebb20)
{{ post.content|markdown:'This is the param' }}
![image](https://github.com/user-attachments/assets/9c688ae3-1d3f-48c6-9af7-e62a019c0922)
