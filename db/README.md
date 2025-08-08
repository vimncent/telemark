## Schema

### logs
+------------+---------------+--------------------------+-----------------------------------------+
| Column     | Type          | Constraints              | Description                             |
+------------+---------------+--------------------------+-----------------------------------------+
| id         | SERIAL        | PRIMARY KEY              | Unique log entry identifier             |
| user       | VARCHAR(255)  | NOT NULL                 | Telegram username or user ID            |
| timestamp  | TIMESTAMPTZ   | NOT NULL                 | When the event actually occurred        |
| text       | TEXT          | NOT NULL                 | Free-form description of the event      |
| tags       | TEXT[]        | (nullable)               | Array of tag strings (e.g. [“health”])  |
| created_at | TIMESTAMPTZ   | NOT NULL DEFAULT NOW()   | When we recorded the log into the DB    |
+------------+---------------+--------------------------+-----------------------------------------+

Indexes:

  • idx_logs_user      ON logs(user)
  • idx_logs_timestamp ON logs(timestamp)
