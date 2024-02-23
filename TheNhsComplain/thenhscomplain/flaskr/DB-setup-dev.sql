-- Inserting data into Trust table with exact column names
INSERT INTO trusts (TrustName, region, HeadquartersAddress) VALUES
('North Healthcare Trust', 'North Region', '123 Main Street, City A'),
('South Healthcare Trust', 'South Region', '456 Oak Avenue, City B'),
('East Healthcare Trust', 'East Region', '789 Elm Road, City C'),
('West Healthcare Trust', 'West Region', '890 Pine Boulevard, City D'),
('Central Healthcare Trust', 'Central Region', '567 Cedar Lane, City E');




-- Inserting 20 hospitals into Hospital1 with 5 trusts
INSERT INTO hospitals (HospitalName, HospitalAddress, trustID) VALUES
('City General Hospital', '789 Oak Lane, Metropolis', 1),
('Central Medical Center', '456 Maple Street, Capital City', 2),
('Sunset Health Clinic', '123 Pine Avenue, Serenity Town', 3),
('Metro Community Hospital', '890 Elm Road, Downtown', 4),
('Unity Medical Center', '567 Cedar Lane, Harmonyville', 5),
('Greenfield General', '234 Birch Street, Green Valley', 1),
('Golden Valley Hospital', '789 Willow Avenue, Tranquil Springs', 2),
('Lakefront Medical Center', '456 Rose Boulevard, Lakeside', 3),
('Sunrise Health Clinic', '123 Oak Lane, Sunshine Town', 4),
('Harbor Regional Hospital', '890 Elm Road, Coastal City', 5),
('Meadowview Medical Center', '567 Pine Avenue, Meadowville', 1),
('Highland General', '234 Cedar Lane, Highlands', 2),
('Silver Springs Hospital', '789 Birch Street, Silver City', 3),
('Valley Medical Center', '456 Willow Avenue, Valleytown', 4),
('Maple Grove Health Clinic', '123 Rose Boulevard, Mapleville', 5),
('Riverside Regional Hospital', '890 Oak Lane, Riverside', 1),
('Sunnydale Medical Center', '567 Maple Street, Sunnyville', 2),
('Pinecrest General', '234 Pine Avenue, Pinecrest', 3),
('Oceanfront Hospital', '789 Cedar Lane, Oceanview', 4),
('Mountainview Medical Center', '456 Elm Road, Mountain City', 5);
