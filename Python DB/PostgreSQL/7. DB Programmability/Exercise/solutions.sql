--1.	User-defined Function Full Name

CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR(50), last_name VARCHAR(50))
RETURNS VARCHAR(100)
AS
$$
    DECLARE
        full_name VARCHAR(100);
    BEGIN
        IF first_name IS NULL AND last_name IS NULL THEN
            full_name := NULL;
        ELSIF first_name IS NULL THEN
            full_name := initcap(last_name);
        ELSIF last_name IS NULL THEN
            full_name := initcap(first_name);
        ELSE
            full_name := concat(initcap(first_name), ' ', initcap(last_name));
        END IF;
    RETURN full_name;
    END
$$
LANGUAGE plpgsql;

--2.	User-defined Function Future Value

CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    initial_sum DECIMAL,
    yearly_interest_rate DECIMAL,
    number_of_years INT
)
RETURNS DECIMAL
AS $$
    DECLARE
        future_value DECIMAL;
    BEGIN
        future_value := trunc(initial_sum * power(1 + yearly_interest_rate, number_of_years), 4);
    RETURN future_value;
    END;
$$
LANGUAGE plpgsql;

--OR

CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    IN initial_sum DECIMAL,
    IN yearly_interest_rate DECIMAL,
    IN number_of_years INT,
    OUT future_value DECIMAL
)

AS $$
    BEGIN
        future_value := trunc(initial_sum * power(1 + yearly_interest_rate, number_of_years), 4);
    END;
$$
LANGUAGE plpgsql;

--exammple
SELECT fn_calculate_future_value (1000, 0.1, 5);

--3.	User-defined Function Is Word Comprised

CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    IN set_of_letters VARCHAR(50),
    IN word VARCHAR(50),
    OUT bool_val BOOLEAN
)
AS $$
    DECLARE
        sub_letter CHAR(1);
        pos_letter INT;
        sub_set VARCHAR(50);
    BEGIN
        sub_set := LOWER(set_of_letters);

        WHILE CHAR_LENGTH(word) > 0 LOOP
            sub_letter := LEFT(LOWER(word), 1);
            pos_letter := POSITION(sub_letter IN sub_set);
            IF pos_letter = 0 THEN
                bool_val := FALSE;
                RETURN;
            ELSE
                word := SUBSTRING(word FROM 2);
                sub_set := LEFT(sub_set, pos_letter - 1) || RIGHT(sub_set, CHAR_LENGTH(sub_set) - pos_letter);
            END IF;
        END LOOP;
        bool_val := TRUE;

    END;
$$
LANGUAGE plpgsql;

--4.	Game Over

CREATE OR REPLACE FUNCTION fn_is_game_over(is_game_over BOOLEAN)
RETURNS TABLE(name VARCHAR(50), game_type_id INT, is_finished BOOLEAN)
AS $$
    BEGIN
        RETURN QUERY
        SELECT
	        g.name,
	        g.game_type_id,
	        g.is_finished
        FROM games AS g
        WHERE g.is_finished = is_game_over;
    END;
$$
LANGUAGE plpgsql;

--5. Difficulty Level

CREATE OR REPLACE FUNCTION fn_difficulty_level(
    IN level INT,
    OUT difficulty_level VARCHAR(50)
)
AS $$
    BEGIN
        IF level <= 40 THEN
           difficulty_level := 'Normal Difficulty';
        ELSIF level >= 41 AND level <= 60 THEN
            difficulty_level := 'Nightmare Difficulty';
        ELSE
            difficulty_level := 'Hell Difficulty';
        END IF;
    END
$$
LANGUAGE plpgsql;

--6. * Cash in User Games Odd Rows

CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE(total_cash NUMERIC)
AS $$
    BEGIN
        RETURN QUERY
        SELECT ROUND(SUM(cash)::NUMERIC, 2) AS "total_cash"
    FROM (
        SELECT cash,
               ROW_NUMBER() OVER (ORDER BY cash DESC) AS "row_number"
        FROM users_games AS ug
        JOIN games AS g
			ON ug.game_id = g.id
        WHERE g.name = game_name
    ) AS joined_table
    WHERE joined_table.row_number % 2 != 0;
    END
$$
LANGUAGE plpgsql;

--7. Retrieving Account Holders**

CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
AS $$
    DECLARE
        row_data RECORD;

        my_cursor CURSOR FOR
            SELECT
            ah.id,
            ah.first_name,
            ah.last_name,
            SUM(a.balance) AS "total_balance"
        FROM accounts AS a
            JOIN account_holders AS ah
                ON a.account_holder_id = ah.id
        GROUP BY
            ah.id,
            ah.first_name,
            ah.last_name
        ORDER BY
            ah.first_name,
            ah.last_name;

    BEGIN

        OPEN my_cursor;
        LOOP
            FETCH my_cursor INTO row_data;
            EXIT WHEN NOT FOUND;
            IF row_data.total_balance > searched_balance THEN
                RAISE NOTICE '% % - %', row_data.first_name, row_data.last_name, row_data.total_balance;
            END IF;
        END LOOP;

        CLOSE my_cursor;

    END;
$$
LANGUAGE plpgsql;

-- test
CALL sp_retrieving_holders_with_balance_higher_than(200000);

--8. Deposit Money

CREATE OR REPLACE PROCEDURE sp_deposit_money(account_id INT, money_amount NUMERIC(8, 4))
LANGUAGE plpgsql
AS $$
    BEGIN
       UPDATE accounts
        SET balance = balance + money_amount
        WHERE id = account_id;
    COMMIT;
    END
$$;

--test
CALL sp_deposit_money(10, 500);

SELECT *
FROM accounts as a
WHERE a.id = 10;

--9. Withdraw Money

CREATE OR REPLACE PROCEDURE sp_withdraw_money(account_id INT, money_amount NUMERIC(30, 4))
LANGUAGE plpgsql
AS $$
    DECLARE
        check_balance NUMERIC;
    BEGIN
        check_balance := (SELECT a.balance FROM accounts AS a WHERE a.id = account_id);

        IF check_balance >= money_amount THEN
            UPDATE accounts
            SET balance = balance - money_amount
            WHERE accounts.id = account_id;
            COMMIT;
        ELSE
            RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
        END IF;

    END;
$$;

--10. Money Transfer

CREATE OR REPLACE PROCEDURE sp_transfer_money(
    sender_id INT,
    receiver_id INT,
    amount NUMERIC(30, 4)
)
LANGUAGE plpgsql
AS $$
    DECLARE
        withdraw_rows INT := 0;
        deposit_rows INT := 0;

    BEGIN

        CALL sp_withdraw_money(sender_id, amount);
        GET DIAGNOSTICS withdraw_rows = ROW_COUNT;

        IF withdraw_rows = 0 THEN
            CALL sp_deposit_money(receiver_id, amount);
            GET DIAGNOSTICS deposit_rows = ROW_COUNT;

            IF deposit_rows = 0 THEN
                COMMIT;
            END IF;

        ELSE
            ROLLBACK;
        END IF;
    END;
$$;

--11. Delete Procedure

DROP PROCEDURE sp_retrieving_holders_with_balance_higher_than;

--12. Log Accounts Trigger

CREATE TABLE logs(
    id SERIAL PRIMARY KEY,
    account_id INT,
    old_sum NUMERIC,
    new_sum NUMERIC
);

CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs()
    RETURNS TRIGGER
AS $$
    BEGIN
        INSERT INTO logs(account_id, old_sum, new_sum)
        VALUES (OLD.id, OLD.balance, NEW.balance);
    RETURN NEW;
    END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_account_balance_change
    AFTER UPDATE OF balance ON accounts
    FOR EACH ROW
    WHEN (OLD.balance IS DISTINCT FROM NEW.balance)
    EXECUTE FUNCTION trigger_fn_insert_new_entry_into_logs();

--13. Notification Email on Balance Change

CREATE TABLE notification_emails(
    id SERIAL PRIMARY KEY,
    recipient_id INT,
    subject VARCHAR(200),
    body TEXT
);

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
    RETURNS TRIGGER
AS $$

    BEGIN

        INSERT INTO notification_emails(recipient_id, subject, body)
        VALUES (
                NEW.account_id,
                CONCAT('Balance change for account: ', NEW.account_id),
                CONCAT('On ', CURRENT_DATE,' your balance was changed from ',
            NEW.old_sum, ' to ', NEW.new_sum, '.')
                );
        RETURN NEW;
    END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_send_email_on_balance_change
    AFTER UPDATE OF new_sum ON logs
    FOR EACH ROW
    EXECUTE FUNCTION trigger_fn_send_email_on_balance_change();

-- test
INSERT INTO logs(account_id, old_sum, new_sum)
VALUES (1, 100, 200);

SELECT *
FROM notification_emails;
