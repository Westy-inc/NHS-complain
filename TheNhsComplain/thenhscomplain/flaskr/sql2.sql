-- Insert one task for each user from user_id 2 to 9
-- Insert one task for each user from user_id 2 to 9
INSERT INTO task (title, body, date, public, user_id)
VALUES
    ('Task for user2', 'This is the body of the task for user 2.', NOW(), TRUE, 2),
    ('Task for user3', 'This is the body of the task for user 3.', NOW(), TRUE, 3),
    ('Task for user4', 'This is the body of the task for user 4.', NOW(), TRUE, 4),
    ('Task for user5', 'This is the body of the task for user 5.', NOW(), TRUE, 5),
    ('Task for user6', 'This is the body of the task for user 6.', NOW(), TRUE, 6),
    ('Task for user7', 'This is the body of the task for user 7.', NOW(), TRUE, 7),
    ('Task for user8', 'This is the body of the task for user 8.', NOW(), TRUE, 8),
    ('Task for user9', 'This is the body of the task for user 9.', NOW(), TRUE, 9);

