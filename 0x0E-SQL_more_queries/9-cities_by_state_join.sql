-- cities contained in database
select ct.id, ct.name, st.name from cities AS ct INNER JOIN states AS st ON ct.state_id = st.id ORDER BY ct.id
