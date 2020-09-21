update from auth_user WHERE (id!=1);

update auth_user 
SET 
    id = 1
WHERE 
    id = 6;

update app_symptomentry
SET 
    symptom_id = 1
Where 
    id = 5;

DELETE FROM app_entry;


update django_admin_log
SET 
    user_id = 1
WHERE 
    user_id = 6;







