-- Creates a trigger that decrease
-- the qunatity of an item
-- after adding new order
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		IF NEW.email <> OLD.email THEN
			SET NEW.valid_email = 0;
		END IF;
	END;//
	DELIMITER;
