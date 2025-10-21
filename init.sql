-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data into the 'users' table
INSERT INTO users (name, email) VALUES
('Arjun', 'arjun@example.com'),
('Bobby', 'bobby@example.com'),
('Charlie', 'charlie@example.com');
