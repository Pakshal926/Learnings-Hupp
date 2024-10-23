Here is way to handle this in PostgreSQL:

### 1. View Active Sessions
    - You can use the following query to view all active sessions and connections to the database:
```sql
SELECT 
    pid, 
    usename, 
    application_name, 
    client_addr, 
    state, 
    query 
FROM 
    pg_stat_activity
WHERE 
    datname = 'GiCare-Insurance-Manager';
 ``` 

 This will show you the Process ID (pid), username, and current state of the connections.

---

### 2. Terminate a Session
    - Once you've identified the session you want to terminate, you can run:
```sql
SELECT pg_terminate_backend(<pid>);
```

Replace <pid> with the actual Process ID of the session.

---

### 3. Terminate all Connections
    - If you need to disconnect all active sessions to the database, use this query:
```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'GiCare-Insurance-Manager'
  AND pid <> pg_backend_pid();
```

This will terminate all sessions except your current one.

---

### 4. Check for Locking Queries
    - If the issue is caused by a query holding locks, you can identify those queries:
```sql
SELECT * 
FROM pg_locks 
JOIN pg_stat_activity ON pg_locks.pid = pg_stat_activity.pid 
WHERE pg_stat_activity.datname = 'GiCare-Insurance-Manager';
```

This all commands can be used inside the query tool of the PgAdmin.

---
