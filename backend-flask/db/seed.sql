-- We create this file to initially ad values to the database 
INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
  ('Amine Rayes', 'aminerayes' ,'MOCK'),
  ('Andrew Brown', 'andrewbrown' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'aminerayes' LIMIT 1),
    'This was imported as seed data for initialization!',
    current_timestamp + interval '10 day'
  )