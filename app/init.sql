CREATE DATABASE IF NOT EXISTS techsecure_db;
USE techsecure_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    service_id VARCHAR(50) NOT NULL
);

-- Mots de passe cryptés avec Bcrypt pour le mot de passe clair : TechSecure2026!
INSERT INTO users (username, password_hash, service_id) VALUES
('admin.infra', '$2b$12$7R3C3p1Ym1KxN1y6w36f6eMvG8wQ8Vv8n3Y86jS0Vz2g3Zq7G7K1.', 'infra'),
('cyber.sec', '$2b$12$7R3C3p1Ym1KxN1y6w36f6eMvG8wQ8Vv8n3Y86jS0Vz2g3Zq7G7K1.', 'cyber'),
('cloud.pme', '$2b$12$7R3C3p1Ym1KxN1y6w36f6eMvG8wQ8Vv8n3Y86jS0Vz2g3Zq7G7K1.', 'cloud_pme'),
('cloud.collect', '$2b$12$7R3C3p1Ym1KxN1y6w36f6eMvG8wQ8Vv8n3Y86jS0Vz2g3Zq7G7K1.', 'collectivites')
ON DUPLICATE KEY UPDATE username=username;
