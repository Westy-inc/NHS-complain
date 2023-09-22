
-- SQLite
-- Insert one task for each user from user_id 2 to 9 with the current date and time
INSERT INTO tasks (title, body, date, public, user_id)
VALUES
    ('Task for user2', 'This is the body of the task for user 2.', CURRENT_TIMESTAMP, TRUE, 2),
    ('Task for user3', 'This is the body of the task for user 3.', CURRENT_TIMESTAMP, TRUE, 3),
    ('Task for user4', 'This is the body of the task for user 4.', CURRENT_TIMESTAMP, TRUE, 4),
    ('Task for user5', 'This is the body of the task for user 5.', CURRENT_TIMESTAMP, TRUE, 5),
    ('Task for user6', 'This is the body of the task for user 6.', CURRENT_TIMESTAMP, TRUE, 6),
    ('Task for user7', 'This is the body of the task for user 7.', CURRENT_TIMESTAMP, TRUE, 7),
    ('Task for user8', 'This is the body of the task for user 8.', CURRENT_TIMESTAMP, TRUE, 8),
    ('Task for user9', 'This is the body of the task for user 9.', CURRENT_TIMESTAMP, TRUE, 9);
